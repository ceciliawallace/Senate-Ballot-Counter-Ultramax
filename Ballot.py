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
        self.changeTopChoice = newTopChoice

    def popPreference(self):
        if self.preferences not empty:

        self.preferences.

