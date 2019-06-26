'''
This is the main doc.
'''


allBallots = []
scoreCard = {} #name:numVotes  keeps track of candidates and how many votes they have
numSeats = 15 #actually this needs to be input on command line
threshold = 0


def intakeSpreadsheet():

def checkDoubleBallots():
    for i in allBallots:
        for j in allBallots:
            if i.tNumber == j.tNumber:
                allBallots.remove(i) #will this actually remove the first ballot submitted? could throw error

def calculateThreshold(numSeats):
    numVotes = len(allBallots)
    calcThreshold = numVotes / numSeats
    calcThreshold = int(threshold)
    return calcThreshold

def findSurplus():
    for candidate in scoreCard:
        if scoreCard[candidate] >= threshold:
            numToRedistribute = scoreCard[candidate] - threshold




def redistributeSurplus(candidateName, numToRedistribute):
    counter = 0
    for ballot in allBallots:
        if counter < numToRedistribute:
            if ballot.preferences[0] == candidateName: #we wanna redistribute these ballots
                ballot.popPreference()
                counter += 1
        else:
            return #when we finally hit the number to redistribute, we wanna return

def findEliminated():

def redistributeEliminated(candidateName):
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
    #numSeats = something that we get from command line
    intakeSpreadsheet()
    checkDoubleBallots()
    threshold = calculateThreshold(numSeats) #will this actually change global variable threshold?
    tallyScoreCard()












main() #



#need something to execute main here??