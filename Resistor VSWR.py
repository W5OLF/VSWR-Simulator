# W5OLF VSWR Simulator (w5olf@comcast.net)

import numpy as np
import matplotlib.pyplot as plt
def par(x, y):  # add impedances in parallel
    return x*y/(x+y)
def ser(x, y):  # add impedances in series
    return x + y
def res(val):
    return val*np.ones(fnumb)
def cap(val):  # get impedance vs f of capacitor
    return -1e6j/(2*np.pi*f*val)
def ind(val):  # get impedance vs f of inductor
    return 2j*np.pi*f*val

# Circuit values; inductance(uH), capacitance(pF), resistance(ohms), frequencies (MHz)
# START USER INPUT
title = 'Resistor at Higher Frequencies'
fstart = 10.0  # start frequency
fstop = 1000.0  # stop frequency
fnumb = 50  # number of frequency values (integer)
f = np.linspace(fstart, fstop, fnumb)  # do not change this line
maxVSWR = 3.0  # maximum VSWR to plot
RS = 50.0  # source resistance value
LW = 0.014  # carbon resistor 1/4" wire leads
CP = 2.0  # carbon resistor parallel capacitance
VAR = np.linspace(30.0, 70.0, 11)  # load resistor range of values
def circuit():  # do not change this line
    for i in range(len(VAR)):  # do not change this line
        zIN = ser(ind(LW), par(cap(CP), res(VAR[i])))  # collapse circuit to input impedance
# END USER INPUT

        gamma = (zIN - RS)/(zIN + RS)  # VSWR at input
        VSWR = (1 + abs(gamma))/(1 - abs(gamma))
        plt.plot(f, VSWR, label=str(VAR[i]))
plt.figure(figsize=(12, 6))
plt.ylim(1, maxVSWR)  # VSWR range limit 
circuit()
plt.title(title, fontsize=18)
plt.ylabel('VSWR', fontsize=16)
plt.xlabel('Frequency(MHz)', fontsize=16)
plt.xlim((fstart, fstop))
plt.legend(loc='best')   
plt.show()
