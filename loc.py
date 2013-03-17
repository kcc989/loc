import os
from os import listdir
from os.path import isfile, join

def ensure(f,y):
	d = os.path.dirname(y)
	;print y
	if not os.path.isdir(y):
		os.makedirs(y)
	
		

def main():
	years = [10,11,12,13]
	loc = os.path.dirname(os.path.abspath(__file__))
	for year in years:
		yearDir = (loc + "\\" + str(year))
		print yearDir
		ensure(yearDir,year)
	onlyfiles = [ f for f in listdir(loc) if isfile(join(loc,f)) ]
	modDate = []
	locPath = os.listdir(loc)
	realNames = []
	for fname in onlyfiles:
		realNames.append(loc + "\\" + fname)
	for i in realNames:
		if os.path.isfile(i):
			z = os.path.getmtime(i)
			modDate.append(z)
		
	i = 0
	while i < len(modDate):
		#print locPath[i] + ": " + str(modDate[i])
		i += 1
main()