class InitTracker:
    usernames = []
    names = []
    initiatives = []
    currentPlayer = 0
    rounds = 0

    def __init__(self):
        super().__init__()

    def printTracker(self):
        for i in len(usernames):
            print(i + ": " + names[i] + ", " + initiatives[i])
    
    def join(self, username, name, initiative):
        usernames.append(username)
        names.append(name)
        initiatives.append(initiative)
    
    def begin(self):
        printTracker()
        return usernames(currentPlayer)
