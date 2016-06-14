#! python3
import random
from random import randint
from rolltables import *

# This is the random choice initializer functions

def main():
    charRace = random_choice(raceTable101)
    if charRace == 'other races':
        charRace = random_choice(raceTable101a)
    charCulture = random_choice(cultureTable102)
    cuMod = cultureTable102a(charCulture)
    tiMod = 0
    global charSocial
    global charAdopted
    global solMod
    charAdopted = False
    charSocial, solMod, nobleTitle, tiMod = socialTable103(cuMod, tiMod, charCulture)
    legitBirth = birthTable104(cuMod)
    if legitBirth == False:
        if cuMod >= 0:
            cuMod = cuMod - randint(1,4)
        illegitReason = illegitBirthTable105(cuMod)
        illegitBirth = 'Birth was illegitimate. Cause: ' + illegitReason + '.'
    charFamily, charAdopted = familyTable106(cuMod)
    if charAdopted == True:
        charFamily = '(adopted) ' + str(charFamily)
    print('Race: ' + charRace + ' | Culture: ' + charCulture + ' | Social Standing: ' + charSocial + ((' | Title: ', "")[nobleTitle == ""]) + nobleTitle + "\nFamily: " + str(charFamily) + '.')
    siblingMale, siblingFemale, birthOrder = siblingsTable107()
    if siblingMale == 'none':
        print('Siblings: None')
    else:
        print('Siblings: ' + str(siblingMale) + ' male' + (('s', '')[siblingMale == 1]) + ' and ' + str(siblingFemale) + ' female' + (('s', '')[siblingFemale == 1]) + ', of which the character is the ' + birthOrder + '.')
    birthSeason, birthTimeOfDay = birthTimeTable109()
    placeOfBirth, biMod = placeOfBirthTable110()
    print('Birth: In ' + birthSeason + ' at ' + birthTimeOfDay + ' ' + placeOfBirth + '.')
    birthOccurance, unusualBirth = unusualBirthTable112(biMod)
    if unusualBirth == True:
        birthOccurance = ", ".join(birthOccurance)
        print('Birth Circumstances: ' + birthOccurance.capitalize())
    if legitBirth == False: #this needs to be after birth occurances because it fits better, thematically
        print(illegitBirth)
    #shit about parents go hurr
    hohOccupation = parentTable114a(charCulture, solMod)
    print('Parents Info: ' + hohOccupation)
    childhoodEvents, adolescentEvents = childhoodEventsTable215a(solMod)
    childhoodEvents = capitalize_shit(childhoodEvents)
    adolescentEvents = capitalize_shit(adolescentEvents)
    childhoodEvents = " | ".join(childhoodEvents)
    adolescentEvents = " | ".join(adolescentEvents)
    print('Childhood: ' + childhoodEvents + "\nAdolescence: " + adolescentEvents)
    adulthoodEvents = adulthoodSignificantEventsTable217(charSocial, solMod)
    adulthoodEvents = capitalize_shit(adulthoodEvents)
    adulthoodEvents = " | ".join(adulthoodEvents)
    print('Adulthood: ' + adulthoodEvents )

def capitalize_shit(array): #I don't feel like re-writing everything from lower-case in the rolltables, so fuck it. Here.
    for i in range(len(array)):
        array[i] = array[i].capitalize()
    return array

def random_choice_index(chances):
	dice = randint(1, sum(chances))
	running_sum = 0
	choice = 0
	for w in chances:
		running_sum += w
		if dice <= running_sum:
			return choice
		choice += 1

def random_choice(chances_dict):
	chances = chances_dict.values()
	strings = list(chances_dict.keys())
	return strings[random_choice_index(chances)]

if __name__ == "__main__":
    main()
