import numpy as np
import matplotlib.pyplot as plt



NUM_TRIAL = 10000
# always explore 
# EPS = 1
# always exploit the current best choice
# EPS = 0
# balance the exploration and exploition
EPS = 0.8
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class BanditARM:
    def __init__(self, p):
        # the win rate
        self.p = p
        # the win rate of sample data, it's zero so far
        self.p_estimate = 0
        # the number of sample, it's zero so far
        self.N = 0
    def pull(self):
        # draw a result with probability p
        return np.random.random() < self.p
    def update(self, x):
        self.N = self.N + 1
        self.p_estimate = self.p_estimate + (x - self.p_estimate) / self.N

def experiment():
    bandits  = [BanditARM(p) for p in BANDIT_PROBABILITIES]

    rewards = np.zeros(NUM_TRIAL)
    num_times_explored = 0
    num_times_exploited = 0
    num_optimal = 0
    optimal_j = np.argmax([b.p for b in bandits])
    print('optimal_j: ', optimal_j)

    # use epsilon-greedy to select next bandit
    for i in range(NUM_TRIAL):
        if np.random.random() < EPS:
            # keep exploring
            num_times_explored += 1
            # choose a bandit randomly
            j = np.random.randint(len(bandits))
        else:
            # use the current best choice
            num_times_exploited += 1
            j = np.argmax([b.p_estimate for b in bandits])
        
        if j == optimal_j:
            num_optimal += 1

        # pull the arm for bandit with the lagest sample
        x = bandits[j].pull()

        # update rewards log
        rewards[i] = x

        # update the distribution of bandit whose arm we just pulled 
        bandits[j].update(x)
    
    # output result
    for b in bandits:
        print('mean estimate:', b.p_estimate)
    
    print('total reward earned:', rewards.sum())
    print('overall win rate:', rewards.sum() / NUM_TRIAL)
    print('num_times_explored:', num_times_explored)
    print('num_times_exploited:', num_times_exploited)
    print('num times selected optimal bandit:', num_optimal)
    
    # plot the results
    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(NUM_TRIAL)+1)
    plt.plot(win_rates)
    plt.plot(np.ones(NUM_TRIAL)*np.max(BANDIT_PROBABILITIES))
    plt.show()

if __name__ == '__main__':
    experiment()