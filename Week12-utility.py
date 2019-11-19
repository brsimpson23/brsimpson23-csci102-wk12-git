# Brian Simpson
# CSCI 102 - Section A
# Week 12 - Part A


def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file):
    with open(file, 'r') as text:
        output = []
        for line in text:
            output.append(line)
    return output

def UpdateString(modify, char, index):
    modified = modify[:index] + char + modify[(index + 1):]
    print('OUTPUT', modified)
    
def FindWordCount(lista, string):
    counts = 0
    for value in lista:
        counts += value.count(string)
    return counts

def ScoreFinder(names, scores, player):
    namesu = []
    playeru = player.lower()
    for value in names:
        namesu.append(value.lower())
    cont = namesu.count(player)
    if cont == 0:
        print('OUTPUT player not found')
    else:
        ind = namesu.index(playeru)
        print('OUTPUT %s got a score of %d' % (player, scores[ind]))
    
def Union(lista, listb):
    listc = lista + listb
    return listc
