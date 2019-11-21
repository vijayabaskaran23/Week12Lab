# https://github.com/vijayabaskaran23/Week12Lab.git
#Ethan Vijayabaskaran
#CSCI 102 - Section E
#Lab 12 - Part A
def PrintOutput(output):
    out = 'OUTPUT ' + str(output)
    print(out)
def LoadFile(file):
    name = open(file,'r')
    f = name.read()
    mylist = []
    mylist = f.splitlines()
    return mylist
def UpdateString(str_1,str_2,index):
    str_1 = list(str_1)
    new_list = []
    for x in range(len(str_1)):
        if x == index:
            new_list.append(str_2)
        else:
            new_list.append(str_1[x])
    print ('OUTPUT', ''.join(new_list))
def FindWordCount(input_list,input_string):
    count=0
    for x in input_list:
        if x == input_string:
            count += 1
    return count
def ScoreFinder(player_names,player_scores,player_to_find):
    score_index = 0
    cap = player_to_find.capitalize()
    #player_to_find = player_to_find.capitalize()
    if cap in player_names:
        name_index = player_names.index(cap)
        score_index = player_scores[name_index]
        print('OUTPUT',player_to_find, "got a score of",score_index)
    else:
        word = 'OUTPUT Player not found'
        print(word)
def Union(list_1,list_2):
    new_list = []
    new_list = list_1 + list_2
    return new_list
def Intersection(list_1,list_2):
    new_list = []
    for x in list_1:
        if x in list_2:
            new_list.append(x)
    return new_list
