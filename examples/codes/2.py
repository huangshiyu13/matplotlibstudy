import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib import cm

from mpl_toolkits.mplot3d import axes3d

saveName = '2'


fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
cset = ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
ax.clabel(cset, fontsize=9, inline=1)

plt.savefig('../images/'+saveName+'.png',dpi=600)
plt.show()
