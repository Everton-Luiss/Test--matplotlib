import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_vals=[]
y_vals=[]

index=count()
def animated(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))

    plt.cla()#cla method garante que o grafico fique da mesma cor
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animated, interval=20)


plt.tight_layout()
plt.show()