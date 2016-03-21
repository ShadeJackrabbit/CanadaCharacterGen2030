def readFromFileToDict(filename, dictionary):
	f = open(filename, 'r')
	for line in f:
		sData = line.split(';')
		dictionary[sData[0]] = sData[1:len(sData)-1]
		for n in range(len(dictionary[sData[0]])):
			dictionary[sData[0]][n] = int(dictionary[sData[0]][n])
	f.close()

dFemaleNames = {}
dMaleNames = {}

readFromFileToDict("nameDataBoys.txt", dMaleNames)
readFromFileToDict("nameDataGirls.txt", dFemaleNames)

def indexNames(dictionary, total):
	tempDict = {}
	prevValue = 0
	for key in dictionary.keys():
		stat = dictionary[key][len(dictionary[key])-1] 
		if int(stat) is not 0:
			tempDict[key] = stat / total * 100 + prevValue
			prevValue = tempDict[key]
	return tempDict
		
def getTotalPop(dictionary):
	val = 0
	for key in dictionary.keys():
		val += dictionary[key][len(dictionary[key])-1] 
	return val

dMaleNames = indexNames(dMaleNames, getTotalPop(dMaleNames))
dFemaleNames = indexNames(dFemaleNames, getTotalPop(dFemaleNames))

def writeDictToTable(dataDict):
	strOutput = ''
	for key in dataDict.keys():
		strOutput += key + ':' + str(dataDict[key]) +'\n'
	return strOutput

def writeDataToFile(fileName, dataString):
	fileData = open(fileName, 'w')
	fileData.write(dataString)
	fileData.close()

writeDataToFile("nameIndexBoys.txt", writeDictToTable(dMaleNames))
writeDataToFile("nameIndexGirls.txt", writeDictToTable(dFemaleNames))