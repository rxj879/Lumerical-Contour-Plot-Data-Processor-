# -*- coding: utf-8 -*-
"""
   Copyright 2020 DR ROBIN RAFFE PRYCE JONES
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import matplotlib.pyplot as plt
# import the matplotlib library


from matplotlib.colors import LinearSegmentedColormap
# Import the colour map options

from CustomLib.Funcs import  AxisLimitTune, RescaleAxis, DoRotation
# Import axis limit tuning algorithm from Funcs

import numpy as np
# Import the mathematical library

import pickle

import os

class Contour_Plot:
    """Here we make the plot"""
        
    def __init__(self, Mode_Data):
            
        self.Mode_Data = Mode_Data
        
        self.RotateAngle = 0
        
        self.FlipX = False
        
        self.FlipY = False
            
        self.X_lim = []
        
        self.Y_lim = []
        
        self.X_lim2Plot = []
        
        self.Y_lim2Plot = []
            
        self.x_label = "x"
            
        self.y_label = "y"
        
        self.Num_Y_Ticks = 5
            
        self.Num_X_Ticks = 5
            
        self.Num_Cbar_Ticks= 5
        
        self.Cbar_ColourMap = 'nipy_spectral'
        
        self.Cbar_Reverse ='Reverse'
            
        self.Cbar_lim = [] 
        
        self.Axis_Units = 'nm' #'$\mu$m'
        
        self.Cbar_label = 'E-field (V/m)'
            
        self.Cbar_MagChange = 0
            
        self.ExtendCBarOption = 'neither'
            
        self.Cbar_SkewHi = 100
            
        self.Cbar_SkewLo = 0
            
        self.ExportFormat = 'png'
            
        self.SMALL_SIZE  = 22
        self.MEDIUM_SIZE = 25
        self.BIGGER_SIZE = 30
        # Define three font sizes
        
        self.ExportDPI = 300
    

            
    def MakePlot(self):
            
        self.fig = plt.figure(figsize = (12,5))
        # Create a blank figure with the specificed width and height
        
        plt.rcParams['font.family'] = "sans-serif"
        # Set The font. See following lines for options
        """ Font options: [ 'serif' | 'sans-serif' | 'cursive' | 'fantasy' | 'monospace' ]"""
    
    
        plt.rc('font', size=self.BIGGER_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=self.MEDIUM_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=self.BIGGER_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=self.SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=self.SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=self.MEDIUM_SIZE)    # legend fontsize
        plt.rc('figure', titlesize=self.BIGGER_SIZE)  # fontsize of the figure title
        # Asign font sizes to figure texts
            
        left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
        # fractions of the figure width and height
    
        ax = self.fig.add_axes([left, bottom, width, height])
        # Adds the axes at the specificed locations to give the margin sizes
    

        
        if self.RotateAngle !=0:
            Rotate_Rads = self.RotateAngle* np.pi/180
        
            X, Y = DoRotation(self.Mode_Data.X_Data[0], self.Mode_Data.X_Data[1], RotRad=Rotate_Rads)
            
        else:
            X, Y = np.meshgrid(self.Mode_Data.X_Data[0], self.Mode_Data.X_Data[1])
        # Create the coordinate grid based on the coordinate data
            
        if self.FlipX:
            X = -1.0*X
            
        if self.FlipY:
            Y = -1.0*Y
    
        if self.Axis_Units != '$\mu$m':
            """ Test for a user input on the axes scale"""
        
            X, Y = RescaleAxis(X, Y, self.Axis_Units)
            # Rescale X and Y accord to the user input
            

    
        Z = np.transpose(self.Mode_Data.Plane_Data)
        # transpose gridded the scalar data to fit the coordinate grid data
            
        if self.Cbar_label == 'E-field (mV/m)' or self.Cbar_label == 'H-field (mA/m)':
                
            self.Cbar_MagChange = 3
            
        Z = pow(10, self.Cbar_MagChange)*Z
            

        self.X_lim  =  AxisLimitTune(X, self.X_lim)
            
        self.Y_lim  =  AxisLimitTune(Y, self.Y_lim)
    
        if self.Axis_Units == '$\mu$m':
            self.X_lim2Plot = [i /1000.0 for i in self.X_lim]
        
            self.Y_lim2Plot = [i /1000.0 for i in self.Y_lim]
            
        elif self.Axis_Units == 'nm':
            self.X_lim2Plot =  self.X_lim
        
            self.Y_lim2Plot =  self.Y_lim
    
        self.Cbar_lim=  AxisLimitTune(Z, self.Cbar_lim)
    
        plt.gca().set_aspect('equal', adjustable='box')
        # Sets the aspect ratio of the x and y axis to be equal - no scale scew
       
        ax.tick_params(direction='out', length=6, width=2, colors='k',
                           grid_color='k', grid_alpha=0.5)
        # modify the axis ticks
    
        plt.rcParams['axes.linewidth'] = 2 
        #set the value of the figure linwidth globally

        ax.set_xlabel(self.x_label + " ("+self.Axis_Units+")")
        # Set label of the x-axis
    
        plt.xticks(np.linspace(self.X_lim2Plot[0],self.X_lim2Plot[1],self.Num_X_Ticks))
        # Set the minimum, maximum and number of the x ticks
    
        ax.set_ylabel(self.y_label + " ("+self.Axis_Units+")", labelpad = 3)
        # Set the label of the y-axis and add some space between it and the axis
    
        plt.yticks(np.linspace(self.Y_lim2Plot[0],self.Y_lim2Plot[1],self.Num_Y_Ticks))
        # Set the minimum, maximum and number of the y ticks
    
        ax.tick_params(axis='both', which='major', pad=8)
        # Addition axis tick modifications
    
        plt.xlim((self.X_lim2Plot))
        plt.ylim((self.Y_lim2Plot))
        # Set the limits of the x and y axes in 
    
        cmap = plt.get_cmap(self.Cbar_ColourMap )
        # Choose the colour bar map. Search "python colourmap options" online
    
        start= (self.Cbar_SkewHi - 100.0)/100.0
        stop = (self.Cbar_SkewLo + 100.0)/100.0
            
 
        # fractional start and stop values for offsetting the colour map extremeties
        # Default values are 0 and 1 respectively


        colors = cmap(np.linspace(start, stop, cmap.N))
        # Create a new colormap from those colors with adjusted offsets
        if self.Cbar_Reverse == 'Forward':
            color_map = LinearSegmentedColormap.from_list('Upper Half',colors)
            
        elif self.Cbar_Reverse == 'Reverse':
            color_map = LinearSegmentedColormap.from_list('Upper Half',colors[::-1])
        # define the colour map from the new colour map. 
        # [::-1] reverses the colour bar map. Remove as required
    
        plt.pcolor(X, Y, Z,  cmap=color_map, vmin=0)  
        # plot a pixel map based on our new colour map settin zero as the minimum colourbar value
    
    
        cb = plt.colorbar(ticks=np.linspace(self.Cbar_lim[0], 
                                                self.Cbar_lim[1] ,
                                                self.Num_Cbar_Ticks) ,extend = self.ExtendCBarOption)
    

        # Adjust tick spacing of our colurbar. the commented "extend" option is for 
        #an extended bar arrow. See documentation for detail and uncomment as required.
    
        cb.set_label(self.Cbar_label , labelpad=10)
        cb.ax.tick_params(labelsize=self.MEDIUM_SIZE)
        # Add a colourbar label
    
        plt.clim(self.Cbar_lim)
        # Set the limits of the colurbar. Uncomment as required

        plt.show()
        # Show the plot
    


##############################################################################
    """Next we have the functions for saveing the figures """


    def Save_Fig(self):
        """Save figure as an svg file """
    
        path = self.Mode_Data.Idir +'/'+ self.Mode_Data.File_Name +'.' + self.ExportFormat
        #Define the path with name of the file to be saved
    
        self.fig.savefig(path,  bbox_inches = 'tight', dpi=self.ExportDPI, format = self.ExportFormat)
        # Save figure with specified resolution in dpi
    
        print('Plot saved to: ' , path)
        # Output a message informing of its location
    
    def save_Plot_prefs(self):
        

        print("Saving Plot preferences...")
        File = "Plot_prefs.pickle"
        pickle.dump([self.X_lim,
                     self.Y_lim ,
                     self.X_lim2Plot,
                     self.Y_lim2Plot,
                     self.x_label ,
                     self.y_label ,
                     self.Num_Y_Ticks,
                     self.Num_X_Ticks,
                     self.Num_Cbar_Ticks,
                     self.Cbar_ColourMap ,
                     self.Cbar_Reverse ,
                     self.Cbar_lim ,
                     self.Axis_Units ,
                     self.Cbar_label,
                     self.Cbar_MagChange,
                     self.ExtendCBarOption,
                     self.Cbar_SkewHi ,
                     self.Cbar_SkewLo ,
                     self.ExportFormat ,
                     self.SMALL_SIZE ,
                     self.MEDIUM_SIZE,
                     self.BIGGER_SIZE,
                     self.ExportDPI], open(File, "wb"))

        print("Plot preferences saved.")
                

    def load_Plot_prefs(self):

        print("Loading preferences...")
        File = "Plot_prefs.pickle"
        (self.X_lim,
         self.Y_lim ,
         self.X_lim2Plot,
         self.Y_lim2Plot,
         self.x_label ,
         self.y_label ,
         self.Num_Y_Ticks,
         self.Num_X_Ticks,
         self.Num_Cbar_Ticks,
         self.Cbar_ColourMap ,
         self.Cbar_Reverse ,
         self.Cbar_lim ,
         self.Axis_Units ,
         self.Cbar_label,
         self.Cbar_MagChange,
         self.ExtendCBarOption,
         self.Cbar_SkewHi ,
         self.Cbar_SkewLo ,
         self.ExportFormat ,
         self.SMALL_SIZE ,
         self.MEDIUM_SIZE,
         self.BIGGER_SIZE,
         self.ExportDPI)= pickle.load(open(File, "rb"))

    def CheckandLoad_Spectra_Prefs(self):
        try:
            print("Loading preferences...")
            self.load_Plot_prefs()
        except (OSError, IOError):
            print("No preferences file found. Creating one...")
            self.save_Plot_prefs()
            
    def Delete_Plot_Prefs(self):
        File = "Plot_prefs.pickle"
        os.remove(File)