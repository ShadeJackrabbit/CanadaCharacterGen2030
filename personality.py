# coding=utf-8

#Character generator project
#This chooses a personality type and can also describe each type

from random import random
from numpy import log

sISTJ = "Quiet, serious, earn success by thoroughness and dependability. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized – their work, their home, their life. Value traditions and loyalty."
sISFJ = "Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home."
sINFJ = "Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision."
sINTJ = "Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance – for themselves and others."
sISTP = "Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency."
sISFP = "Quiet, friendly, sensitive, and kind. Enjoy the present moment, what’s going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts, do not force their opinions or values on others."
sINFP = "Idealistic, loyal to their values and to people who are important to them. Want an external life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened."
sINTP = "Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical."
sESTP = "Flexible and tolerant, they take a pragmatic approach focused on immediate results. Theories and conceptual explanations bore them – they want to act energetically to solve the problem. Focus on the here-and-now, spontaneous, enjoy each moment that they can be active with others. Enjoy material comforts and style. Learn best through doing."
sESFP = "Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work, and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people."
sENFP = "Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency."
sENTP = "Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another."
sESTJ = "Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans."
sESFJ = "Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-by-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute."
sENFJ = "Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership."
sENTJ = "Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas."

dPersonality = { 'ISTJ':sISTJ, 'ISFJ':sISFJ, 'INFJ':sINFJ, 'INTJ':sINTJ, 'ISTP':sISTP, 'ISFP':sISFP, 'INFP':sINFP, 'INTP':sINTP, 'ESTP':sESTP, 'ESFP':sESFP, 'ESFP':sESFP, 'ENFP':sENFP, 'ENTP':sENTP, 'ESTJ':sESTJ, 'ESFJ':sESFJ, 'ENFJ':sENFJ, 'ENTJ':sENTJ }

lPersonality = list(dPersonality.keys())

percentOdd = lambda: random()*100.0

def gen():
	num = min(int(random()*16.0), 15)
	return lPersonality[num]

def desc(acronym):
	return dPersonality[acronym.upper()]

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
			'Sexuality': -1,
			'Polyamorous': False }

#[0.0 - Asexual - 1.05 - Homosexual - 2.25 - Pansexual - 20.35 - Heterosexual - 100.0]
#[        -1                 6      5      4      3     2      1      0              ]

def genSex():
	#Sexuality
	num = percentOdd()
	if (num < 1.05):
		dSex['Sexuality'] = -1
	elif num < 2.25:
		dSex['Sexuality'] = 6
	elif num < 20.35:
		dSex['Sexuality'] = int(random()*5.0)+1
	else:
		dSex['Sexuality'] = 0

	#Polyamorous
	if percentOdd() < 13.0:
		dSex['Polyamorous'] = True

	#Gender
	if percentOdd() < 0.2:
		dSex['Gender'] = 'Trans'
	else:
		dSex['Gender'] = 'Cis'
	return dSex