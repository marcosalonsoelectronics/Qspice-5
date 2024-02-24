# -*- coding: utf-8 -*-
"""
Buck converter CCM

@author: Alonso
"""
from math import pi, log10, sqrt
from control import tf, bode_plot

L= 50e-6; C=10e-6; R=1; rl=0.05; rc=0.15
VB= 10

s = tf('s')
G = VB*(1+rc*C*s)/( L*C*(1+rc/R)*s**2 + (L/R+rc*C+rl*C+rl*rc*C/R)*s + 1+rl/R )

R1=2.24e3; R2=2.24e3; C2=10e-9
Comp= (1 + R2*C2*s)/(R1*C2*s)
Vpp=10
H=1

T=Comp*(1/Vpp)*G*H

# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10,1e6), \
                              omega_num=100 )
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=56
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)




