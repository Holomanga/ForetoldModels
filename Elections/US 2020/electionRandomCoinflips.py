import random
import numpy as np
from collections import Counter

#goals:
# calculate an election from steps T to N 1000 times
# find distribution of results
# add distribution to an array
# T -> T+1

T = 0
N = 50
nCandidates = 10
outcomes = range(nCandidates)
weights = [1,1,1,1,1,1,1,1,1,1]
weights = weights/np.sum(weights)

runningResults = []
winners = [[0 for o in outcomes] for i in range(N)]

while T < N:
	for iteration in range(100):
		temporaryResults = list(runningResults)
		for i in range(T,N):
			temporaryResults.append(np.random.choice(outcomes,p=weights))
		#print(temporaryResults)
		winner = max(temporaryResults,key=temporaryResults.count)
		winners[T][winner] += 1

	runningResults.append(np.random.choice(outcomes,p=weights))

	print(N-T)
	T += 1

print(winners)

import matplotlib.pyplot as plt

flipTimes = range(N)

plt.plot(flipTimes, winners)

plt.ylabel('% chance of winning from here')
plt.xlabel('Time')
plt.show()
