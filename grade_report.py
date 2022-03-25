#   Sarpas, Rahim

infile1 = open("classes.txt", "r")
infile2 = open("CSC1.txt", "r")
infile3 = open("CSC2.txt", "r")
infile4 = open("MATH121.txt", "r")

ids = []
csc1 = []
csc2 = []
math = []

def input1(list, infile):
    while (True):
        line = infile.readline()
        line = line.split()
        if (len(line) == 0):
            break
        list.append(line[1])

def input2(list, list2, infile):
    while (True):
        line = infile.readline()
        line = line.split()
        if (len(line) == 0):
            break
        list.append(line[0])
        list2.append(line[1])

input2(ids, csc1, infile2)
input1(csc2, infile3)
input1(math, infile4)

def findIDIndex(givenID, list):
    givenID = str(givenID)
    if (ids.count(givenID) == 1):
        idx = ids.index(givenID)
        return idx
    else:
        return 0

givenID = int(input("Enter the student id: "))
print("Student ID", givenID)
print("CSC1", csc1[findIDIndex(givenID, ids)])
print("CSC2", csc2[findIDIndex(givenID, ids)])
print("MTH121", math[findIDIndex(givenID, ids)])

infile1.close()
infile2.close()
infile3.close()
infile4.close()