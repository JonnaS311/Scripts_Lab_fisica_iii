import matplotlib
import numpy as np
import pandas as pd
import matplotlib. pyplot as plt
from scipy.fftpack import fft, fftfreq

d = pd.read_csv('datos 4.csv')
# eliminamos las columnas que no son de nuestro interes
d = d.drop(['wy (rad/s)'], axis=1)
d = d.drop(['wz (rad/s)'], axis=1)

# removemos los datos que son de ruido
d = d.loc[d['time']> 7]
d = d.loc[d['time']< 45]

ax = d.plot(x='time',y='wx (rad/s)',title='Cuarta toma de datos',ylabel='Amplitud',xlabel='Tiempo',cmap=matplotlib.colormaps['jet'])

# transformada discreta de fourier
f = np.fft.fft(d['wx (rad/s)'])/1000
freq = np.fft.fftfreq(len(d['wx (rad/s)']),d=5)*2500


fig,pl = plt.subplots(2)
fig.suptitle('Transformada rápida de Fourier [FFT]')
fig.subplots_adjust(hspace=0.5)
pl[0].plot(d['time'].to_numpy(),d['wx (rad/s)'].to_numpy())
pl[0].set(xlabel='tiempo [s]',ylabel='Amplitud')
pl[1].plot(freq,abs(f), 'tab:purple')
pl[1].set(xlabel='frecuencia [Hz]',ylabel='FFT Amplitud')
pl[1].set_xlim(0,1)
pl[1].set_ylim(0,10)


plt.show()


"""
Y2 = fft(d['wx (rad/s)'].to_numpy()) / 1000
frq2 = fftfreq(d.shape[0], d['time'].to_numpy())

fig = plt.figure(figsize=(8, 6))
ax2 = fig.add_subplot()
ax2.plot(Y2, frq2)
"""

