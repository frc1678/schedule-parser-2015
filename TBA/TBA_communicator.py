from urllib2 import Request, urlopen

# Created by Colin Unger 
# Year: 2015

basicURL = "http://www.thebluealliance.com/api/v2/"

headers = {"X-TBA-App-Id" : "cdu:TBA_communicator:0"} # set to "<your initials>:TBA_communicator:0"

def setHeadersForApp(yourName, appName, versionNumber):
	headers = {"X-TBA-App-Id" : str(yourName) + str(appName) + str(versionNumber)}

def makeRequest(url):
	#print url
	request = Request(url, headers = headers)
	return urlopen(request).read()

def getTeamListRequestKey(pageNumber):
	return "teams/{pageNumber}".format(pageNumber = pageNumber)

def makeTeamListRequest(pageNumber):
	return makeRequest(basicURL + getTeamListRequestKey(pageNumber))

def getTeamRequestKey(teamNumber):
	return "team/frc{teamNumber}".format(teamNumber = teamNumber)

def makeTeamRequest(teamNumber):
	return makeRequest(basicURL + getTeamRequestKey(teamNumber))

def getTeamEventsRequestKey(teamNumber, year):
	return "team/frc{teamNumber}/{year}/events".format(teamNumber = teamNumber, year = year)

def makeTeamEventsRequest(teamNumber, year):
	return makeRequest(basicURL + getTeamEventsRequestKey(teamNumber, year))

def getTeamEventAwardsRequestKey(teamNumber, competition, year):
	return "/api/v2/team/frc{teamNumber}/event/{year}{competition}/awards".format(teamNumber = teamNumber, year = year, competition = competition)

def makeTeamEventAwardsRequest(teamNumber, year):
	return #finish this later

def getEventRequestKey(competition, year):
	return "event/{year}{competition}".format(competition = competition, year = year)

def makeEventRequest(competition, year):
	return makeRequest(basicURL + getEventRequestKey(competition, year))

def getEventMatchesRequestKey(competition, year):
	return "event/{year}{competition}/matches".format(competition = competition, year = year)

def makeEventMatchesRequest(competition, year):
	return makeRequest(basicURL + getEventMatchesRequestKey(competition, year))

def getEventTeamsRequestKey(competition, year):
	return "event/{year}{competition}/teams".format(competition = competition, year = year)

def makeEventTeamsRequest(competition, year):
	return makeRequest(basicURL + getEventTeamsRequestKey(competition, year))

def getEventStatsRequestKey(competition, year):
	return "event/{year}{competition}/stats".format(competition = competition, year = year)

def makeEventStatsRequest(competition, year):
	return makeRequest(basicURL + getEventStatsRequestKey(competition, year))

