#Character generator project
#Central generation file

from generation import *

vPersonality = personality.gen()
lPersonalityDisorder = personality.genDisorder()
dPersonalitySex = personality.genSex()

vBody = body.gen()

vBackground = background.gen()

print("Age: ", vBody['Age'])
print("Height: ", vBody['Height'], "cm", "\tWeight: ", vBody['Weight'], "lbs.")
print("Religion: ", vBackground['Religion'])
print("Ancestry: ")
for ancestor in vBackground['Ancestry']:
	print("\t", ancestor)

print("\nSex: ", vBody['Sex'], "\tGender: ", dPersonalitySex['Gender'])
print(dPersonalitySex['Sexuality'], "Polyamorous" if dPersonalitySex['Polyamorous'] else "")

print("\nPersonality: ", ', '.join(vPersonality).capitalize())
if len(lPersonalityDisorder) > 0:
	print("\nPersonality disorders:")
	for disorder in lPersonalityDisorder:
		print("\t", disorder)