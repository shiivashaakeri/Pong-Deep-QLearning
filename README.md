# Pong Q-Learning and Deep Q-Learning
By definition, in reinforcement learning, an agent takes discrete or continuous actions in
a given environment in order to maximize some notion of reward that is coded into it.
We will utilize two model-free and off-policy reinforcement learning methods in this
project and observe the effects on the performance of the agent in two environments: our
chosen environment from the OpenAI gym and our implemented environment.
Atari Pong is a game environment provided on the OpenAI “Gym” platform. Pong is a
two-dimensional sport game that simulates table tennis which was released in 1972 by Atari.
The player controls an in-game paddle by moving it vertically across the left or right side of
the screen. They can compete against another player controlling a second paddle on the
opposing side. Players use the paddles to hit a ball back and have three actions (“stay”,
“down”, and “up”). The goal is for each player to reach 21 points before the opponent, points
are earned when one fails to return the ball to the other.
OpenAI’s environment gives an RGB image for its state observation (100,800 possible
states). This is far too much information for simple algorithms to handle. So, to acquire the
results quickly, we use 'pygame' to build a simpler environment

## Methods
### Random Action Selection
The main idea behind this method is that each action has the same probability, hence the
agent chooses its actions at random. A random action is chosen in each game and step, and
we can get observation, reward, and other essential information from the environment. After
all games have been played, we can report the average rewards from all games to use this
method to evaluate other methods.
### Q-Learning
Q-learning is an off-policy reinforcement learning algorithm that seeks to find the best
action to take given the current state. It’s considered off-policy because the q-learning
function learns from actions that are outside the current policy, like taking random actions,
and therefore a policy isn’t needed. More specifically, q-learning seeks to learn a policy that
maximizes the total reward.
### Deep Q-Learning
In deep Q-learning, we use a neural network to approximate the Q-value function. The
state is given as the input and the Q-value of all possible actions is generated as the output. There are two main phases that are interleaved in the Deep Q-Learning Algorithm. One
is where we sample or remember the environment by performing actions and store away the
observed experienced tuples in a replay memory. The other is where we select the small
batch of tuples from this memory, randomly, and learn from that batch using an algorithm
(gradient descent or ‘adam’) update step.

## Environments
### OpenAI Gym: Pong
The openAI “gym” framework gives us the dataset we need in terms of observations at
every time step. An observation consists of pixel values of the game screen taken for a9
window of k consecutive frames. This is a numpy.array of shape (210, 160, 3), where the
first value x is the height of the screen, the second value y stands for the width of the screen,
and the third represents the RGB dimension for each pixel at coordinate (x, y). 
- gym.make(env): This simply gets our environment from the open AI gym. We will be
calling env = gym.make(‘Pong-v0’), which is saying that our env is Pong.
- env.reset(): This resets the environment back to its first state
- env.step(a): This takes a step in the environment by performing action a. This returns the
next frame, reward, a done flag, and info. If the done flag == True, then the game is over.
- frames: the frames received from OpenAI are much larger than we need, with a much
higher resolution than we need.

### Our Implemented Environment
In this part, every step of building and designing our Pong Environment will be explained.
First, like Gym, we design our elements which are necessary to the agent to develop a sense
of its body and how to take different actions to hit the ball, minimize the difference of the
scores and finally score more goals to win every game. 

* ***You can find more details in the "Report.pdf" file.***
