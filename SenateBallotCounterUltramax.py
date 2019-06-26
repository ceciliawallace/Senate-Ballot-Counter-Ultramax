'''
This is the main doc.
'''
import sys
import Ballot

#Spreadsheet should be formatted as:
#column1=timestamp, column2=Tnumber; all following columns are preferences
#converts spreadsheet into objects
#returns number of votes cast
#FILE MUST BE A CSV
def intakeSpreadsheet(filename):
    allBallots = []
    with open(filename, 'r') as f:
        readCSV = csv.reader(f, delimiter=',')
        next(readCSV)
        for row in readCSV:
            #make a new ballot object
            timeStamp = row[0] #TimeStamp is always the first column
            tNumber = row[1] #TNumber should always be the second column in the spreadsheet
            currentBallot = Ballot.Ballot(timeStamp, tNumber)
            #if the preference is empty, will be empty string
            preferences = []
            for column in row[2:]:
                if column.strip() != '':
                    preferences.append(column)
            currentBallot.changeTopChoice(preferences[0])
            currentBallot.preferences = preferences
            allBallots.append(currentBallot)

    return allBallots

def checkDoubleBallots(allBallots):
    for i in allBallots:
        for j in allBallots:
            if i.tNumber == j.tNumber:
                allBallots.remove(i) #will this actually remove the first ballot submitted? could throw error

def calculateThreshold(numSeats, threshold):
    numVotes = len(allBallots)
    calcThreshold = numVotes / numSeats
    threshold = int(calcThreshold)

def findSurplus():
    for candidate in scoreCard:
        if scoreCard[candidate] >= threshold:
            numToRedistribute = scoreCard[candidate] - threshold

def redistributeSurplus(candidateName, numToRedistribute, allBallots):
    counter = 0
    for ballot in allBallots:
        if counter < numToRedistribute:
            if ballot.preferences[0] == candidateName: #we wanna redistribute these ballots
                ballot.popPreference()
                counter += 1
        else:
            return #when we finally hit the number to redistribute, we wanna return

def findEliminated():

def redistributeEliminated(candidateName, allBallots):
    for ballot in allBallots:
        if ballot.preferences[0] == candidateName: #we wanna redistribute these ballots, what will happen if null??
            ballot.popPreference()

def tallyScoreCard():
    scorecard = {} #empty the scorecard first this might honestly not be global
    for ballot in allBallots:
        if ballot.preferences[0] in scoreCard:
            scorecard[ballot.preferences[0]] += 1
        else:
            scorecard[ballot.preferences[0]] = 1

def main():
    file = sys.argv[1]
    allBallots = intakeSpreadsheet(file)
    scoreCard = {}  #name:numVotes  keeps track of candidates and how many votes they have
    numSeats = 15  #actually this needs to be input on command line
    threshold = 0

    #numSeats = something that we get from command line
    intakeSpreadsheet()
    checkDoubleBallots(allBallots)
    calculateThreshold(numSeats, threshold) #will this actually change global variable threshold?
    tallyScoreCard(scoreCard)












main() #



#need something to execute main here??
