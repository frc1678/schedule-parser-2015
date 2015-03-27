import TBA_communicator as tba
import json
import os
import shutil as sh

competition = 'casa'
year = 2015

competition = raw_input("Competition: ")
year = int(raw_input("Year: "))

inputCSV = raw_input('Export as csv file to teams.csv? (Y, n): ') 
inputJSON = raw_input('Export as json file to teams.json? (Y, n): ')
inputChangePackets = raw_input('Export as change packet json files to directory "Change Packets"? (Y, n): ')

outputAsCSV = inputCSV != 'n' and inputCSV != 'N'
outputAsJSON = inputJSON != 'n' and inputJSON != 'N'
outputAsChangePackets = inputChangePackets != 'n' and inputChangePackets != 'N'

print '\n'

print 'Getting event info for competition ' + competition
event = json.loads(tba.makeEventRequest(competition, year))
print 'Got event info for competition ' + competition

eventName = event['name']
compCode = event['key']

print 'Getting teams at event ' + competition
teamsJSON = json.loads(tba.makeEventTeamsRequest(competition, year))
print 'Got teams at event ' + competition

if outputAsCSV:
	print 'Opening csv file'
	f = open('teams.csv','w')
	print 'Writing to csv file'
	f.write(eventName + ',' + compCode)
	for team in teamsJSON:
		f.write('\n' + str(team['team_number']) + ',' + team['nickname'])
	f.close()
	print 'Finished csv file'

if outputAsJSON:
	print 'Opening csv file'
	f = open('teams.json','w')
	print 'Writing to json file'
	e = {'event_name' : eventName, 'comp_code' : compCode}
	j = []
	j.append(e)

	for team in teamsJSON:
		t = {'number' : team['team_number'], 'name' : team['nickname']}
		j.append(t)

	f.write(json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))
	f.close()
	print 'Finished json file'

if outputAsChangePackets:
	if os.path.isdir('Change Packets'):
		print 'Deleting directory "Change Packets"'
		sh.rmtree('Change Packets')
		print 'Deleted directory "Change Packets"'
	print 'Creating directory "Change Packets"'
	os.mkdir('Change Packets')
	print 'Created directory "Change Packets"'

	for team in teamsJSON:
		j = {}
		j['class'] = 'Team'
		j['uniqueValue'] = team['team_number']
		cs = []
		c = {}
		c['keyToChange'] = 'name'
		c['valueToChangeTo'] = team['nickname']
		cs.append(c)
		j['changes'] = cs
		print 'Opening json file for team ' + str(team['team_number'])
		f = open('Change Packets/' + str(team['team_number']) + '.json', 'w')
		print 'Writing to json file for team ' + str(team['team_number'])
		f.write(json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))
		f.close()
		print 'Finished json file for team ' + str(team['team_number'])
