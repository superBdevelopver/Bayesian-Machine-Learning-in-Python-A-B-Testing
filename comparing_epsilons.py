import numpy as np
import matplotlib.pyplot as plt


class BanditARM:
    def __init__(self, p):
        # the win rate
        self.p = p
        self.p_estimate = 0
        self.N = 0
    def pull(self):
        # follow a normal distribution
        return np.random.random() + self.p
    def update(self, x):
        self.N = self.N + 1
        self.p_estimate = self.p_estimate + (x - self.p_estimate) / self.N

def experiment(m1, m2, m3, eps, num_trial):
    bandits  = [BanditARM(m1), BanditARM(m2), BanditARM(m3)]

    means = np.array([m1, m2, m3])
    true_best = np.argmax(means)
    count_suboptimal = 0

    data = np.empty(num_trial)

    # use epsilon-greedy to select next bandit
    for i in range(num_trial):
        if np.random.random() < eps:
            j = np.random.randint(len(bandits))
        else:
            # use the current best choice
            j = np.argmax([b.p_estimate for b in bandits])

        if j == true_best:
            count_suboptimal += 1

        x = bandits[j].pull()
        bandits[j].update(x)
        # for the output
        data[i] = x
    
    cumulative_average = np.cumsum(data) / (np.arange(num_trial) + 1)
    
    plt.plot(cumulative_average)
    plt.plot(np.ones(num_trial)*m1)
    plt.plot(np.ones(num_trial)*m2)
    plt.plot(np.ones(num_trial)*m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.p_estimate)

    print('percent suboptimal for epsilon = %s:'% eps, float(count_suboptimal) / num_trial)

    return cumulative_average

if __name__ == '__main__':
    m1, m2, m3 = 1.5, 2.5, 3.5
    experiment_A = experiment(m1, m2, m3, 0.1, 100000)
    experiment_B = experiment(m1, m2, m3, 0.05, 100000)
    experiment_C = experiment(m1, m2, m3, 0.01, 100000)

    # log scale plot
    plt.plot(experiment_A, label = 'esp = 0.1')
    plt.plot(experiment_B, label = 'esp = 0.05')
    plt.plot(experiment_C, label = 'esp = 0.01')
    plt.legend()
    plt.xscale('log')
    plt.show()

    # linear plot
    plt.plot(experiment_A, label = 'esp = 0.1')
    plt.plot(experiment_B, label = 'esp = 0.05')
    plt.plot(experiment_C, label = 'esp = 0.01')
    plt.legend()
    plt.show()
