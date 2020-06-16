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

from tkinter import filedialog
from tkinter import Tk
# import the librarys for opening a user interactive file select dialogue box

import re
# import the regular expression operations library for the scientific notation

import ntpath
# import the library for handling windows paths

from math import log10, floor, ceil
import decimal
import numpy as np
# import math libraries



#####################################################################################
""" Now we define the custom functions"""

# Generate a meshgrid and rotate it by RotRad radians.
def DoRotation(xspan,yspan,  RotRad=0):
    """ Rotate the coordinate data"""

    # Clockwise, 2D rotation matrix
    RotMatrix = np.array([  [np.cos(RotRad),  np.sin(RotRad)],
                            [-np.sin(RotRad), np.cos(RotRad)]])

    # This makes two 2D arrays which are the x and y coordinates for each point.
    X, Y = np.meshgrid(xspan,yspan)

    # After rotating, I'll have another two 2D arrays with the same shapes.
    xrot , yrot = np.einsum('ji, mni -> jmn', RotMatrix, np.dstack([X, Y]))

    # Now the matrix is rotated
    return xrot, yrot



def Get_File (Idir):
    """This uses tkinter to ask for the data file"""
    
    root = Tk();
    # Creates a Tk object
    
    root.file =  filedialog.askopenfilename(initialdir = Idir, title = "Select file");
    # Opens the user file select box starting from the initial directory
    
    root.withdraw();
    # gets rid of the Tk box
    
    return root.file;
    # Returns your chosen file. Remianing local variables are wiped



def Find_Line(File , Text_Search):
    """Function to find the line number where a string appears in the file """
    
    with open(File,'r') as f:
        """Opens the file """
        
        content = f.readlines()
        # reads all lines and assigns all to content
        
    index = [x for x in range(len(content)) if Text_Search in content[x].lower()]
    # Pythonic language for searching line by line for the specificed string
    
    f.close()
    # Close the file
    
    return index
    # Returns all lines where the string appears. Remianing local variables are wiped



def Read_Line_Numbers(File , Line_Num):
    """ Function for reading the numbers that appear in a line with other strings """
    
    with open(File,'r') as f:
        """Opens the file """
        for i in range(0,Line_Num+1):
            """loops to read lines up to the point where the numbers appear"""
            
            content = f.readline()
            # reads the individual line in the extent and assigns to content
            
    Numbers = Extract_Numbers(content)
    # Gets the numbers from the last line read
    
    f.close()
    # Close the file 
    
    return Numbers
    # Returns the numbers that appeared in the specified line number.
    # Remianing local variables are wiped



def Extract_Numbers(string):
    """Function to extract the individual numbers form within a string """
    
    List = [int(s) for s in re.findall(r'\d+', string)]
    # Pythonic language for obtaining the integers that may appear in a string
    
    return List
    # Return the list of integers. Remianing local variables are wiped



def Extract_NumberData(string):
    """ Function to import data in scientific notation """
    
    scinot = re.compile('[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)')
    # Defines the scientific notation
    
    List = [float(s) for s in re.findall(scinot, string)]
    # Pythonic langauge for obtaining the data in scientific notation
    
    return List
    # Return the numeric data. Remianing local variables are wiped



def Read_Data_Section(File , Start , Extent):
    """Read data from specificied start and stop lines in a text file"""
    
    with open(File,'r') as f:
        """Opens the file """
        
        Data = []
        # Create an empty array to fill with data
        
        for i in range(0,Start+1):
            """Loops to the start of the data """
            
            content = f.readline()
            # Reads the lines up to the start
            
        for i in range(0,Extent):
            """ Loops to the extend of the data"""
            
            content = f.readline()
            # Continues to read line by line
            
            Numbers = Extract_NumberData(content)
            # Extract the numebrs in the lines
            
            Data.append(Numbers)
            # Add these numbers to the empty array

    f.close()
    # Close the file
    
    return Data
    # Returns the data. Remaining local vraibels are wiped



def path_leaf(path):
    """ Function for splitting the file path"""
    
    head, tail = ntpath.split(path)
    # Split the path into a head and a tail
    print(head)
    return head, tail.split(".")[0] 
    # Either return the split of the tail or the directory head

