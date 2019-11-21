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
