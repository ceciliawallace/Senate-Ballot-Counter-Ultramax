'''
This is the main doc.
'''
import sys
import Ballot
import csv

#Spreadsheet should be formatted as:
#column1=timestamp, column2=Tnumber; all following columns are preferences
#converts spreadsheet into objects
#returns list of all ballots
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
    return allBallots

def calculateThreshold(numSeats, threshold):
    numVotes = len(allBallots)
    calcThreshold = numVotes / numSeats
    threshold = int(calcThreshold)


def tallyScoreCard(scoreCard):
    scorecard = {} # this is a dictionary... empty the scorecard first this might honestly not be global
    for ballot in allBallots:
        if ballot.preferences[0] in scoreCard:
            scorecard[ballot.preferences[0]] += 1
        else:
            scorecard[ballot.preferences[0]] = 1
    return scoreCard

"""
this method will take in a tallied scorecard--the initial one--and find candidates over
the surplus level whose votes we need to redistribute. it will pass on this info with a dictionary that has
candidate name:num of votes to redistribute
"""
def findSurplus(threshold, scoreCard):
    surplusInfo = {} # this will be another dictionary that goes {candidate name:number to redistribute}
    for candidate in scoreCard: # go through each candidate we have
        if scoreCard[candidate] >= threshold: # if they have more votes than threshold, we're going to redistribute
            numToRedistribute = scoreCard[candidate] - threshold
            surplusInfo[candidate] = numToRedistribute #add candidate:numToRedistribute to dictionary
    return surplusInfo

def redistributeSurplus(surplusInfo, allBallots):
    for candToRedistribute in surplusInfo:
        numToRedistribute = surplusInfo[candToRedistribute] # this should be the num of ballots to redistribute from this candidate
        for ballot in allBallots:
            if numToRedistribute > 0: #we haven't redistributed all appropriate ballots yet
                if ballot.preferences[0] == candToRedistribute: # we wanna redistribute these matches
                    ballot.popPreference()

                    """here should think about eliminating empty ballots from allBallots"""

                    numToRedistribute -= 1
                    #then we wanna go to the next ballot
            else: #if we have redistributed all of the surplus for this candidate...
                break # wanna get out of ONLY THIS for loop, go to next candidate... check to make sure that's happening
    return allBallots

"""
this will find which candidate has least votes, and then will return their name
"""
def findEliminated(scoreCard):
    #only problem with this is... currently if there's a min tie it seems to return the lastest entry added which is
    #kinda arbitrary, but perhaps that's fair?
    eliminatedInfo = min(scoreCard.items(), key=lambda x: x[1]) #this is a tuple with (candName, numVotes)
    return eliminatedInfo[0] #this returns name of candidate to redistribute


def redistributeEliminated(eliminatedCand, allBallots):
    for ballot in allBallots:
        if ballot.preferences[0] == eliminatedCand: #we wanna redistribute these ballots, what will happen if null??
            ballot.popPreference()

            """here should think about eliminating empty ballots from allBallots"""

    return allBallots


def main():

    # first task: intake the spreadsheet and create ballots
    #file = sys.argv[1]
    file = sys.argv[2]
    print("fileName: ", file)

    allBallots = intakeSpreadsheet(file)
    # second task: find duplicate T number ballots and get rid of the first submission, keep the second
    allBallots = checkDoubleBallots(allBallots)

    # third task: get number of seats up for election from user input, then calculate election threshold using # votes cast
    numSeats = int(sys.argv[1])
    print("numSeats: ", numSeats)
    # numSeats = 7  #actually this needs to be input on command line but doing dummy number for now
    threshold = 0
    threshold = calculateThreshold(numSeats, threshold)

    #fourth task, tally up initial score card to find surplus and redistribute it
    scoreCard = {}  # dictionary w name:numVotes -- it keeps track of candidates and how many votes they have
    scoreCard = tallyScoreCard(scoreCard)
    print("initial scorecard: ", scoreCard.itmes())
    surplusInfo = findSurplus(threshold, scoreCard) #this will be another dictionary...
    allBallots = redistributeSurplus(surplusInfo, allBallots) #so NOW, all ballots should be reshuffled so that surplus ppl eliminated

    #fifth task, tally the scorecard again, figure out how many elimination rounds needed, start eliminating people
    numToEliminate = len(scoreCard) - numSeats
    for round in range(numToEliminate): #wanna do the right num of eliminations
        scoreCard = {}
        scoreCard = tallyScoreCard(scoreCard)
        eliminatedCand = findEliminated(scoreCard) # this is a tuple with (name, numVotes)
        allBallots = redistributeEliminated(eliminatedCand, allBallots)

    #sixth task, tally score card again and this should be our electees!!!!
    scoreCard = {}
    scoreCard = tallyScoreCard(scoreCard)
    print(scoreCard.items())


main() #



#need something to execute main here??
