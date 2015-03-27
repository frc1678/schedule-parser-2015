Schedule Parser
===

How to use:

Getting teams from TBA:
```
python TBA/teams_TBA.py
```

Scraping from FIRST (currenly not functional)
```
rm schedule.csv
rm schedule.json
python FIRST/scrape.py CASA 2014 > FIRST/schedule.csv
python FIRST/makejson.py "Competition Name" > FIRST/schedule.json
```

The JSON version gets team nicknames from The Blue Alliance, thus it takes a bit longer.