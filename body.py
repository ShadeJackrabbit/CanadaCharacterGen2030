#Character generator project
#This chooses body features

from random import random
from numpy import exp
from numpy.random import normal

dSleepDisorders = { 'Bruxism':13.0, 'Restless Leg Syndrome':8.5, 'Rapid eye movement behavior disorder':0.5, 'Narcolepsy':0.05, 'Obstructive sleep apnea':5.0, 'Snoring':35.0 }

def genSex():
	#Half-n-half odds
	if (random() > 0.51):
		return "Male"
	else:
		return "Female"

def genAge(sex, minimum = 12, maximum = 86):
	age = 0
	while (age < minimum or age > maximum):
		x = random() * 50
		if sex is "Male":
			age = 4.8831 - (2.56 * x) + (0.765 *(x**2)) - (0.06 *(x**3)) + (0.00219 *(x**4)) - (0.000039 *(x**5)) + (2.660*(10**(-7))*(x**6))
		else:
			age = 3.3298 - (1.72 * x) + (0.643 *(x**2)) - (0.05 *(x**3)) + (0.00186 *(x**4)) - (0.000033 *(x**5)) + (2.264*(10**(-7))*(x**6))
	return age

def genHeight(sex, age, minimum = 120):
	if sex is "Male":
		avg = 55.4569 + (12.8112 * age) - (0.463094 *(age**2)) + (0.00690439 *(age**3)) - (0.000036748 *(age**4))
		dev = 0.521294 + (1.19338 * age) - (0.0797696*(age**2)) + (0.00239874 *(age**3)) - (0.0000330695 *(age**4)) + (1.69632*(10**(-7))*(age**5))
	else:
		avg = 53.638 + (13.7638 * age) - (0.597792 *(age**2)) + (0.0106054 *(age**3)) - (0.0000660119 *(age**4))
		dev = 0.681796 - (4.63564*(10**(-28))) * exp(age) + (1.32768*age) - (0.113382 *(age**2)) + (0.00429827*(age**3)) - (0.0000736469 *(age**4)) + (4.6587 * (10**(-7)) *(age**5))
	result = 0
	while (result <= minimum):
		result = normal(avg, max(dev, 1))
	return result

def genWeight(sex, age, minimum = 40, maximum = 160):
	if sex is "Male":
		avg = 8.14413 - (0.947303*age) + (0.810396*(age**2)) - (0.0506978*(age**3)) + (0.00132382*(age**4)) - (0.0000159615*(age**5)) + (7.31837*(10**(-8))*(age**6))
		dev = -3.06963 + (2.04638*age) - (0.0910433*(age**2)) + (0.00159937*(age**3)) - (9.66068*(10**(-6))*(age**4))
	else:
		avg = -4.73772 - (1.62009*(10**(-27)))*exp(age) + (6.10373*age) - (0.178605*(age**2)) + (0.00165265*(age**3))
		dev = 1.65959 + (8.66302*(10**(-27))*exp(age)) - (2.21431*age) + (0.871924*(age**2)) - (0.0909011*(age**3)) + (0.00436892*(age**4)) - (0.000108096*(age**5)) + (1.3384*(10**(-6))*(age**6)) - (6.57234*(10**(-9))*(age**7))
	result = 0
	while (result <= minimum or result >= maximum):
		result = normal(avg, max(dev, 1))
	return result

def gen():
	#Height in m, weight in kg
	dBody = { 'Sex':'NONE',
			  'Age':0,
			  'Height':0,
		  	  'Weight':0 }
	dBody['Sex'] = genSex()
	dBody['Age'] = int(genAge(dBody['Sex']))
	dBody['Height'] = int(genHeight(dBody['Sex'], dBody['Age']))
	dBody['Weight'] = int(genWeight(dBody['Sex'], dBody['Age']) * 2.20462)
	return dBody