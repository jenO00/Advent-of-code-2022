def readFile():
    #read the file
    lines = []
    with open('day3.txt') as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def rucksack():
    bags = readFile()
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    curr = 1
    saved = []
    #these above work
    for bag in bags:
        found = False
        half = len(bag)//2
        first = bag[:half]
        second = bag[half:]
       # print("Bag: ", bag, "first: ", first, "second: ", second)
        found = 0
        for letter in first:
            if letter in second:
                if found == 0:
                    saved.append(letter)
                    found = 1
        res = 0
    print(saved)
    for i in saved:
        if i in lowercase:
            index = lowercase.index(i)
            res+=index+1
        if i in uppercase:
            index=uppercase.index(i)
            res+=index+27
                    
    return res


def partTwo():
    #first, sort them into three
    bags = readFile()
    res = 0
    curr = 0
    currBag = []
    finalBags = []
    foundCommons = []
    for bag in bags:
        if curr == 3:
            finalBags.append(currBag)
            #reset
            curr=0
            currBag = [] 
        else:
            currBag.append(bag)
            curr+=1
            if curr==3:
                finalBags.append(currBag)
                curr=0
                currBag=[]
    #initiate the priority
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for bag in finalBags:
        found = 0
        for curr in bag:
            for letter in curr:
               # print("Current letter :", letter)
                if found == 0:
                    if letter in bag[1] and letter in bag[2]:
                        #found one
                        foundCommons.append(letter)
                        found = 1
    for i in foundCommons:
        if i in lowercase:
            index = lowercase.index(i)
            res+=index+1
        if i in uppercase:
            index=uppercase.index(i)
            res+=index+27
    return res

