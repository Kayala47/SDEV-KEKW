class InitTracker:
    usernames = []
    names = []
    initiatives = []
    numCombatants = 0
    currentPlayer = 0
    rounds = 0

    def __init__(self):
        super().__init__()

    def printTracker(self):
        for i in range(numCombatants):
            print(i + ": " + names[i] + ", " + initiatives[i])
    
    def join(self, username, name, initiative):
        usernames.append(username)
        names.append(name)
        initiatives.append(initiative)
        numCombatants += 1
    
    def begin(self):
        printTracker()
        return usernames(currentPlayer)
