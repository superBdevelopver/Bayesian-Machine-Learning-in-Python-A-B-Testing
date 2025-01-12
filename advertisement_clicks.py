import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest


if __name__ == '__main__':
    df = pd.read_csv('advertisement_clicks.csv')
    group_a = df[df['advertisement_id'] == 'A']['action'].dropna().to_numpy()
    group_b = df[df['advertisement_id'] == 'B']['action'].dropna().to_numpy()

    # calculate the mean
    group_a_mean = group_a.mean()
    group_b_mean = group_b.mean()
    print('mean of group a', group_a_mean)
    print('mean of group b', group_b_mean)
    group_a_std = group_a.std()
    group_b_std = group_b.std()
    print('std of group a', group_a_std)
    print('std of group b', group_b_std)

    # generate chart of PDF (Probability Density Function)
    sns.kdeplot(group_a, label = 'Group A')
    sns.kdeplot(group_b, label = 'Group B')
    plt.legend()
    plt.show()

    # use z-test to verify if group b has significant better click through rate
    z_stat, p_value = ztest(group_a, group_b)
    print('z_stat: ', z_stat)
    print('p_value', p_value)
    confidence_level = 0.05
    if(p_value <= confidence_level):
        print('advertisement B shows significant improvement')
    else:
        print('advertisement B shows non-significant improvement')
        

    


