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
