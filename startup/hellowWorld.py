import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

#plt.plot([1, 2.5, 3, 4], [1, 4, 9, 16],'ro')
plt.plot(t, t, t, t**2, 'bs', t, t**3, 'g^',t,t**4,'-',linewidth=10.0)


plt.ylabel('some numbers')
plt.xlabel('x')

plt.show()