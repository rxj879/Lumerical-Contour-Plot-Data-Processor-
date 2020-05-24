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
import numpy as np
# import the mathematical library

import sys
# import a sys library for  program exit function

from Funcs import Get_File, Find_Line , Read_Line_Numbers, Read_Data_Section, path_leaf
# Import my custom functions from the Funcs .py file


class ModeData:
    """This class defines a data set of electric field strength (or other
    scalar quantity) in a 2D plane"""
    
    def __init__(self,Idir): 
        """Here we initialise the object with attributes"""
        
        self.File  = Get_File (Idir); 
        # Gets the file with a dialogue box set to start from the initial directory
        
        self.Idir, self.File_Name = path_leaf(self.File)
        # Makes the initial directory a class/objet attribute &
        # Sets the File name as an object attribute
        
        self.X_Data_StartSearch = ['x(microns)', 'y(microns)', 'z(microns)'];
        # This is the line to look for when importing the coordinates
        
        self.X_Data_StartSearch_Aux = ['x(m)', 'y(m)', 'z(m)'];
        # Auxilliary set of key words to look for if the coordinates are in meters
        
        self.X_Data = self.Retrieve_All_Coords()    
        # Collects the cordiantes as an object attribute
        
        self.Plane = self.Get_Grid_Size()
        # Finds out the size of the gridded scalar data and set it as an attirbute
        
        Plane_Data_StartSearch =  self.Gen_Plane_Search_String() 
        # Creates the string which should exist in the first line of the scalar gridded data
        
        self.Plane_Data = np.array(self.Get_Plane_Data(Plane_Data_StartSearch))
        # Collects the scalar data in the plane
        
###############################################################################################        
    """Now we define the member functions of this class"""
        
    def Get_Numeric_Data(self, index):
        """Collects a collumn of numeric data from a start line with a specific string"""
        
        Line_Num_List = Find_Line(self.File , self.X_Data_StartSearch[index]);
        # Finds the line with the specificed string to start collecting data from

        Scale_Factor = 1.0;
        # Local variable = 1 for data in microns
        
        if len(Line_Num_List)==0:
            """This test determins if there has been no string found. It most likely
            means that the data is in meters so the Auilliary string must
            be searched for"""

            Line_Num_List = Find_Line(self.File , self.X_Data_StartSearch_Aux[index]);
            # Finds the line with the specificed auxilliary string to start collecting data from
            
            Scale_Factor = 1.0e6;
            # Local variable = 1e6 for data in meters to convert to microns
            
        if len(Line_Num_List)>0:
            """This tests if there has been lines found with the specificed string """
            
            Line_Num = Line_Num_List[0]
            # Takes the first instance where the string was found
            
            D_Data_StartLine_Numbers = Read_Line_Numbers(self.File , Line_Num);
            # Finds the numbers in the start line so we know how many numbers to read
            
            D_Data = Read_Data_Section(self.File , Line_Num, D_Data_StartLine_Numbers[0])
            # Sets the numbers in an array to this variable
            
        else:
            """If this fails then output a message to screen"""
            
            print ("No lines with the string: ", self.X_Data_StartSearch[index], "- appear in the data file")
            # Print message to screen
            
            D_Data =[]
            # Sets an empty array as scalar
            
        D_Data = [[x * Scale_Factor for x  in y] for y in D_Data]
        # Pythonic langauge for multiplying an array by a float: unit conversion
        
        return D_Data
        # Return the Data. remaining local variables are hence wiped
    
    
    
    def Get_Plane_Data(self, Heading_Part):
        """This function obtains the scalar data in the 2D grid"""
        
        Line_Num_List = Find_Line(self.File , Heading_Part);
        # Find the line where the specified string appear: first line of the plane data
        
        if len(Line_Num_List)>0:
            """This tests if there has been lines found with the specificed string """
            
            Line_Num = Line_Num_List[0]
            # Takes the first instance where the string was found
            
            D_Data_StartLine_Numbers = Read_Line_Numbers(self.File , Line_Num);
            # Reads the numbers in the first line to determin the grid dimensions
            
            D_Data = Read_Data_Section(self.File , Line_Num, self.Plane[0])
            # Sets the numbers in an array to this variable
            
        else:
            """If this fails then output a message to screen"""
            
            print ("Failed to find lines for the scalar data")
            # Print message to screen
            
            sys.exit();
            # Ends program if this test fails 
            
        return D_Data
        # Return the Data. remaining local variables are hence wiped
        
    
    
    def Get_Grid_Size(self):
        """Simple function which determines the grid dimensions of the 2D data"""
        
        Grid = [len(self.X_Data[0]) , len(self.X_Data[1])]
        # A 2 Number array of the grid dimensions
        
        Plane = np.trim_zeros(Grid)
        # Get rid of spurious zeros
        
        return Plane;
        # Return the grid size. remaining local variables are hence wiped
        
    
    
    def Gen_Plane_Search_String(self):
        """Generates a string based on the size of the grid to search for 
        when looking for the plane data """
        
        string = str(tuple(self.Plane))
        # Creates a string from the grid size surrounded by brackets
        
        string = string.replace(" ", "")
        # removes spaces from the tuple
        
        return string
        # Returns the string to search fo when importing the plane scalar data
    
    
        
    def Retrieve_All_Coords(self):
        """Function to get the coordinate data """
        
        X_Data = []
        # Create an empty array for the data
        
        for i in range(len(self.X_Data_StartSearch)):
            """loop from 0 to length of the coordinate dimentions """
            
            Coords = self.Get_Numeric_Data(i)
            # Calls the function to import the coordinates passing i as an input
            
            if len(Coords)>0:
                """Tests if we obtained coordinate data """
                
                X_Data.append(np.array(Coords)[:,0])
                # Appends that coordinate data to the emptry array
                
        return X_Data
        # Return the coordinates. Remaining variables are wiped
