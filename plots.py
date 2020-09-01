import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('cases.csv')

plt.figure(figsize=(10,3))
plt.plot(df['date'], df['new-cases'], 'b')
plt.xlabel('Date')
plt.ylabel('New Cases', color='b')
plt.tick_params('y', colors='b')

ax = plt.twinx()
ax.plot(df['date'], np.cumsum(df['new-cases']), 'r')
ax.set_ylabel('Cumulative', color='r')
ax.tick_params(colors='r')
ax.tick_params(colors='r')
plt.savefig('cases.png', dpi=300, bbox_inches='tight')
plt.show()
