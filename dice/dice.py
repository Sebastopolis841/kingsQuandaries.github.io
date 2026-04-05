from random import randint

dUsed = False
commaUsed = False
dieAmount = ""
dieValue = ""
string = "\n"
total = 0

dice = input("Choose dice to roll (comma for different dice to roll, 2 commas for a seperate group of dice.)  ")

dice = dice.replace(" ", "").lower()

def addNumbers():
    global total
    for i in range(int(dieAmount)):
        total += randint(1,int(dieValue))

def makeString():
    global string
    global total
    
    string += (str(total) + "\n\n")

    total = 0

for i in range (0, len(dice)):
    if not commaUsed:
        if dice[i] == "d":
            dUsed = True
            commaUsed = False

        elif dice[i] == ",":
            addNumbers()

            commaUsed = True
            dUsed = False
            dieAmount = ""
            dieValue = ""

        else:
            if not dUsed:
                dieAmount += dice[i]
                commaUsed = False

            else:
                dieValue += dice[i]
                commaUsed = False

    else: # If a comma was used previously
        if dice[i] == "d":
            dUsed = True
            commaUsed = False

        elif dice[i] == ",":
            commaUsed = False
            dUsed = False
            dieAmount = ""

            makeString()

        else:
            if not dUsed:
                dieAmount += dice[i]
                commaUsed = False

            else:
                dieValue += dice[i]
                commaUsed = False

else:
    addNumbers()
    makeString()
    print(string)