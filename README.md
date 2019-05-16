Useful Commands in MongoDB CLI and import export example of MongoDB

# CLI in MongDB
> show databases
> use reportsdb
> db.dropDatabase()
> db.reports.find({})


# CMD Import / Export MongoDB ( as administrator )
```
Give the example
```

And repeat

```
until finished
```

```
> cd C:\Program Files\MongoDB\Server\4.0\bin
```
> mongoexport -d reportsdb -c reports -o exportReportDBOutput.json
```
> mongoimport --db reportsdb --collection reports --file exportReportDBOutput.json
