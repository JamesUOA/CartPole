import random

import gym

class Agent:
    def __init__(self, env):
        self.action_size = env.action_space.n
        print("action size:", self.action_size)

    def get_action(self):
        angle = state[2]
        action = 0 if angle <0 else 1
        return action


env_name = "CartPole-v1"
env = gym.make(env_name)
state = env.reset()
agent = Agent(env)


for _ in range(200):
    action = agent.get_action()
    state, reward, done, info = env.step(action)
    env.render()
env.close()
