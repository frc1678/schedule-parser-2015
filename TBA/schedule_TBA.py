import TBA_communicator as tba
import json
import re		

def matchJSONToMatch(json):
	match = ""
	match += (re.sub('(?<=[A-Z])[A-Z]', '', str.upper((json["comp_level"]).encode('ascii','ignore'))) + str(json["match_number"]) + ",")
	for team in json["alliances"]["red"]["teams"]:
		match += team[3:]
		match += ","
	for team in json["alliances"]["blue"]["teams"]:
		match += team[3:]
		match += ","
	return match[:-1]

competition = "casa"
year = "2015"

print competition
print json.loads(tba.makeEventRequest(competition, year))["name"]

matchesJSON = json.loads(tba.makeEventMatchesRequest(competition, year))

for matchJSON in matchesJSON:
	print matchJSONToMatch(matchJSON)

#print str(matches)