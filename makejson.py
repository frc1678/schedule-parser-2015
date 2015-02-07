import csv
import json
import sys
import requests

schedule = {"matches":[]}

tbaAppId = 'frc1678:schedule_downloader:1'
teams = {}

with open('schedule.csv', 'rb') as csvFile:
	csvReader = csv.reader(csvFile, delimiter=',', quotechar='\"')
	for row in csvReader:
		if len(row) == 1:
			schedule["compCode"] = row[0]
			schedule["compName"] = sys.argv[1]
		else:
			if row != []:
				rt1r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[2]), headers={'X-TBA-App-Id': tbaAppId})
				rt2r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[3]), headers={'X-TBA-App-Id': tbaAppId})
				rt3r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[4]), headers={'X-TBA-App-Id': tbaAppId})
				bt1r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[5]), headers={'X-TBA-App-Id': tbaAppId})
				bt2r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[6]), headers={'X-TBA-App-Id': tbaAppId})
				bt3r = requests.get("http://www.thebluealliance.com/api/v2/team/frc{num}".format(num=row[7]), headers={'X-TBA-App-Id': tbaAppId})

				rt1rr = json.loads(rt1r.text)['nickname']
				rt2rr = json.loads(rt2r.text)['nickname']
				rt3rr = json.loads(rt3r.text)['nickname']
				bt1rr = json.loads(bt1r.text)['nickname']
				bt2rr = json.loads(bt2r.text)['nickname']
				bt3rr = json.loads(bt3r.text)['nickname']

				teams[row[2]] = json.loads(rt1r.text)['nickname']
				teams[row[3]] = json.loads(rt2r.text)['nickname']
				teams[row[4]] = json.loads(rt3r.text)['nickname']
				teams[row[5]] = json.loads(bt1r.text)['nickname']
				teams[row[6]] = json.loads(bt2r.text)['nickname']
				teams[row[7]] = json.loads(bt3r.text)['nickname']


				schedule["matches"].append({"name": row[1], "redAlliance": [{"number": row[2], "name": rt1rr}, {"number": row[3], "name": rt2rr}, {"number": row[4], "name": rt3rr}], "blueAlliance": [{"number": row[5], "name": bt1rr}, {"number": row[6], "name": bt2rr}, {"number": row[7], "name": bt3rr}]})


print(json.dumps(schedule, sort_keys=True, indent=4, separators=(',', ': ')))