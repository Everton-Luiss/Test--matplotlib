import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
#Aula 1 - https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

#plt.style.use('fivethirtyeight')

plt.plot(x_vals, y_vals, 'bo', color='green', marker='h', linewidth=2, markersize=12)#grafico de pontos

#plt.plot(x_vals, y_vals, 'r+')
#grafico de bolinhas com sinal de +

#plt.plot(x_vals, y_vals, 'go--', linewidth=2, markersize=1)
#grafico de bolinhas ligado por linhas tracejadas


plt.tight_layout()#plota um gráfico maior
plt.show()
