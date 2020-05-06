# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:11:27 2020

@author: rrj21
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

import sys
#import sys for exit function

#####################################################################################
""" Now we define the custom functions"""

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
    return int(decimal.Decimal(str(x)).as_tuple().exponent)


def AxisLimitTune(Series, XY_lim, XY_tick_spacing):
    if XY_lim == []:    
        """If the Y limits are unspecified"""
        
        XY_min = np.min(Series)
        XY_max = np.amax(Series)

        dec = DecimalPlaces(round_to_sig((XY_max - XY_min), sig =1))  +2

        XY_lim = [floor_to_dec(XY_min, dec ),ceil_to_dec(XY_max, dec )]
        #Retreive Y limits
        
    elif len(XY_lim) != 2 or isinstance(XY_lim, list)==False:
        """If the input limits are not in correct format """
        
        print("Limits must be input in [min,max] format")
        # print an error message to screen
        
        sys.exit()
        #Exit program on failure
    
    Num_XY_Ticks = int(round_to_sig((XY_lim[1] - XY_lim[0])/XY_tick_spacing)+1)
    
    return XY_lim, Num_XY_Ticks


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