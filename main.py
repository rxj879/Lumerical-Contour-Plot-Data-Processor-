# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:11:13 2020

@author: rrj21
"""

from Classes import ModeData
# Import my custom class for the data structure

from Plot import Contour_Plot, Save_Fig_svg, Save_Fig_png, Save_Fig_eps
# Import the custom plot library and functions

Idir = "C:/";
#Idir = "C:/Users/rrj21/Documents/Lumerical_Results";
# The directory where the data file selector is to start from. Change as needed 

Data = ModeData(Idir);
# Create an object of the class "ModeData" for the structured data


##############################################################################
Plot = Contour_Plot(Data)
# Create a plot of the mode data; the "Data" Arguement is of the type <ModeData> class
""" 
Optional key word args include:

X_lim = [min, max] 
Y_lim = [min, max]
X_tick_spacing = float
Y_tick_spacing = float
Cbar_lim = [min, max]
Cbar_tick_spacing = float
Axis_Units = string option: 'mm' or 'nm'. Default = $\mu$m
Cbar_label = 'E-field (V/m)' by default

Contour_Plot(Mode_Data, X_lim = [], Y_lim = [], X_tick_spacing = 0.5, Y_tick_spacing = 0.2,
                 Cbar_lim = [], Cbar_tick_spacing = 0.5, Axis_Units = '$\mu$m' ):
"""

##############################################################################
""" Save the plot as a file. Options are png, eps and svg. Comment out or adapt as needed"""
Save_Fig_png(Data, Plot)
# png format

#Save_Fig_eps(Data, Plot)
# eps format

#Save_Fig_svg(Data, Plot)
# svg format