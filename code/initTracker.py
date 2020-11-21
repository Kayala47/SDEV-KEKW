class InitTracker:
    trackerInfo = []

    currentPlayer = 0
    rounds = 0
    channel = None

    def __init__(self, channel):
        super().__init__()
        self.channel = channel

    def printTracker(self):
        if self.trackerInfo == []:
            self.channel.send("No combatants have joined initiative!")
        else:
            current = 0
            self.channel.send("-----------------------------------")
            self.channel.send("Current Initiative:" + str(rounds))
            self.channel.send("-----------------------------------")
            for data in self.trackerInfo:
                if current == self.currentPlayer:
                    self.channel.send("**" + str(data[2]) + ": " + data[1] + "**")
                else:
                    self.channel.send(str(data[2]) + ": " + data[1])
                current = current + 1
            self.channel.send("-----------------------------------")
    
    def join(self, username, name, initiative):
        for data in self.trackerInfo:
            if name == data[1]:
                self.channel.send("That character already exists!")
                break
        
        if self.currentPlayer != 0:
            self.channel.send("Combat has already begun!")
        else:
            # Add all relevant information to the arrays.
            self.trackerInfo.append([username, name, initiative])
            # Sort tracker information.
            self.sortTrackerInfo()
    
    def begin(self):
        if self.currentPlayer != 0:
            self.channel.send("Combat has already begun!")
        else:
            self.printTracker()
            # return self.usernames(currentPlayer)
    
    def end(self):
        # Clear the initiative tracker information.
        self.trackerInfo.clear()
        # Reset currentPlayer and rounds.
        self.currentPlayer = 0
        self.rounds = 0

    def next(self):
        if self.currentPlayer + 1 == len(self.trackerInfo):
            self.currentPlayer = 0
            self.inc_round()
        else:
            self.currentPlayer = self.currentPlayer + 1
        self.printTracker()
    
    def prev(self):
        if self.currentPlayer - 1 == -1:
            self.currentPlayer = len(self.trackerInfo) - 1
            self.dec_round()
        else:
            self.currentPlayer = self.currentPlayer - 1
        self.printTracker()
    
    def inc_round(self):
        rounds += 1
    
    def dec_round(self):
        if rounds - 1 == 0:
            rounds = 1
        else:
            rounds = rounds - 1

    def sortTrackerInfo(self):
        self.trackerInfo = sorted(self.trackerInfo, key = lambda x:x[2], reverse = True)

i = InitTracker()

i.join("@dana", "Scarlett", 17)
i.join("@swam", "Blobfish", 1)
i.join("@raf", "Meoung", 20)

i.begin()
i.end()
i.printTracker()
i.end()
i.printTracker()