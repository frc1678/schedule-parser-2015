import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 3: # Make sure there are enough arguments
	print("Usage: {name} comp year".format(name=sys.argv[0]))
	sys.exit(1)

r = requests.get('http://www2.usfirst.org/{year}comp/Events/{code}/ScheduleQual.html'.format(year=sys.argv[2],code=sys.argv[1])) # Download the schedule HTML

soup = BeautifulSoup(r.text) # Parse the schedule HTML into a BeautifulSoup object

print(sys.argv[1])

for tag in soup.find_all('tr'): # Find all the table rows
	if tag.get('style', '') == "background-color:#FFFFFF;": # Filter them by the ones that have a white background.  A bit of a hack, but it's the best way
		numParsed = 0
		for child in tag.children:
			if child.name == "td": # Only parse TDs
				sys.stdout.write("\"" + child.contents[0] + "\"") # Print with quotes.  See RFC 4180
				numParsed = numParsed + 1
				if numParsed < (sum(1 for _ in tag.children)-1)/2: # If this is the last TD, don't print the comma
					sys.stdout.write(",")
	print("")