import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5,3))
cases = np.loadtxt('cases.dat')
dates = ['Aug {:d}'.format(i) for i in np.arange(cases.shape[0])+24] # starting from Aug 24
plt.plot(dates, cases, 'ko-')
plt.tick_params(direction='in')
plt.xlabel('Date')
plt.xlabel('New cases')
plt.savefig('new_cases.png', dpi=300, bbox_inches='tight')

plt.figure(figsize=(5,3))
cases = np.loadtxt('cases.dat')
dates = ['Aug {:d}'.format(i) for i in np.arange(cases.shape[0])+24] # starting from Aug 24
plt.plot(dates, np.cumsum(cases), 'ko-')
plt.tick_params(direction='in')
plt.xlabel('Date')
plt.xlabel('Cumulative count')
plt.savefig('total_cases.png', dpi=300, bbox_inches='tight')

plt.show()
