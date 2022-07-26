# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:17:56 2022

@author: dh361
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack

# Number of sample points
N = 670
# sample spacing
T = 1.0 /670
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0//(2.0*T), N//2)
test = np.fft.fftfreq(N, T)
test = test[: len(test)//2]
yf = np.abs(yf[:len(yf)//2])


plt.plot(xf, yf)