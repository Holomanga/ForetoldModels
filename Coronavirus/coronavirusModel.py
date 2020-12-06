from random import choice
import numpy as np

cases = [7814, 9819, 11337, 13994, 17339, 19876, 23865, 28266, 30817, 34377, 37111, 40134, 42729, 43116]

percentageIncreases = []
for i in range(len(cases)-1):
	percentageIncreases.append(cases[i+1]/cases[i] - 1)

percentageDeltas = []
for i in range(len(percentageIncreases)-1):
	percentageDeltas.append(percentageIncreases[i+1]/percentageIncreases[i])

currentDay = 42
targetDay = 60

results = []
for N in range(10000):
	modelCases = cases[-1]
	modelPercentageIncrease = (43116/7814)**(1/(len(cases)-1)) - 1
	hist = [modelCases]
	for day in range(currentDay+1,targetDay+1):
		modelPercentageIncrease *= choice(percentageDeltas)
		modelCases*=(1+modelPercentageIncrease)
		hist.append(modelCases)

	results.append(hist[-1])

print(results)
s = "=mm("
for i in range(100):
	s += "uniform(" + str(np.percentile(results,i)) + ","+ str(np.percentile(results,i+1)) + "), "
s += ")"
print(s)