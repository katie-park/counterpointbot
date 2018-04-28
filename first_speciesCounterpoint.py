from random import choice, randint

print "COUNTERPOINT BOT"
print "Input cantus firmus as scale degrees numbers, eg. 3 2 1 2 3 5 ..."

test = raw_input("Test sample song? (y/n) ")

if test == 'y':
    cantus_firmus = "3 2 1 2 3 3 3 2 2 2 3 5 5 3 2 1 2 3 3 3 3 2 2 3 2 1"
else:
    cantus_firmus = raw_input('Cantus firmus: ')

if len(cantus_firmus) == 0:
    print 'error: no input'
else:
    cantus_firmus_list = map(int,cantus_firmus.split( ))
print cantus_firmus_list

#to-do: optimize modes
def ionian(input):
    return {
            #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,5,4,2],
        3 : [1,6,5,3],
        4 : [2,'TT',6,4],
        5 : [3,1,7,5],
        6 : [4,2,1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def dorian(input):
    return {
        #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,5,4,2],
        3 : [1,'TT',5,3],
        4 : [2,7,6,4],
        5 : [3,1,7,5],
        6 : [4,2,1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def phrygian(input):
    return {
        #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,'TT',4,2],
        3 : [1,6,5,3],
        4 : [2,7,6,4],
        5 : [3,1,7,5],
        6 : [4,2,1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def lydian(input):
    return {
        #3,5,6,8
        1 : [6,'TT',3,1],
        2 : [7,5,4,2],
        3 : [1,6,5,3],
        4 : [2,7,6,4],
        5 : [3,1,7,5],
        6 : [4,2,1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def mixolydian(input):
    return {
        #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,5,4,2],
        3 : [1,6,5,3],
        4 : [2,7,6,4],
        5 : [3,1,7,5],
        6 : [4,2,1,6],
        7 : [5,'TT',2,7]
            }.get(input, ':(')

def aolian(input):
    return {
        #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,5,4,2],
        3 : [1,6,5,3],
        4 : [2,7,6,4],
        5 : [3,1,7,5],
        6 : [4,'TT',1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def locrian(input):
    return {
        #3,5,6,8
        1 : [6,4,3,1],
        2 : [7,5,4,2],
        3 : [1,6,5,3],
        4 : [2,7,6,4],
        5 : [3,'TT',7,5],
        6 : [4,2,1,6],
        7 : [5,3,2,7]
            }.get(input, ':(')

def firstSpecies(mode,third,four,fifth,sixth,seven,octave):
    result = 0
    
    if third == 3:
        result = choice([mode[1],mode[2],mode[3]])
        third = 0
    elif fifth == 1:
        result = choice([mode[0],mode[2],mode[3]])
        fifth == 0
    elif sixth == 3:
        result = choice([mode[0],mode[1],mode[3]])
        sixth = 0
    elif octave == 1:
        result = choice([mode[0],mode[1],mode[2]])
        octave == 0
    else:
        result = choice(mode)
    #to-do: fix TT logic
    if four == 1:
        if result == 7:
            result == '>:('
        four = 0
    if seven == 1:
        if result == 4:
            result == '>:('
        seven = 0
    if result == 'TT':
        if third == 3:
            result == choice([mode[2],mode[3]])
            third == 0
        elif sixth == 3:
            result == choice([mode[0],mode[3]])
            sixth == 0
        elif octave == 1:
            result == choice([mode[0],mode[2],])
            octave == 0
        else:
            result == choice([mode[0],mode[2],mode[3]])

    if result == mode[0]:
        third += 1
    elif result == 4:
        four += 1
    elif result == 7:
        seven += 1
    elif result == mode[1]:
        fifth += 1
    elif result == mode[2]:
        sixth += 1
    elif result == mode[3]:
        octave += 1
    else:
        print ":("
    return result

counterpoint = []

third = 0
fifth = 0
sixth = 0
four = 0
seven = 0

#start with octave
counterpoint.append(ionian(cantus_firmus_list[0])[3])
octave = 1

if len(cantus_firmus_list) >= 4:
    for i in cantus_firmus_list[1:len(cantus_firmus_list)-3]:
        counterpoint.append(firstSpecies(ionian(i),third,four,fifth,sixth,seven,octave))
    #to-do:  ban all the 3s
    counterpoint.append(ionian(cantus_firmus_list[len(cantus_firmus_list)-3])[0])
    counterpoint.append(ionian(cantus_firmus_list[len(cantus_firmus_list)-2])[1])
    counterpoint.append(ionian(cantus_firmus_list[len(cantus_firmus_list)-1])[3])
else:
    #to-do: fill in parameters
    print "too short"
def CM(input):
    return {
        1 : 'C',
        2 : 'D',
        3 : 'E',
        4 : 'F',
        5 : 'G',
        6 : 'A',
        7 : 'B'
            }.get(input, ':(')

askCM = raw_input("Write in C Major? (y/n): ")
if askCM == 'y':
    counterpointinC = []
    for i in counterpoint:
        counterpointinC.append(CM(i))
    print counterpointinC
else:
    print counterpoint