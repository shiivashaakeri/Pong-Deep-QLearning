from sre_parse import State
from DiscretePong import *
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd


paddle_discrete = 18
ball_discrete_posx = 17
ball_discrete_posy = 18
ball_discrete_velx = 9
ball_discrete_vely = 9
action = 2 

NumEpisodes = 5000
MaxTimeSteps = 50000

tracker = np.zeros((int(NumEpisodes/100)+1,2))  #Average Hit for each 100 episodes


qTable = np.zeros((paddle_discrete,ball_discrete_posx,ball_discrete_posy,
                    ball_discrete_velx,ball_discrete_vely,action))


learningRate = 0.05
explorationRate = 0.05
discountFactor = 0.99

experience = 0

def epsilonGreedy(epsilon, s):
    if (np.random.rand() > epsilon):
        actions = qTable[s][:]
        return np.argmax(actions)
    else:
        return randint(0,1)

def getLearningRate(episode): #Alpha
    alpha_decay = 0.9992
    return np.max([0.8 * np.power(alpha_decay, episode), 0.02])

def getExplorationRate(episode):   #Epsilon
    epsilon_decay = 0.9992
    return np.max([0.5 * np.power(0.9992, episode), 0.02])


hits = 0
qtable_save_step = 500


for episode in range(0, NumEpisodes+1):
    #Begin Episode
    step = 0

    # DicretePong (p1bin, ballXbin, ballYbin, ballXvelbin, ballYvelbin, ballXvelmax, ballYvelmax)
    MDP = DiscretePong(qTable.shape[0], qTable.shape[1], qTable.shape[2], qTable.shape[3], qTable.shape[4], 20, 20)
    state, r, running, temp = MDP.update(2)  # update(2) because with a=2 paddles will have no move and nothing  #initialization
    learningRate = getLearningRate(episode)
    explorationRate = getExplorationRate(episode)

    while(running and step < MaxTimeSteps):
        step = step + 1  
        #Action Selection
        action = epsilonGreedy(explorationRate, state)
        #Exicute Action
        next_state, reward, running, hit = MDP.update(action)
        hits += hit 
        #Update Equation       
        qTable[state][action] = qTable[state][action] + learningRate *(reward + discountFactor * 
                                                                        np.max(qTable[next_state][:]) - qTable[state][action])           
        #Update State
        state = next_state

    if (step > qtable_save_step):
        np.save('q_table.npy', qTable)
        qtable_save_step = step
        print("Step which Q table is saved: " + str(qtable_save_step))

    experience = experience + step

    if (np.mod(episode, 100) == 0):
        tracker[int(episode/100), 0] = hits/100 #Average Hits in 100 previous games
        tracker[int(episode/100), 1] = episode
        
        print("Average for previous 100 episodes = " + "Experience:" + str(experience/100) + "  -  " 
                                                    + "hits:" + str(hits/100) + "  -  " + "episode:" + str(episode))
        experience = 0
        hits = 0


sns.set_style("darkgrid")
plt.figure()
df = pd.DataFrame({'Average Hits': tracker[:, 0], 'Episodes': tracker[:, 1]})
ax = sns.lineplot(x="Episodes", y="Average Hits", data=df).set_title("Q-Learning Agent Training")
plt.show()

        


    