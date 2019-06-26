'''
This is the Ballot class.
This contains the information for each Ballot - which includes:
    - preferences, a stack (Python list treated as a stack) containing a person's preferences
    - topChoice, a string of the ballot's current first element
    - TNumber
    - timeStamp, a record of the time the ballot was submitted
Each Ballot which is read in from a spreadsheet that is generated from a Google Form.
'''

class Ballot:
    def __init__(self, timeStamp, tNumber):
        self.timeStamp = timeStamp
        self.tNumber = tNumber
        self.preferences = [] # this will contain prefered candidates in order (first pref to last)
        self.topChoice = ""

    def changeTopChoice(self, newTopChoice):
        self.topChoice = newTopChoice

    def popPreference(self):
        if len(self.preferences) != 0:
            newTopChoice = self.preferences.pop(0) #pop the 0th index off of our preference list
            changeTopChoice(newTopChoice)

            if len(self.preferences) == 0:
                return False #ok so if we empty list return False??
            else:
                return True

        else:
            "tried to remove pref from empty list"

    def addPreference(self, candidateName):
        self.preferences.append(candidateName)