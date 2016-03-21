#Character generator project
#This chooses their background features, like religion and ancestry
#Note that these are all based on Canadian Census statistics, extrapolated to 2030 by both Statistics Canada and personally by me!

from random import random

dReligion = { 1:'Catholic',
			  3:'Protestant',
			  5:'Christian Orthodox',
			  4:'Other Christian',
			  2:'Muslim',
			  6:'Jewish',
			  7:'Buddhist',
			  8:'Hindu',
			  9:'Sikh',
			  10:'Other Religion',
			  11:'None' }

def genReligion():
	x = random() * 100.0
	rel = -189.973 + (13.3556 * x) - (0.336317 * (x**2)) + (0.00362483 * (x**3)) - (0.0000139634 * (x**4))
	return dReligion[max(1, min(11, round(rel)))]

vPopSinglBackground = 0.65
vPopMultiBackground = 0.35

lSingleBackground = [ 'North American Indian', 'Métis', 'Inuit', 'Other Aboriginal', 'Filipino', 'Chinese', 'South Asian', 'Black', 'Latin American', 'Southeast Asian', 'Arab', 'West Asian', 'Korean', 'Japanese', 'Other Visible Minority', 'Canadian', 'English', 'French', 'Scottish', 'Irish', 'German', 'Italian', 'Ukranian', 'Dutch', 'Polish', 'Russian', 'Welsh', 'Norwegian', 'Portugese', 'British Isles', 'Swedish', 'Other Nationality'] 

dMultiBackground = { 'Métis':2.21, 'Inuit':0.14, 'North American Indian':5.37, 'Canadian':33.41, 'English':40.27, 'French':28.72, 'Scottish':32.13, 'Irish':29.9, 'German':19.42, 'Italian':5.45, 'Chinese':1.63, 'Ukranian':7.03, 'Dutch':5.67, 'Polish':5.53, 'East Indian':1.41, 'Russian':3.11, 'Welsh':3.2, 'Filipino':0.89, 'Norwegian':3.0, 'Portugese':1.15, 'British Isles':2.40, 'Swedish':2.37, 'MULT_MINOR':1.03 }

def genAncestry():
	#This one generates a lot of scotts; my function may be a little off, eh.
	if random() < vPopSinglBackground:
		#Only one background
		x = random() * 100.0
		num = 1.25103 + (0.810964 * x) - (0.0551849 * (x**2)) + (0.00173663 * (x**3)) - (0.0000219102 * (x**4)) + (9.5533 * (10**(-8)) * (x**5))
		lReturn = [ lSingleBackground[max(0, min(len(lSingleBackground), round(num)))] ]
		return lReturn
	else:
		#Multiple backgrounds
		lBackgrounds = []
		while len(lBackgrounds) < 2:
			for key in dMultiBackground.keys():
				if random() * 100.0 < dMultiBackground[key]:
					if key is 'MULT_MINOR':
						newBack = lSingleBackground[round(random() * 10.0) + 5]
						if newBack not in lBackgrounds:
							lBackgrounds.append(newBack)
					else:
						if key not in lBackgrounds:
							lBackgrounds.append(key)
				if len(lBackgrounds) >= 2:
					break
		return lBackgrounds

def gen():
	return { 'Religion':genReligion(), 'Ancestry':list(genAncestry()) }