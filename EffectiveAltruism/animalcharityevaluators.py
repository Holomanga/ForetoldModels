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

reviewStatusCodes = {
    "unreviewed": 0,
    "exploratory": 0,
    "comprehensive": 1,
    "standout": 2,
    "top": 3
}

transitions = [[],[],[],[]]

# For each pair of years, append the transition to the appropriate transitions dictionary
for charity in charities:
  for year in range(len(charity)-1):
      if reviewStatusCodes[charity[year+1]] != 0:
        transitions[reviewStatusCodes[charity[year]]].append(reviewStatusCodes[charity[year+1]])

# TODO: I want a list for which list[x][y] is the probability of transition from x to y

# Now calculate each transition as a % of total transitions and print the values
uniqueTop, countsTop = np.unique(transitions[3], return_counts=True)
topTransitions = list(zip(uniqueTop,countsTop/sum(countsTop)))
uniqueStandout, countsStandout = np.unique(transitions[2], return_counts=True)
standoutTransitions = list(zip(uniqueStandout,countsStandout/sum(countsStandout)))
uniqueComprehensive, countsComprehensive = np.unique(transitions[1], return_counts=True)
comprehensiveTransitions = list(zip(uniqueComprehensive,countsComprehensive/sum(countsComprehensive)))
uniqueNull, countsNull = np.unique(transitions[0], return_counts=True)
nullTransitions = list(zip(uniqueNull,countsNull/sum(countsNull)))

print("Top to " + str(topTransitions))
print("Standout to " + str(standoutTransitions))
print("Comprehensive to " + str(comprehensiveTransitions))
print("Unreviewed to " + str(nullTransitions))

# Now we can do the markov chain model
from scipy.stats import poisson

# currentCharityStatuses: the status of each WAS charity ACE evaluates
currentCharityStatuses = ["top"]

totalNumberOfCharities = len(charities)
percentageCharitiesOfDesiredType = (len(currentCharityStatuses)+1)/(totalNumberOfCharities+2)
newCharitiesPerYear = len(charities)/(len(charities[0])-1) * percentageCharitiesOfDesiredType