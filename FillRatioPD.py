"""
Code created to calculate the fill ratio  
(holes/active) in PDs and its consequences in
their properties

"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def area_hole (diameter_hole):
    area_hole= np.pi * (diameter_hole/2)**2
    return (area_hole)

def active_area(radio_pd):
    active_area= np.pi * radio_pd**2
    return (active_area)

def area_unitcell(periodicity, radio_hole):
    area_unitcell= ((periodicity)**2) - area_hole(radio_hole)
    return (area_unitcell)


def fill_ratio( diameter_hole, period,radio_pd ):
    area_hole=np.pi * (diameter_hole/2)**2
    area_device=np.pi * radio_pd**2
    area_unitcell=(period**2)# considering square lattice
    numberHoles_inDevice=area_device/area_unitcell #square lattice
    area_air=numberHoles_inDevice*area_hole
    fillRatio=area_air/area_device
    return (numberHoles_inDevice,fillRatio)
    
    
diameters=np.arange(400,1400,100)*1e-9
    
numberofHoles,fill_ratios=fill_ratio(diameters,1300e-9,500e-6)

plt.plot (diameters,fill_ratios)
plt.show()
#plt.plot (diameters,numberofHoles)
#plt.show()


"""
def numberOfHoles_Device(area_unitcell, area_device):
    number_holes=area_device/ area_unitcell
    return (number_holes)
    
def area_air(number_holes,area_hole):
    area_air=number_holes*area_hole
    return (area_air)

def fill_ratio(area_air,active_area):
    fill_ratio=area_air/active_area
    return (fill_ratio)

"""


