class InitTracker:
    trackerInfo = []

    currentPlayer = 0
    rounds = 0

    def __init__(self):
        super().__init__()

    def printTracker(self):
        if self.trackerInfo == []:
            print("No combatants have joined initiative!")

            return "No combatants have joined initiative!"
        else:
            current = 0
            toPrint = ""
            toPrint = toPrint + "-----------------------------------\nCurrent Initiative: " + str(self.rounds) + "\n-----------------------------------"

            # print statements
            print("-----------------------------------")
            print("Current Initiative: " + str(self.rounds))
            print("-----------------------------------")

            for data in self.trackerInfo:
                if current == self.currentPlayer:
                    toPrint = toPrint + "\n**" + str(data[2]) + ": " + data[1] + "**"
                    
                    # print statements
                    print("**" + str(data[2]) + ": " + data[1] + "**")
                else:
                    toPrint = toPrint + "\n" + str(data[2]) + ": " + data[1]

                    # print statements
                    print(str(data[2]) + ": " + data[1])
                current = current + 1
            toPrint = toPrint + "\n-----------------------------------"

            # print statements
            print("-----------------------------------")

            return toPrint
    
    def join(self, username, name, initiative):
        for data in self.trackerInfo:
            if name == data[1]:
                # print statements
                print("That character already exists!")

                return "That character already exists!"
                break
        
        if self.currentPlayer != 0:
            # print statements
            print("Combat has already begun!")

            return "Combat has already begun!"
        
        else:
            try:
                initiative = int(initiative)
            except ValueError:
                print("Initiative must be an integer!")

                return "Initiative must be an integer!"

            # Add all relevant information to the array.
            self.trackerInfo.append([username, name, initiative])

            # print statements
            print("Combatant successfully joined!")

            return "Combatant successfully joined!"
    
    def begin(self):
        if self.currentPlayer != 0:
            # print statements
            print("Combat has already begun! User !end to clear the initiative tracker.")

            return "Combat has already begun! User !end to clear the initiative tracker."
        elif len(self.trackerInfo) < 2:
            # print statements
            print("At least two combatants required!")

            return "At least two combatants required!"
        else:
            self.sortTrackerInfo()
            self.rounds = 1
            return self.printTracker()
    
    def end(self):
        # Clear the initiative tracker information.
        self.trackerInfo.clear()
        # Reset currentPlayer and rounds.
        self.currentPlayer = 0
        self.rounds = 0

        return "Initiative tracker cleared!"

    def next(self):
        if self.currentPlayer == 0 and self.rounds == 0:
            # print statement
            print("Combat hasn't begun yet! Use !begin to begin combat.")

            return "Combat hasn't begun yet! Use !begin to begin combat."        
        elif self.currentPlayer + 1 == len(self.trackerInfo):
            self.currentPlayer = 0
            self.inc_round()
        else:
            self.currentPlayer = self.currentPlayer + 1
        return self.printTracker()
    
    def prev(self):
        if self.currentPlayer == 0 and self.rounds == 0:
            # print statement
            print("Combat hasn't begun yet! Use !begin to begin combat.")

            return "Combat hasn't begun yet! Use !begin to begin combat."
        elif self.currentPlayer == 0 and self.rounds == 1:
            # print statement
            print("You're at the beginning of combat already!")

            return "You're at the beginning of combat already!"
        elif self.currentPlayer - 1 == -1:
            self.currentPlayer = len(self.trackerInfo) - 1
            self.dec_round()
        else:
            self.currentPlayer = self.currentPlayer - 1
        return self.printTracker()
    
    def inc_round(self):
        self.rounds += 1
    
    def dec_round(self):
        if self.rounds - 1 == 0:
            self.rounds = 1
        else:
            self.rounds = self.rounds - 1

    def sortTrackerInfo(self):
        self.trackerInfo = sorted(self.trackerInfo, key = lambda x:x[2], reverse = True)