class InitTracker:
    trackerInfo = []

    currentPlayer = 0
    rounds = 0

    def __init__(self):
        super().__init__()

    def printTracker(self):
        ''' Prints the current initiative tracker information.
            Inputs:     None
            Outputs:    None '''

        if self.trackerInfo == []:
            return "No combatants have joined initiative!"
        else:
            self.sortTrackerInfo()

            current = 0
            toPrint = "-----------------------------------"
            toPrint = toPrint + "\nCurrent Round: " + str(self.rounds)
            toPrint = toPrint + "\n-----------------------------------"

            # Loop through trackerInfo and append info to output string accordingly.
            for data in self.trackerInfo:
                # Current player information is bolded.
                if current == self.currentPlayer:
                    toPrint = toPrint + "\n**" + str(data[2]) + ": " + data[1] + "**" 
                else:
                    toPrint = toPrint + "\n" + str(data[2]) + ": " + data[1]

                current = current + 1

            toPrint = toPrint + "\n-----------------------------------"

            return toPrint
    
    def join(self, username, name, initiative):
        ''' Adds new combatant's information into trackerInfo.
            This includes username, name, and initiative roll.
            Inputs:     username - username of player that added the combatant
                        name - name of new combatant
                        initiative - initiative roll result
            Outputs:    string indicating error or success '''

        for data in self.trackerInfo:
            if name == data[1]:
                return "That character already exists!"
        
        if self.rounds != 0:
            return "Combat has already begun!"        
        else:
            # Ensure initiative roll can be interpreted as int.
            try:
                initiative = int(initiative)
            except ValueError:
                return "Initiative must be an integer!"

            # Add all relevant information to the array.
            self.trackerInfo.append([username, name, initiative])

            return "Combatant successfully joined!"
    
    def begin(self):
        ''' Begins initiative and prints current initiative order.
            Inputs:     None
            Outputs:    string indicating error or success '''

        if self.rounds != 0:
            return "Combat has already begun! Use !end to clear the initiative tracker."
        elif len(self.trackerInfo) < 2:
            return "At least two combatants required!"
        else:
            self.rounds = 1
            self.currentPlayer = 0

            return self.printTracker()
    
    def end(self):
        ''' Ends initiative and clears all information in trackerInfo.
            Inputs:     None
            Outputs:    None '''

        # Clear the initiative tracker information.
        self.trackerInfo.clear()
        # Reset currentPlayer and rounds.
        self.currentPlayer = 0
        self.rounds = 0

        if len(self.trackerInfo) != 0:
            return "Unable to clear initiative tracker."

        return "Initiative tracker cleared!"

    def next(self):
        ''' Moves to the next combatant in initiative.
            Inputs:     None
            Outputs:    None '''

        if self.rounds == 0:
            return "Combat hasn't begun yet! Use !begin to begin combat."  
        # Loop around initiative accordingly.
        elif self.currentPlayer + 1 == len(self.trackerInfo):
            self.currentPlayer = 0
            self.inc_round()
        else:
            self.currentPlayer = self.currentPlayer + 1

        return self.printTracker()
    
    def prev(self):
        ''' Moves to the previous combatant in initiative.
            Inputs:     None
            Outputs:    None '''

        if self.rounds == 0:
            return "Combat hasn't begun yet! Use !begin to begin combat."
        # Don't go past currentPlayer = 0, rounds = 1.
        elif self.currentPlayer == 0 and self.rounds == 1:
            return "You're at the beginning of combat already!"
        # Loop around initiative accordingly.
        elif self.currentPlayer - 1 == -1:
            self.currentPlayer = len(self.trackerInfo) - 1
            self.dec_round()
        else:
            self.currentPlayer = self.currentPlayer - 1

        return self.printTracker()
    
    def inc_round(self):
        ''' Increments round.
            Inputs:     None
            Outputs:    None '''

        self.rounds += 1
    
    def dec_round(self):
        ''' Decrements round.
            Inputs:     None
            Outputs:    None '''

        if self.rounds - 1 == 0:
            self.rounds = 1
        else:
            self.rounds = self.rounds - 1

    def sortTrackerInfo(self):
        ''' Sorts trackerInfo by initiative roll in descending order.
            Inputs:     None
            Outputs:    None '''
            
        self.trackerInfo = sorted(self.trackerInfo, key = lambda x:x[2], reverse = True)