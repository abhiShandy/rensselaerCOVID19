# Python script to plot new cases and cumulative cases
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cases.csv')

plt.figure(figsize=(10,3))
sns.barplot('date', 'new-cases', data=df, color='royalblue', alpha=0.5)
plt.xlabel('Date')
plt.ylabel('New Cases', color='royalblue')
plt.tick_params('y', colors='royalblue', direction='in')
plt.grid(True, axis='y', which='major', ls=':', c='royalblue')

ax = plt.twinx()
ax.plot(df['date'], np.cumsum(df['new-cases']), 'tomato', marker='o')
ax.set_ylabel('Cumulative', color='tomato')
ax.tick_params(colors='tomato')
ax.tick_params(colors='tomato')
# automatically adjust tick labels
Ndates = len(df['date'])
showNdates = 10
labels = np.array(df['date'])[::Ndates//showNdates]
ax.set_xticks(labels)
plt.savefig('cases.png', dpi=300, bbox_inches='tight')
plt.show()

