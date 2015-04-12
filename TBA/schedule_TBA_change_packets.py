import TBA_communicator3 as tba
import json
import os
import shutil as sh

# Created by Colin Unger 
# Year: 2015

keys = ['uploadedData.maxFieldToteHeight', 'uploadedData.stackPlacing', 'match.officialRedScore', 'match.officialBlueScore']

competition = input("Competition: ")
year = int(input("Year: "))

print('\n')

print('Getting event info for competition ' + competition)
event = json.loads(tba.makeEventRequest(competition, year))
print('Got event info for competition ' + competition)

eventName = event['name']
compCode = event['key']

teamsJSON = json.loads(tba.makeEventTeamsRequest(competition, year))
teamNames = {}
for team in teamsJSON:
	teamNames[team['team_number']] = team['nickname']

print('Getting teams at event ' + competition)
matchesJSON = json.loads(tba.makeEventMatchesRequest(competition, year))
print('Got teams at event ' + competition)

if os.path.isdir('Change Packets'):
	print('Deleting directory "Change Packets"')
	sh.rmtree('Change Packets')
	print('Deleted directory "Change Packets"')
print('Creating directory "Change Packets"')
os.mkdir('Change Packets')
print('Created directory "Change Packets"')

for match in matchesJSON:
	if match['comp_level'] == 'qm':
		matchName = match['comp_level'][:1].upper() + str(match['match_number'])
		for alliance in match['alliances']:
			for team in match['alliances'][alliance]['teams']:
				teamNum = int(team[3:])

				j = {}
				j['class'] = 'Team'
				j['uniqueValue'] = teamNum
				j['allianceColor'] = alliance

				cs = []
				for key in keys:
					c = {}
					c['keyToChange'] = 'matchData.' + matchName + '.' + key
					c['valueToChangeTo'] = -1
					cs.append(c)

				ct = {}
				ct['keyToChange'] = 'name'
				ct['valueToChangeTo'] = teamNames[teamNum]
				cs.append(ct)
				j['changes'] = cs

				fileName = 'Change Packets/' + str(teamNum) + '_' + matchName + '_creation|' + str(match['match_number']) + '.json'
				f = open(fileName, 'w')
				print('Writing to file ' + fileName)
				print(json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')), file=f)
