from random import choice

def listRandomizer(inputedList):
    randomizedList = []
    while len(inputedList)>0:
        choosen_one = choice(inputedList)
        randomizedList.append(choosen_one)
        inputedList.remove(choosen_one)
    return randomizedList

while True:
    with open("inputedList.txt","r") as f:
        inputedList = f.read().splitlines()

    menuInput = input('Enter command [!quit, !drawteam, !see, !fast]: ')

    if menuInput == "!quit": # Closes the app
        break
    elif menuInput == "!drawteam": # Divides members into teams of n
        teamLimit = int(input("Team limit: "))
        randomedList = listRandomizer(inputedList)
        while len(randomedList)>0:
            try:
                first_n_members = randomedList[:teamLimit]
                print(first_n_members)
                for i in first_n_members:
                    randomedList.remove(i)
            except:
                teamLimit -= 1        
    elif menuInput == "!see": # Shows all members
        print(inputedList)
    elif menuInput == "!fast": # Quickly splits members into 2 teams
        randomedList = listRandomizer(inputedList)
        print("Team 1: " + str(randomedList[:int(len(randomedList)/2)]))
        print("Team 2: " + str(randomedList[int(len(randomedList)/2):]))
    else:
        pass
