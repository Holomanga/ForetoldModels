import numpy as np
import csv
from enum import Enum

# Markov chain model of ACE top charities

# Let's load the data from our csv
charities = []
with open('EffectiveAltruism\\ace_statuses.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        charities.append(row[1:])
charities = charities[1:]

reviewStatusTypes = {
    "unreviewed": "null",
    "exploratory": "null",
    "comprehensive": "comprehensive",
    "standout": "standout",
    "top": "top"
}

transitions = {
	"null": [],
	"comprehensive": [],
	"standout": [],
	"top": []
}

# For each pair of years, append the transition to the appropriate transitions dictionary
for charity in charities:
	for year in range(len(charity)-1):
		transitions[reviewStatusTypes[charity[year]]].append(reviewStatusTypes[charity[year]]+"->"+reviewStatusTypes[charity[year+1]])

# Now calculate each transition as a % of total transitions and print the values
uniqueTop, countsTop = np.unique(transitions["top"], return_counts=True)
print(dict(zip(uniqueTop,countsTop/sum(countsTop))))
uniqueStandout, countsStandout = np.unique(transitions["standout"], return_counts=True)
print(dict(zip(uniqueStandout,countsStandout/sum(countsStandout))))
uniqueComprehensive, countsComprehensive = np.unique(transitions["comprehensive"], return_counts=True)
print(dict(zip(uniqueComprehensive,countsComprehensive/sum(countsComprehensive))))
uniqueNull, countsNull = np.unique(transitions["null"], return_counts=True)
print(dict(zip(uniqueNull,countsNull/sum(countsNull))))