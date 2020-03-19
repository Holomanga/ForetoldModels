from numpy.random import poisson, binomial
from math import sqrt

def thresholdChance(total, number_done, number_won, threshold):
	nSamples = 1000000
	nums = number_won + binomial(total-number_done,(number_won+1)/(number_done+(1/priorProbability)),(nSamples,))
	return (sum(nums >= threshold))/(nSamples)

def logoddsAverage(A,B):
	oddsRA = A/(1-A)
	oddsRB = B/(1-B)
	avg = sqrt(oddsRA*oddsRB)
	return avg/(1+avg)

nC = 6
priorProbability = 1/4
CLPchance = thresholdChance(647,580,27,33)
affiliateChance = thresholdChance(32,22,0,3)

print(CLPchance)
print(affiliateChance)
print(logoddsAverage(CLPchance,affiliateChance))
print(logoddsAverage(max(CLPchance,affiliateChance),3/(nC+2)))