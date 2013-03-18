import os, time, shutil, locator
from os import listdir
from os.path import isfile, join

def ensure(f):
	if not os.path.isdir(f):
		os.makedirs(f)

def member(element, lst):
	for i in lst:
		if i == element:
			return True
	return False
	
def main():
	loc = locator.module_path()
	onlyfiles = [ f for f in listdir(loc) if isfile(join(loc,f)) ]
	realNames = []
	for fname in onlyfiles:
		realNames.append(loc + "\\" + fname)
	fileYear = []
	for i in realNames:
		if os.path.isfile(i):
			fileYear.append(time.ctime(os.path.getmtime(i))[20:24])
	i = 0
	yearPath = []
	years = []
	for i in fileYear:
		if member(i, years) == False:
			years.append(i)
	for year in years:
		yearDir = (loc + "\\" + str(year))
		ensure(yearDir)
		yearPath.append(yearDir)
	i = 0
	while i < len(realNames):
		j = 0
		destination = ""
		while j < len(yearPath):
			if fileYear[i] == years[j]:
				destination = yearPath[j]	
			j += 1
		if destination != "":
				shutil.move(realNames[i],destination)
		i += 1
main()
