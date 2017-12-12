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

def active_area(diameter_hole):
    active_area= np.pi * (diameter_hole/2)**2
    return (active_area)

def area_unitcell_square(periodicity,diameter_hole):
    area_unitcell= ((periodicity)**2) - area_hole(diameter_hole/2)
    return (area_unitcell)


def fill_ratio_square( diameter_hole, period,diameter_pd ):
    area_hole=np.pi * (diameter_hole/2)**2
    area_device=np.pi * (diameter_pd/2)**2
    area_unitcell_square=(period**2)# considering square lattice
    numberHoles_inDevice=area_device/area_unitcell_square #square lattice
    area_air=numberHoles_inDevice*area_hole
    fillRatio=area_air/area_device
    Effective_Area_Device=area_device - area_air
    return (numberHoles_inDevice,area_device,Effective_Area_Device,fillRatio)



def fill_ratio_hexagonal( diameter_hole, period,diameter_pd ):
    area_hole=np.pi * (diameter_hole/2)**2
    area_device=np.pi * (diameter_pd/2)**2
    area_unitcell_hexagonal=(period*np.sin(np.deg2rad(60))*period)# considering hexagonal lattice
    numberHoles_inDevice=area_device/area_unitcell_hexagonal #hexagonal lattice
    area_air=numberHoles_inDevice*area_hole
    Effective_Area_Device=area_device - area_air
    fillRatio=area_air/area_device
    return (numberHoles_inDevice,area_device,Effective_Area_Device,fillRatio)
    
    
#diameters=np.arange(400,1400,100)*1e-9
    
#numberofHoles,fill_ratios=fill_ratio_square(diameters,1300e-9,500e-6)

#plt.plot (diameters,fill_ratios)
#plt.show()
#plt.plot (diameters,numberofHoles)
#plt.show()


#hole_degins = {diameter:period}
hole_designs={1500:[3000,2500,2200,2000,1800], 1300:[3000.3500,2300,2000,1600], 1150:[2250,2000,1750,1500],1000:[1500,2000,1500,1300]}


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


