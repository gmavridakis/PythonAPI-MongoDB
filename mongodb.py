from xml.etree.ElementTree import fromstring, ElementTree, SubElement, Element
import urllib.request
import xmltodict
import json
import pymongo
import time
from pprint import pprint

def insert_forms_into_db(_date):
    print('Hitting API with date : ')
    print(_date)
    # Hit example api with specific data
    request = 'https://example.com/v1/example?token=example_token&date={0}'.format(_date)
    response = urllib.request.urlopen(request).read().decode("utf-8")
    # creates db if not exists
    dbcon = pymongo.MongoClient("mongodb://localhost:50000/")
    # store it in reportsdb
    reportsdb = dbcon["reportsdb"]
    # create column in db
    reportscol= reportsdb["reports"]    
    # parse response in respdict
    respdict = xmltodict.parse(response)
    #print(respdict["Forms"])
    if respdict["Forms"] == None :
        # OrderedDict([('Forms', None)]) 
        print('Got {0} form(s) for {1}'.format(0,_date))
    else:
        #<class 'list'> -> return of typeof in many
        #<class 'collections.OrderedDict'> -> return of typeof in one
        res = type(((respdict["Forms"])["Form"])).__name__
        print(res)
        if res == 'list' : 
            print('Got {0} form(s) for {1}'.format('many',_date))
            key,forms = respdict["Forms"].popitem()
            respjson = json.loads(json.dumps(forms, indent=4))        
            reportscol.insert_many(respjson)
        else:
            print('Got {0} form(s) for {1}'.format(1,_date))
            respjson = json.loads(json.dumps(respdict, indent=4))
            reportscol.insert_one(respjson)

    dbcon.close()

### Hit API for total days for a specific month and year ###
def hit_api(days,month,year):
    count=1
    while(count<=days):
        date = '' +str(year) +'-' + str(month) +'-' +str(count)
        time.sleep(7)
        insert_forms_into_db(date)
        count +=1

# This function will hit example API with delay of 7 seconds for dates 1/1/2018 - 31/1/2018 and store data in mongodb
hit_api(31,1,2018)