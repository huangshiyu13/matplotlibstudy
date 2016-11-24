from matplotlib import pyplot as plt
import numpy as np

x = [20,100,800]
y = [0.487430,0.462706,0.459799]
with plt.style.context('fivethirtyeight'):
    plt.semilogx(x, y)
plt.show()