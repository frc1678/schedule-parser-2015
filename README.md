Schedule Parser
===

How to use:

**Getting teams from TBA:**
```
cd TBA/
python teams_TBA.py
```
This will remove everything in the directory `Change Packets` as well as the files `teams.csv` and `teams.json` if the respective options are chosen.

---

**~~Scraping from FIRST:~~**
```
cd FIRST/
rm schedule.csv
rm schedule.json
python scrape.py CASA 2014 > schedule.csv
python makejson.py "Competition Name" > schedule.json
```
The JSON version of the scraper gets team nicknames from The Blue Alliance, thus it takes a bit longer.
