from random import random
from DiscretePongMDP import *
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit


NumEpisodes = 5000
MaxTimeSteps = 50000

qTable = np.zeros((18,17,18,9,9,2)) #p, x, y, x., y., a

sumScores = 0
avgScores = []
for episode in range(0, NumEpisodes+1):
    scores = [0, 0]
    #Begin Episode
    gameStep = 0
    while True:
        step = 0
        MDP = DiscretePongMDP(qTable.shape[0], qTable.shape[1], qTable.shape[2], qTable.shape[3], qTable.shape[4], 20, 20)
        s, r, running, temp = MDP.update(2)
        score = 0
        while(running and step < MaxTimeSteps):
            step = step + 1  
            #Action Selection
            a = random.randint(0,1)
            #Exicute Action
            ns, r, running, hit = MDP.update(a)
            #Update State
            s = ns
            if r == 100:
                scores[1] += 1
            elif r == -100:
                scores[0] += 1

        gameStep += 1

        if scores[0] == 21 or scores[1] == 21:
            break

    sumScores += scores[1] - scores[0]
    avgScores.append(sumScores / (episode + 1))

    print('Episode {} result: {} - {}'.format(episode, scores[0], scores[1]))
        
#Average Reward Per Episode
sns.set_style("darkgrid")

plt.figure()
df = pd.DataFrame({'Avg Scores': avgScores, 'Episodes': range(NumEpisodes)})

ax = sns.lineplot(x="Episodes", y="Avg Scores", data=df).set_title("Random Agent")

plt.show()
        


    