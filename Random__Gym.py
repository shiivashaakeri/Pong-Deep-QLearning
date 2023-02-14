import random
import gym
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd

class RandomAgent:
    def __init__(self, actionSpace):

        self.env = gym.make('PongNoFrameskip-v4')

        self.actionSpace = actionSpace

    def act(self, state):
        return random.choice(self.actionSpace)

    def resetGame(self):
        return self.env.reset()

    def Qlearning(self):
        episodes = 5000

        scores = []

        totalSteps = 0
        totalScores = 0
        avgScores = []
        for episode in range(episodes):
            state = self.resetGame()

            currScore = 0
            done = False
            while not done:
                action = self.act(state)

                newState, reward, done, _ = self.env.step(action)
                currScore += reward

                totalSteps += 1

            scores.append(currScore)
            totalScores += currScore
            avgScores.append(totalScores / (episode + 1))

            print('Episode: {} - Score: {}'.format(episode, currScore))


        sns.set_style("darkgrid")

        plt.figure()
        df = pd.DataFrame({'Avg Scores': avgScores, 'Episodes': range(episodes)})


        ax = sns.lineplot(x="Episodes", y="Avg Scores", data=df).set_title("Random Agent")

        plt.show()
        

if __name__ == '__main__':
    RlAgent = RandomAgent([2, 3])
    RlAgent.Qlearning()