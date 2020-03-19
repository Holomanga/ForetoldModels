import numpy as np

data = ["PPPPPPPPP","OOOOONNNP","PPPPPPPPP","PPNPPNNNN","PPPPPPPPP","PPPPPPPPP","ONNPPPPPN","PPPPPPPPP","OOOOONNNW","PPNNNNNNW","PPPPPPNPW","PPNNNNNWW","PPPPPNNWW","PPNNNNWWW","PPPPNNWWW","PPPPPWWWW","NPNNNWWWW","ONNNNWWWW","NNNNNWWWW","PPPPWWWWW","PPNNWWWWW","PPNWWWWWW","PPWWWWWWW","NNWWWWWWW","PPWWWWWWW","PPWWWWWWW","NNWWWWWWW","PWWWWWWWW","WWWWWWWWW"]

pairs = {
	"P": [],
	"N": [],
	"O": [],
	"W": []
}

for s in data:
	for i in range(len(s)-1):
		pairs[s[i]].append(s[i]+s[i+1])

uniqueP, countsP = np.unique(pairs["P"], return_counts=True)
print(dict(zip(uniqueP,countsP/sum(countsP))))

uniqueN, countsN = np.unique(pairs["N"], return_counts=True)
print(dict(zip(uniqueN,countsN/sum(countsN))))

uniqueO, countsO = np.unique(pairs["O"], return_counts=True)
print(dict(zip(uniqueO,countsO/sum(countsO))))

uniqueW, countsW = np.unique(pairs["W"], return_counts=True)
print(dict(zip(uniqueW,countsW/sum(countsW))))