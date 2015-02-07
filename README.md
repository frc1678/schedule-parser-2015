Schedule Parser
===

How to use:

```
rm schedule.csv
rm schedule.json
python scrape.py CASA 2014 > schedule.csv
python makejson.py "Competition Name" > schedule.json
```

The JSON version gets team nicknames from The Blue Alliance, thus it takes a bit longer.