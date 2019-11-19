# https://github.com/brsimpson23/brsimpson23-csci102-wk12-git.git
# Brian Simpson
# CSCI 102 - Section A
# Week 12 - Part A


def PrintOutput(string):
    print('OUTPUT', string)

def LoadFile(file):
    with open(file, 'r') as text:
        output = []
        for line in text:
            output.append(line[:-1])
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

def Intersection(lista, listb):
    listc = []
    for value in lista:
        cont = listb.count(value)
        if cont > 0:
            listc.append(value)
        else:
            continue
    return listc

def NotIn(lista, listb):
    listc = []
    for value in lista:
        cont = listb.count(value)
        if cont > 0:
            continue
        else:
            listc.append(value)
    return listc


