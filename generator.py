#Character generator project
#Central generation file

import personality

vPersonality = personality.gen()
lPersonalityDisorder = personality.genDisorder()
dPersonalitySex = personality.genSex()

print("Personality Type: ", vPersonality, "-", personality.desc(vPersonality))
print("Personality Disorders: ", lPersonalityDisorder)
print("Sexuality Dynamics: ", dPersonalitySex)

import body

vBody = body.gen()

print(vBody)

import background

vBackground = background.gen(vBody['Sex'])

print(vBackground)