def round_to_sig(x, sig =2):
    """Round a number to n significant s """
    print(x)
    return round(x, sig-int(floor(log10(abs(x))))-1)
    #Return value

def floor_to_dec(x, dec = 1):
    """Round a number to n decimal places """
    return floor(x*pow(10,dec))/pow(10,dec)
    #Return value

def ceil_to_dec(x, dec = 1):
    """Round a number to n decimal places """
    return ceil(x*pow(10,dec))/pow(10,dec)
    #Return value

def DecimalPlaces(x):
    """ return the number of decimal places"""
    return int(decimal.Decimal(str(x)).as_tuple().exponent)


def AxisLimitTune(Series, XY_lim):
    if XY_lim == []:    
        """If the Y limits are unspecified"""
        
        XY_min = np.min(Series)
        XY_max = np.amax(Series)

        dec = DecimalPlaces(round_to_sig((XY_max - XY_min), sig =1))  +2

        XY_lim = [floor_to_dec(XY_min, dec ),ceil_to_dec(XY_max, dec )]
        #Retreive Y limits
        

    return XY_lim

def AxisUnitsConvert(UnitString):
    """Convert axis units"""
    switcher = {
    'nm' : 'nm',
    'microns' : '$\mu$m'
    }
    return switcher.get(UnitString, 'nm')

def LoHighConvert(limIndex):
    """ switch low to high"""
    switcher = {
    0 : 'Low',
    1 : 'High' 
    }
    return switcher.get(limIndex, 'Low')

def AxisUnitsConvertRev(UnitCode):
    """ convert axis untis"""
    switcher = {
    'nm' : 'nm',
    '$\mu$m' : 'microns' 
    }
    return switcher.get(UnitCode, 'nm')

def LengthUnitArray():
    """ defined length unit options"""
    LengthUnits = ['nm', 'microns']
    return LengthUnits

def AxisLabel_Array():
    """ axis label options"""
    AxisLabels = ["x", "y", "z"]
    return AxisLabels

def ExportDPI_Array():
    """ export dpi options"""
    ExportDPI = ["150", "200", "300", "400", "500", "600"]
    return ExportDPI

def CbarLabel_Array():
    """predefined colourbar label options"""
    CbarLabel_List = ['E-field (V/m)',
                      'E-field (mV/m)',
                      'H-field (A/m)',
                      'H-field (mA/m)']
    return CbarLabel_List 

def CbarManualMag_Array():
    """ ORder of magnitude options for the colour bar"""
    CbarManualMag = ['-9', '-6','-3','0','3','6', '9']
    return CbarManualMag

def Cbar_ColourMapArray():
    """ Coulr map options"""
    Cbar_ColourMap_List = ['nipy_spectral', 'hot', 'ocean','gist_earth', 'terrain',
                           'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 
                           'brg', 'gist_rainbow', 'rainbow', 'jet', 'gist_ncar']
    return Cbar_ColourMap_List

def Cbar_ReverseArray():
    """Colour bar reverse options"""
    Cbar_Reverse_List = ['Forward', 'Reverse']
    return Cbar_Reverse_List
    
def ExportFormat_Array():
    """ Export file format options"""
    ExportFormat_List = ['png', 'svg', 'eps', 'pdf']
    return ExportFormat_List

def RescaleAxis(X, Y, Axis_Units):
    """Function for rescaling the axes based on user input """
    
    if Axis_Units == 'mm':
        """Convert to mm """
        
        X = X / 1000.0
        # Rescale X
        
        Y = Y / 1000.0
        # Rescale Y
        
    elif Axis_Units == 'nm':
        """Convert to nm """
        
        X = X * 1000.0
        # Rescale X
        
        Y = Y * 1000.0
        # Rescale Y
        
    else:
        """ In the event of poor input, report a message """
        
        print("Axis scael options ar 'mm' or 'nm'. Leave blank for microns")
        # Print message to screen
        
    return X, Y
    # Return X and Y, wipe local variables