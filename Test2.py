#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:38:08 2017

@author: solidstates
"""
import numpy as np
import matplotlib.pyplot as plt
### commit file change!
#dkfhdsf
##djiosfa
#lkshfdfdsf


"""
W_sun: 1000 W/m 2
d: 0.1 mm
R: 20 mm
f: 30 mm
r: 50 %
E: 90 %Usage
BPF: 5.7 % (850±30 nm)
T: 27 °C
B: 200 MHz
Rf: 5 kΩ
M: 100
A: 0.5 A/W
x: 0.2

"""

W_sun= 1000# W/m 2
f= 30e-3 #m
r=50  #[%] refelcetance of target
E=90 # [%] lens efficiency 
BPF=5.7 #[%] Band pass filter transmittance (transmittance of sunlight)
R=20e-3 #m Len s Diameter
d=0.1e-3 #m  Diatance to the target objetc

###############################################################################
#Calculation method of natural light

L=np.linspace(1,10,1000)

D=d*(L/f)
W_sun1= W_sun*(D**2) #Ligth level at projection area coming from SUN
plt.plot(L,W_sun1)
W_sun2_dependable= W_sun1*(R/L)**2*r*(1/2)*E*BPF
#Light level that deecttor receives after lens
W_sun2=W_sun*(d*(R/2*f))**2*r*E*BPF
#plt.plot(L,W_sun2 )


"""
Ω: Light receiving lens solid angle [sr] Ω ≈ (R/2) 2 × π/L 2
r: Reflectance of the target object [%]
E: Lens efficiency [%]
BPF: Band-pass filter transmittance (transmittance of sunlight) [%]
R: Lens diameter [m]
L: Distance to the target object [m]
"""
OHM=(R/2)**2 * (np.pi/ L**2)


################################################################################
#Calculation method of signal light


# Light that is received by detecor after signal (W_pulse) reflects the target object

W_pulse=2
W_pulse1= W_pulse* OHM *r*(1/np.pi)*E
W_pulse1_2=W_pulse*(R/(2*L))**2 *r *E
plt.plot(L,W_pulse1)

###The light level received by the detector W_pulse1 is inversely proportional to the square of the distance L. To
##increase the incident light level, the signal light’s pulse power W_pulse or the lens diameter R must be increased.







