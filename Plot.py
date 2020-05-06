# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:44:57 2020

@author: rrj21
"""

import matplotlib.pyplot as plt
# import the matplotlib library

from matplotlib.colors import LinearSegmentedColormap
# Import the colour map options

from Funcs import  AxisLimitTune, RescaleAxis
# Import axis limit tuning algorithm from Funcs

import numpy as np
# Import the mathematical library




def Contour_Plot(Mode_Data, X_lim = [], Y_lim = [], X_tick_spacing = 0.5, Y_tick_spacing = 0.2,
                 Cbar_lim = [], Cbar_tick_spacing = 0.5, Axis_Units = '$\mu$m', 
                 Cbar_label = 'E-field (V/m)'):
    """Here we make the plot"""
    
    fig = plt.figure(figsize = (12,5))
    # Create a blank figure with the specificed width and height
    
    SMALL_SIZE  = 22
    MEDIUM_SIZE = 25
    BIGGER_SIZE = 30
    # Define three font sizes
    
    plt.rcParams['font.family'] = "sans-serif"
    # Set The font. See following lines for options
    """ Font options: [ 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace' ]"""
    
    
    plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    # Asign font sizes to figure texts
    
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    # fractions of the figure width and height
    
    ax = fig.add_axes([left, bottom, width, height])
    # Adds the axes at the specificed locations to give the margin sizes
    
    X, Y = np.meshgrid(Mode_Data.X_Data[0], Mode_Data.X_Data[1])
    # Create the coordinate grid based on the coordinate data
    
    if Axis_Units != '$\mu$m':
        """ Test for a user input on the axes scale"""
        
        X, Y = RescaleAxis(X, Y, Axis_Units)
        # Rescale X and Y accord to the user input
    
    Z = np.transpose(Mode_Data.Plane_Data)
    # transpose gridded the scalar data to fit the coordinate grid data
    
    X_lim, Num_X_Ticks  =  AxisLimitTune(X, X_lim, X_tick_spacing)
    
    Y_lim, Num_Y_Ticks  =  AxisLimitTune(Y, Y_lim, Y_tick_spacing)
    
    Cbar_lim, Num_Z_Ticks  =  AxisLimitTune(Z, Cbar_lim, Cbar_tick_spacing)
    
    plt.gca().set_aspect('equal', adjustable='box')
    # Sets the aspect ratio of the x and y axis to be equal - no scale scew
       
    ax.tick_params(direction='out', length=6, width=2, colors='k',
               grid_color='k', grid_alpha=0.5)
    # modify the axis ticks
    
    plt.rcParams['axes.linewidth'] = 2 
    #set the value of the figure linwidth globally

    ax.set_xlabel("y ("+Axis_Units+")")
    # Set label of the x-axis
    
    plt.xticks(np.linspace(X_lim[0],X_lim[1],Num_X_Ticks))
    # Set the minimum, maximum and number of the x ticks
    
    ax.set_ylabel("z ("+Axis_Units+")", labelpad = 3)
    # Set the label of the y-axis and add some space between it and the axis
    
    plt.yticks(np.linspace(Y_lim[0],Y_lim[1],Num_Y_Ticks))
    # Set the minimum, maximum and number of the y ticks
    
    ax.tick_params(axis='both', which='major', pad=8)
    # Addition axis tick modifications
    
    plt.xlim((X_lim))
    plt.ylim((Y_lim))
    # Set the limits of the x and y axes in microns
    
    cmap = plt.get_cmap('hot')
    # Choose the colour bar map. Search "python colourmap options" online
    
    start=0
    stop =1
    # fractional start and stop values for offsetting the colour map extremeties
    # Default values are 0 and 1 respectively
    
    colors = cmap(np.linspace(start, stop, cmap.N))
    # Create a new colormap from those colors with adjusted offsets
    
    color_map = LinearSegmentedColormap.from_list('Upper Half',colors[::-1])
    # define the colour map from the new colour map. 
    # [::-1] reverses the colour bar map. Remove as required
    
    plt.pcolor(X, Y, Z,  cmap=color_map, vmin=0)  
    # plot a pixel map based on our new colour map settin zero as the minimum colourbar value
    
    cb = plt.colorbar(ticks=np.linspace(Cbar_lim[0], Cbar_lim[1] ,Num_Z_Ticks))# ,extend = 'max')
    # Adjust tick spacing of our colurbar. the commented "extend" option is for 
    #an extended bar arrow. See documentation for detail and uncomment as required.
    
    cb.set_label(Cbar_label , labelpad=10)
    cb.ax.tick_params(labelsize=MEDIUM_SIZE)
    # Add a colourbar label
    
    plt.clim(Cbar_lim)
    # Set the limits of the colurbar. Uncomment as required

    plt.show()
    # Show the plot
    
    return fig
    #Return the figure

##############################################################################
    """Next we have the functions for saveing the figures """


def Save_Fig_svg(Data, fig):
    """Save figure as an svg file """
    
    path = Data.Idir +'/'+ Data.File_Name +'.svg'
    #Define the path with name of the file to be saved
    
    fig.savefig(path,  bbox_inches = 'tight', dpi=600, format = 'svg')
    # Save figure with specified resolution in dpi
    
    print('Plot saved to: ' , path)
    # Output a message informing of its location
    
    
    
def Save_Fig_png(Data, fig):
    """Save figure as an png file """
    
    path = Data.Idir +'/'+ Data.File_Name +'.png'
    #Define the path with name of the file to be saved
    
    fig.savefig(path,  bbox_inches = 'tight', dpi=600, format = 'png')
    # Save figure with specified resolution in dpi
    
    print('Plot saved to: ' , path)
    # Output a message informing of its location
    
    
    
def Save_Fig_eps(Data, fig):
    """Save figure as an eps file """
    
    path = Data.Idir +'/'+ Data.File_Name +'.eps'
    #Define the path with name of the file to be saved
    
    fig.savefig(path,  bbox_inches = 'tight', dpi=600, format = 'eps')
    # Save figure with specified resolution in dpi
    
    print('Plot saved to: ' , path)
    # Output a message informing of its location