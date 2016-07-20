import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(121)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(122)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot(111) by default


plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(121)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title
plt.show()