## Useful Commands in MongoDB CLI and import export example of MongoDB

### CLI in MongDB
```
Show Databases
```
  > show databases
```
Use a database
```
  > use reportsdb
```
Drop the database
```
  > db.dropDatabase()
```
Show Contents of database
```
  > db.reports.find({})
```
 Show IP's connected to db
```
  > db.currentOp(true).inprog.forEach(function(d){if(d.client)print(d.client, d.connectionId)})


### CMD Import / Export MongoDB ( as administrator )
```
Go to folder with mongoexport/monogimport exe
```
  > cd C:\Program Files\MongoDB\Server\4.0\bin
```
Export reportsdb with collection reports in json format
```
  > mongoexport -d reportsdb -c reports -o exportReportDBOutput.json
```
Import reportsdb with collection reports from .json file
```
  >  mongoimport --db reportsdb --collection reports --file exportReportDBOutput.json
```
