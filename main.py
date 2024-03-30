from random import choice

# Shuffle the list.
def listRandomizer(inputedList):
    randomizedList = []
    # Chooses a member from inputedList, adds it to randomizedList and deletes it from inputedList. Until inputedList is completely empty.
    while len(inputedList)>0:
        choosen_one = choice(inputedList)
        randomizedList.append(choosen_one)
        inputedList.remove(choosen_one)
    return randomizedList

while True:
    # Gets list from inputedList.txt (After each command, so that you can always use !see)
    with open("inputedList.txt","r", encoding="utf-8") as f:
        inputedList = f.read().splitlines()

    # Menu Input
    menuInput = input('Enter command [!quit, !drawteam, !see, !fast]: ')

    # Closes the app
    if menuInput == "!quit":
        break
    # Divides members into teams of n // Takes the teamLimit as input, randomizes the list, while there is still members in list,
    # takes the first n members, prints them, removes them. Does it until there are no members in list. If it can't take the first
    # n members of list, decrase the teamLimit by one so that the remaining members can create a team between them.
    elif menuInput == "!drawteam":
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
    # Shows all members        
    elif menuInput == "!see":
        print(inputedList)
     # Quickly splits members into 2 teams
    elif menuInput == "!fast":
        randomedList = listRandomizer(inputedList)
        print("Team 1: " + str(randomedList[:int(len(randomedList)/2)]))
        print("Team 2: " + str(randomedList[int(len(randomedList)/2):]))
    else:
        pass
