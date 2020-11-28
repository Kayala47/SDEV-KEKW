class InitTracker:
    trackerInfo = []

    currentPlayer = 0
    rounds = 0

    def __init__(self):
        super().__init__()

    def printTracker(self):
        print("--------------")
        print("| INITIATIVE |")
        print("--------------")
        if self.trackerInfo == []:
            print("")
        else:
            for data in self.trackerInfo:
                print(str(data[2]) + ": " + data[1])
        print("--------------")
    
    def join(self, username, name, initiative):
        for data in self.trackerInfo:
            if name == data[1]:
                print("That character already exists!")
                break
        
        if self.currentPlayer != 0:
            print("Combat has already begun!")
        else:
            # Add all relevant information to the arrays.
            self.trackerInfo.append([username, name, initiative])
            # Sort tracker information.
            self.sortTrackerInfo()
    
    def begin(self):
        if self.currentPlayer != 0:
            print("Combat has already begun!")
        else:
            self.printTracker()
            # return self.usernames(currentPlayer)
    
    def end(self):
        # Clear the initiative tracker information.
        self.trackerInfo.clear()
        # Reset currentPlayer and rounds.
        self.currentPlayer = 0
        self.rounds = 0

    def sortTrackerInfo(self):
        self.trackerInfo = sorted(self.trackerInfo, key = lambda x:x[2], reverse = True)
