import urllib.request
import re

rListItem = r'<li>.+</li>'
rWord = r'[a-zA-Z]+'
rNum = r'[0-9]+'

dFemaleNames = {}
dMaleNames = {}

def extractDataPairsFromList(listIn, dictOut, columnLabel = 'NUM'):
	for entry in listIn:
		entry = entry[4:len(entry)-5]
		name = re.search(rWord, entry).group(0)
		if name == 'nbsp' or name == 'N':
			continue
		num = int(re.search(rNum, entry).group(0))
		if name in dictOut.keys():
			dictOut[name][columnLabel] = num
		else:
			dictOut[name] = { columnLabel : num }

def getBabyNamesFromVancouver(year = 2012):
	sock = urllib.request.urlopen("http://www.vs.gov.bc.ca/babynames/baby"+str(year)+".html")
	htmlSource = str(sock.read(), encoding='utf8')
	sock.close()

	girlsDataSection = htmlSource[htmlSource.index('<a name="gnames">'):htmlSource.index('<a name="bnames">')]
	boyysDataSection = htmlSource[htmlSource.index('<a name="bnames">'):htmlSource.index('<div id="rightColumn">')]
	lGirlsNamesData = re.findall(rListItem, girlsDataSection)
	lBoyysNamesData = re.findall(rListItem, boyysDataSection)

	extractDataPairsFromList(lGirlsNamesData, dFemaleNames, str(year))
	extractDataPairsFromList(lBoyysNamesData, dMaleNames, str(year))

for i in range(2001, 2013):
	print(i)
	getBabyNamesFromVancouver(i)

def writeDictToTable(dataDict):
	strOutput = ''
	for key in dataDict.keys():
		strOutput += key + ';'
		for i in range(2001, 2013):
			if str(i) in dataDict[key].keys():
				strOutput += str(dataDict[key][str(i)]) + ';'
			else:
				strOutput += '0;'
		strOutput += '\n'
	return strOutput

def writeDataToFile(fileName, dataString):
	fileData = open(fileName, 'w')
	fileData.write(dataString)
	fileData.close()

writeDataToFile("nameDataBoys.txt", writeDictToTable(dMaleNames))
writeDataToFile("nameDataGirls.txt", writeDictToTable(dFemaleNames))