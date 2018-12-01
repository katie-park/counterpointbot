from random import choice, randint

# define variables that count previous repetition(s) of named interval
third = 0
fifth = 0
sixth = 0
octave = 0
# define variables that count previous instance(s) of named degrees
four = 0
seven = 0

def mode(modex,input):
    return {
        #3,5,6,8
        1 : [6,'TT',3,1] if modex == "lydian" else [6,4,3,1],
        2 : [7,'TT',4,2] if modex == "phrygian" else [7,5,4,2],
        3 : [1,'TT',5,3] if modex == "dorian" else [1,6,5,3],
        4 : [2,'TT',6,4] if modex == "ionian" else [2,7,6,4],
        5 : [3,'TT',7,5] if modex == "locrian" else [3,1,7,5],
        6 : [4,'TT',1,6] if modex == "aeolian" else [4,2,1,6],
        7 : [5,'TT',2,7] if modex == "mixolydian" else [5,3,2,7]
            }.get(input, ':(')

def first_species(mode):
    global third, fifth, sixth, octave, four, seven

    result = 0
    options = choice(mode)
    
    if third == 3:
        options = choice([mode[1],mode[2],mode[3]])
        result = options
        third = 0
    elif fifth == 1:
        options = choice([mode[0],mode[2],mode[3]])
        result = options
        fifth = 0
    elif sixth == 3:
        options = choice([mode[0],mode[1],mode[3]])
        result = options
        sixth = 0
    elif octave == 1:
        options = choice([mode[0],mode[1],mode[2]])
        result = options
        octave = 0
    else:
        result = options
    #to-do: fix TT logic
    if four == 1:
        while result == 7:
            result = options
        four = 0
    elif seven == 1:
        while result == 4:
            result = options
        seven = 0
    if result == 'TT':
        if third == 3:
            result == choice([mode[2],mode[3]])
            third == 0
        elif sixth == 3:
            result == choice([mode[0],mode[3]])
            sixth == 0
        elif octave == 1:
            result == choice([mode[0],mode[2]])
            octave == 0
        else:
            result == choice([mode[0],mode[2],mode[3]])
    
    if result == 4:
        four += 1
    elif result == 7:
        seven += 1
    elif result == 1:
        result == choice([1,8])
    
    if result == mode[0]:
        third += 1
        #interval.append(3)
    elif result == mode[1]:
        fifth += 1
        #interval.append(5)
    elif result == mode[2]:
        sixth += 1
        #interval.append(6)
    elif result == mode[3]:
        octave += 1
        #interval.append(8)
    else:
        return "X"
    return result

def gen_counterpoint(cantus_firmus):
    global third, fifth, sixth, octave, four, seven

    third = 0
    fifth = 0
    sixth = 0
    octave = 0
    four = 0
    seven = 0
    
    counterpoint = []
    counterpoint.append(mode(modex,cantus_firmus[0])[3]) # use tonic for first note in counterpoint

    for i in cantus_firmus[1:len(cantus_firmus)-3]:
        counterpoint.append(first_species(mode(modex,i)))
    
    counterpoint.append(mode(modex,cantus_firmus[len(cantus_firmus)-3])[0])
    counterpoint.append(mode(modex,cantus_firmus[len(cantus_firmus)-2])[1])
    counterpoint.append(mode(modex,cantus_firmus[len(cantus_firmus)-1])[3])
    return counterpoint

modex = "ionian"

cantus_firmus = [3,2,1,2,3,3,3,2,2,2,3,5,5,3,2,1,2,3,3,3,3,2,2,3,2,1]

def cantus_firmus_list(cantus_firmus):
    cantus_firmus = map(int,cantus_firmus.split( ))
    return cantus_firmus

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

counterpoint = gen_counterpoint(cantus_firmus)

print(' '.join([str(i) for i in cantus_firmus]))
print(' '.join([str(i) for i in counterpoint]))
print()
print(' '.join([CM(i) for i in cantus_firmus]))
print(' '.join([CM(i) for i in counterpoint]))

