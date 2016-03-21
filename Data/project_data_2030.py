import numpy as np

dFemaleNames = {}
dMaleNames = {}

dataYearRange = range(2001, 2013)
projectedYear = 2030
dataFinalYearRange = list(dataYearRange)
dataFinalYearRange.append(projectedYear)

def readFromFileToDict(filename, dictionary):
	f = open(filename, 'r')
	for line in f:
		sData = line.split(';')
		dictionary[sData[0]] = sData[1:len(sData)-1]
		for n in range(len(dictionary[sData[0]])):
			dictionary[sData[0]][n] = int(dictionary[sData[0]][n])
	f.close()

readFromFileToDict("nameDataBoys.txt", dMaleNames)
readFromFileToDict("nameDataGirls.txt", dFemaleNames)

#import matplotlib.pyplot as plt
#plt.ylabel('Number Born')
#plt.xlabel('Year')

from scipy.optimize import curve_fit

def projectToFuture(year, dictionary):
	numpasses = 0
	for key in dictionary.keys():
		#getting trend line to shift sin values
		trend = np.polyfit(dataYearRange, dictionary[key], 1)

		#using some code from http://stackoverflow.com/a/16716964
		amp = 3 * np.std(dictionary[key])/(2 ** 0.5)
		offset = lambda x:((np.mean(dictionary[key]) + np.polyval(trend, x)) / 2)
		sin_f = lambda x, phase: amp * np.sin(x - phase) + offset(x)

		#find the offset
		try:
			fitpars, covmat = curve_fit(sin_f, dataYearRange, dictionary[key], maxfev=700)
		except RuntimeError:
			print("Error: Could not fit. Defaulting to phase zero.")
			fitpars = [0]

		#project trend
		dictionary[key].append(max(0, sin_f(year, fitpars[0])))

		##draw curve for debugging
		#test_x = np.linspace(2001, projectedYear, 100) # 100 linearly spaced numbers
		#test_y = sin_f(test_x, fitpars[0]) # computing the values of sin(x)/x
		#
		##draw to graph
		#if numpasses < 1:
		#	plt.plot(dataFinalYearRange, dictionary[key], '-')
		#	plt.plot(test_x, test_y, '--')
		#	break;
		
		numpasses += 1
		print("Predictions made: ", numpasses, "/", len(dictionary.keys()))

projectToFuture(projectedYear, dMaleNames)
projectToFuture(projectedYear, dFemaleNames)

#plt.show()

def writeDictToTable(dataDict):
	strOutput = ''
	for key in dataDict.keys():
		strOutput += key + ';'
		for i in range(13):
			strOutput += str(dataDict[key][i]) + ';'
		strOutput += '\n'
	return strOutput

def writeDataToFile(fileName, dataString):
	fileData = open(fileName, 'w')
	fileData.write(dataString)
	fileData.close()

writeDataToFile("nameDataBoys2030.txt", writeDictToTable(dMaleNames))
writeDataToFile("nameDataGirls2030.txt", writeDictToTable(dFemaleNames))