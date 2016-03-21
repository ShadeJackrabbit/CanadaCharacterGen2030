#Character generator project
#This chooses a personality type and can also describe each type

from random import random
from numpy import log

lPersonalityConfigs = [ 'ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ', 'ENTJ' ]

percentOdd = lambda: random()*100.0

def gen():
	num = min(int(random()*16.0), 15)
	sPersonality = lPersonalityConfigs[num]
	lPersonTraits = []
	for cFlip in sPersonality:
		fEmotive = open('TraitLists/'+cFlip+".txt", 'r')
		lDescriptors = fEmotive.read().split('\n')
		num = min(int(random()*len(lDescriptors)), len(lDescriptors)-1)
		lPersonTraits.append(lDescriptors[num])
		fEmotive.close()
	return lPersonTraits

#Following values are percentages, i.o.w. x/100
dDisorders = { 'Generalized Anxiety Disorder':3.2, 'Phobia':15.0, 'Panic Disorder':0.4, 'Social Anxiety Disorder':12.0, 'Obsessive Compulsive Disorder':2.5, 'Obsessive Compulsive Personality Disorder':1.0, 'Paranoid Personality Disorder':1.25, 'Delusional Disorder':(27.0/100000.0), 'Psychopathy':1.2, 'Depression':10.0, 'Bipolar Disorder':6.4, 'Posttraumatic Stress Disorder':8.1, 'Schizophrenia':0.45, 'Alcoholism':12.0, 'Pathological Gambling':1.7, 'Hypersexuality':4.5, 'Binge eating disorder':3.0, 'Bulimia':0.7, 'Anorexia':0.2, 'Cannabis Dependance':2.2, 'Avoidant Personality Disorder':0.3, 'Body Dysmorphic Disorder':0.9, 'Borderline Personality Disorder':1.5, 'Claustrophobia':3.5, 'Depersonalization Disorder':2.4, 'Dyslexia':7.5, 'Dissociative identity disorder':2.0, 'Hallucinogen persisting perception disorder':0.66, 'Histrionic personality disorder':2.0, 'Trichotillomania':2.45, 'Pyromania':3.0, 'Intermittent explosive disorder':0.3, 'Kleptomania':0.6, 'Sexual Compulsion':5.5, 'Skin Picking':5.0, 'Compulsive Shopping':5.0, 'Dyscalculia':4.5, 'Narcissistic personality disorder':1.0, 'Night eating syndrome':1.5, 'Pica':6.1, 'Schizoaffective disorder':0.5, 'Schizoid personality disorder':0.4, 'Seasonal affective disorder':13.0, 'Separation anxiety disorder':7.0 }

dSleepDisorders = { 'Confusional Arousals':4.0, 'Insomnia':6.0, 'Sleep Talking':4.0, 'Delayed sleep-phase disorder':0.15, 'Advanced sleep phase disorder':0.01, 'Non-24-hour sleep-wake disorder':0.06, 'Irregular sleep–wake rhythm':0.01, 'Sleep paralysis':6.2, 'Recurring Out-of-body Experiences':5.5 }

dSpeechDisorders = { 'Stuttering':1.0, 'Mutism':0.08 }

dPhobias = { 74.0:'Glossophobia', 68.0:'Necrophobia', 30.5:'Arachnophobia', 18.0:'Aquaphobia', 11.0:'Nyctophobia', 10.0:'Acrophobia', 7.9:'Sociophobia', 6.5:'Aerophobia', 2.5:'Claustrophobia', 2.2:'Agoraphobia', 2.5:'Claustrophobia', 2.2:'Agoraphobia', 2.0:'Brontophobia'}

#Sleep impairment is percentage compared to the national average (100 is equivalent to everywhere else)
def genDisorder(age=0, sleepImpairMult=1):
	lDisorders = []
	for key in dDisorders.keys():
		if (percentOdd() < dDisorders[key]):
			lDisorders.append(key)
	for key in dSleepDisorders.keys():
		if (percentOdd() < dSleepDisorders[key]):
			lDisorders.append(key)
	for key in dSpeechDisorders.keys():
		if (percentOdd() < dSpeechDisorders[key]):
			lDisorders.append(key)
	if "Obsessive Compulsive Disorder" in lDisorders and "Obsessive Compulsive Personality Disorder" in lDisorders:
		lDisorders.remove("Obsessive Compulsive Disorder")

	#Alzheimer
	alzOdds = lambda a: -679.767 + 160.0798 * log(a) 
	if (age > 0 and percentOdd() < alzOdds(age)):
		lDisorders.append("Alzheimer's")

	#Autism Spectrum Disorders
	num = percentOdd()
	if (num < 0.1):
		lDisorders.append("Autism")
	elif (num < 0.7):
		lDisorders.append("Autism Spectrum Disorder")
	elif (num < 0.76):
		lDisorders.append("Asperger Syndrome")

	#Nightmares
	mareOdd = lambda a: 14361 * a**(-2.9573)
	if (age > 0 and percentOdd() < mareOdd(age) * sleepImpairMult):
		lDisorders.append("Nightmare Disorder")

	#Sleepwalking
	walkOdd = lambda a: -1.3583 * a + 28.15
	if (percentOdd() < walkOdd(age) * sleepImpairMult):
		lDisorders.append("Sleepwalking")

	#Night Terrors
	terrOdd = lambda a: numpy.cos(a*numpy.pi()*2/24)*0.2+36.144*a**(-1.63)
	if (age > 0 and percentOdd() < terrOdd() * sleepImpairMult):
		lDisorders.append("Night Terrors")

	#Phobias
	while 'Phobia' in lDisorders:
		num = percentOdd()
		for key in dPhobias.keys():
			if num < key:
				lDisorders.remove('Phobia')
				lDisorders.append(dPhobias[key])
				break


	return lDisorders

dSex = {	'Gender':'NONE',
			'Sexuality': 'Unknown',
			'Polyamorous': False }

#[0.0 - Asexual - 1.05 - Homosexual - 2.25 - Pansexual - 20.35 - Heterosexual - 100.0]
#[        -1                 6      5      4      3     2      1      0              ]

dSexuality = { -1: "Asexual",
			    0: "Fully Heterosexual",
			    1: "Mostly Heterosexual",
			    2: "Hetero-Pansexual",
			    3: "Pansexual",
			    4: "Homo-Pansexual",
			    5: "Mostly Homosexual",
			    6: "Fully Homosexual" }

def genSex():
	#Sexuality
	iSexity = 0
	num = percentOdd()
	if (num < 1.05):
		iSexity = -1
	elif num < 2.25:
		iSexity = 6
	elif num < 20.35:
		iSexity = int(random()*5.0)+1
	else:
		iSexity = 0
	dSex['Sexuality'] = dSexuality[iSexity]

	#Polyamorous
	if percentOdd() < 13.0:
		dSex['Polyamorous'] = True

	#Gender
	if percentOdd() < 0.2:
		dSex['Gender'] = 'Trans'
	else:
		dSex['Gender'] = 'Cis'
	return dSex