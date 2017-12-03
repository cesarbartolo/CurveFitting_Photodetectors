"""
Code created to calculate the fill ratio  
(holes/active) in PDs and its consequences in
their properties

"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def area_hole (radio):
    area_hole= np.pi * radio**2
    return (area_hole)

def active_area(radio_pd):
    active_area= np.pi * radio_pd**2
    return (active_area)

def area_unitcell(periodicity, radio_hole):
    area_unitcell= ((periodicity)**2) - area_hole(radio_hole)
    return (area_unitcell)

def fill_ratio ( area_allHoles, area_device):
    fill_ratio=area_allHoles/ area_device
    return (fill_ratio)
    



radio_hole=np.array([ 300,350,500,600,650])*1e-9

area=area_hole(radio_hole)
print (area)
plt.plot(radio_hole, area)


radio_devices=np.array([15,30,50,125,250])*1e-6    
act_a=active_area(radio_devices)    
print (act_a)