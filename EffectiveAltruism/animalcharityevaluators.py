import numpy as np
import csv

# Markov chain model of ACE top charities

# Let's load the data from our csv
charities = []
with open('EffectiveAltruism\\ace_statuses.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        charities.append(row[1:])
charities = charities[1:]

reviewStatusTypes = {
    "unreviewed": "unreviewed",
    "exploratory": "unreviewed",
    "comprehensive": "comprehensive",
    "standout": "standout",
    "top": "top"
}

transitions = {
	"unreviewed": [],
	"comprehensive": [],
	"standout": [],
	"top": []
}

# For each pair of years, append the transition to the appropriate transitions dictionary
for charity in charities:
  for year in range(len(charity)-1):
      if reviewStatusTypes[charity[year+1]] != "unreviewed":
        transitions[reviewStatusTypes[charity[year]]].append(reviewStatusTypes[charity[year+1]])

# Now calculate each transition as a % of total transitions and print the values
uniqueTop, countsTop = np.unique(transitions["top"], return_counts=True)
topTransitions = dict(zip(uniqueTop,countsTop/sum(countsTop)))
uniqueStandout, countsStandout = np.unique(transitions["standout"], return_counts=True)
standoutTransitions =  dict(zip(uniqueStandout,countsStandout/sum(countsStandout)))
uniqueComprehensive, countsComprehensive = np.unique(transitions["comprehensive"], return_counts=True)
comprehensiveTransitions = dict(zip(uniqueComprehensive,countsComprehensive/sum(countsComprehensive)))
uniqueNull, countsNull = np.unique(transitions["unreviewed"], return_counts=True)
nullTransitions = dict(zip(uniqueNull,countsNull/sum(countsNull)))

print("Top to " + str(topTransitions))
print("Standout to " + str(standoutTransitions))
print("Comprehensive to " + str(comprehensiveTransitions))
print("Unreviewed to " + str(nullTransitions))

# Now we can do the markov chain model
from scipy.stats import poisson
from np.random import rand

# currentCharityStatuses: the status of each WAS charity ACE evaluates
currentCharityStatuses = ["top"]

totalNumberOfCharities = len(charities)
percentageCharitiesOfDesiredType = (len(currentCharityStatuses)+1)/(totalNumberOfCharities+2)
newCharitiesPerYear = len(charities)/(len(charities[0])-1) * percentageCharitiesOfDesiredType