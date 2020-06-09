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

import wx
# Import wx gui - you will need to install wx in your python distribution

import CustomLib.GUI as gui
# Import the gui

from CustomLib.Classes import ModeData
# Import my custom class for the data structure

from CustomLib.Plot import Contour_Plot
# Import the custom plot library and functions

from CustomLib.Funcs import (AxisUnitsConvert, 
                             LengthUnitArray, 
                             AxisUnitsConvertRev, 
                             AxisLabel_Array, 
                             CbarLabel_Array,
                             CbarManualMag_Array,
                             ExportFormat_Array,
                             Cbar_ColourMapArray,
                             Cbar_ReverseArray,
                             LoHighConvert)
# Import the custom functions

class MainFrame(gui.MainFrame):
    """ Custom Gui Control Class"""
    
    def __init__(self,parent):
        """Initialise Data and plot objects"""

        gui.MainFrame.__init__(self,parent)
        #Instantiate the gui
        
        self.Idir = None # r"C:\Documents";
        # The directory where the data file selector is to start from. Change as needed 
        
        self.Plot = None
        # Attribute for checking the existence of the plot
        
    def OnButtonClick_select_file(self, event):
        """ Select the data file"""
        self.Data = ModeData(self.Idir);
        # Create an object of the class "ModeData" for the structured data
        
        self.m_textCtrl_FILE.SetValue(self.Data.File_Name)
        # Set the text control box to be the file name
        
        self.Plot = Contour_Plot(self.Data)
        # instantiate a contour plot
        
        self.LoadPrefs_ThenPlot( event)
        # Load preferences from the root directory

    def MakePlot(self):
        """ Check existence of the plot object and make the plot"""
        if self.Plot != None:
            self.Plot.MakePlot()
            
    def OnButtonClick_LoadPrefs(self, event):
        """ Load the preferences from the root directory"""
        if self.Plot != None:
            self.LoadPrefs_ThenPlot(event)

    def LoadPrefs_ThenPlot(self, event):
        """ Load the preferences from the root directory"""
        self.Plot.CheckandLoad_Spectra_Prefs()
        self.MakePlot()
        # Make the plot
        self.Populate_Gui_Values(event)
        # Populate the parameters in the gui

    def OnButtonClick_SavePrefs(self, event):
        """ Save the current settings to the preferences file in the root directory"""
        if self.Plot != None:
            self.Plot.save_Plot_prefs()

    def OnButtonClick_RestorePrefs(self, event):
        """ Delete the preferences file and re-initialise the plot defaults"""
        if self.Plot != None:
            self.Plot.Delete_Plot_Prefs()
            self.Plot = Contour_Plot(self.Data)
            self.LoadPrefs_ThenPlot( event)

    def OnButtonClick_ExportFig(self, event):
        """ Export the figure taking the chosen file type"""
        if self.Plot != None:
            self.Plot.Save_Fig()

######################################
        
    def OnSpinCtrl_YLowLimit (self, event):
        """ Set the Y axis lower limit"""
        self.SetAxisLimit('Y', 0)

    def OnSpinCtrl_YHighLimit (self, event):
        """ Set the Y axis upper limit"""
        self.SetAxisLimit('Y', 1)
        
    def OnSpinCtrl_XLowLimit (self, event):
        """ Set the X axis lower limit"""
        self.SetAxisLimit('X', 0)

    def OnSpinCtrl_XHighLimit (self, event):
        """ Set the X axis upper limit"""
        self.SetAxisLimit('X', 1)
        
    def OnSpinCtrl_Cbar_Lowlim  (self, event):
        """ Set the colour bar axis lower limit"""
        self.SetAxisLimit('Cbar', 0)

    def OnSpinCtrl_Cbar_Highlim (self, event):
        """ Set the colour bar axis upper limit"""
        self.SetAxisLimit('Cbar', 1)
        
    def SetAxisLimit(self, Axis, limIndex):
        """ check plot object exisits and set an axis limit - space saver function"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            LimText = LoHighConvert(limIndex)
            self.Plot.__dict__[Axis + 
                               '_lim'][limIndex] = self.__dict__['m_SpinCtrl_' +
                                                                      Axis + LimText + 
                                                                      'Limit'].GetValue()
            self.MakePlot()
######################################
            
            
    def OnSpinCtrl_Num_Y_Ticks (self, event):
        """ set the number of Y axis ticks"""
        self.SetAxisTicks('Y')
        
    def OnSpinCtrl_Num_X_Ticks (self, event):
        """ set the number of X axis ticks"""
        self.SetAxisTicks('X')

    def OnSpinCtrl_Num_Cbar_Ticks (self, event):
        """ set the number of colour bar ticks"""
        self.SetAxisTicks('Cbar')
        
    def SetAxisTicks(self, Axis):
        """ set the number of ticks on an axis - space saver function"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            self.Plot.__dict__['Num_' + 
                               Axis + 
                               '_Ticks'] = self.__dict__['m_SpinCtrl_Num_' + 
                                                         Axis + 
                                                         '_Ticks'].GetValue()
            self.MakePlot()
######################################

    def OnSpinCtrl_Cbar_SkewHi(self, event):
        """ set the colour bar saturation level - upper limit"""
        self.Cbar_Skew( 'Hi')
        
    def OnSpinCtrl_Cbar_SkewLo(self, event):
        """ set the colour bar saturation level - lower limit"""
        self.Cbar_Skew( 'Lo')
        
    def Cbar_Skew(self, LoHi):
        """ set the colour bar saturation level - Space saver function"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            self.Plot.__dict__['Cbar_Skew' + 
                               LoHi] = self.__dict__['m_SpinCtrl_Cbar_Skew' + 
                                                         LoHi ].GetValue()
            self.MakePlot()
######################################
            
            
    def OnComboBoxSelect_XAxis_Label(self, event):
        """ set a new x axis label"""
        self.ComboBox_DirectApply('x_label')

    def OnComboBoxSelect_YAxis_Label(self, event):
        """ set a new y axis label"""
        self.ComboBox_DirectApply('y_label')
        
    def OnComboBoxSelect_Cbar_ColourMap(self, event):
        """ set a new colourmap"""
        self.ComboBox_DirectApply('Cbar_ColourMap')

    def OnComboBoxSelect_Reverse(self, event):
        """ reverse colourmap"""
        self.ComboBox_DirectApply('Cbar_Reverse')
        
    def ComboBox_DirectApply(self, SelectedParam):
        """ set the above combo box option - space saver function"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            n = self.__dict__['m_ComboBox_' + SelectedParam].GetCurrentSelection()
        
            DummyParam = self.__dict__['m_ComboBox_' +SelectedParam].GetString(n)
        
            self.Plot.__dict__[SelectedParam] = DummyParam
        
            self.MakePlot()
######################################
            
    def OnSpinCtrl_LargeTextSize(self, event):
        """ set the large font size"""
        self.Spin_DirectApply('BIGGER_SIZE')
        
    def OnSpinCtrl_MidTextSize(self, event):
        """ set the medium font size"""
        self.Spin_DirectApply('MEDIUM_SIZE')

    def OnSpinCtrl_SmallTextSize(self, event):
        """ set the small font size"""
        self.Spin_DirectApply('SMALL_SIZE')
        
    def OnSpinCtrl_Rotate(self, event):
        """ Set the rotation angle"""
        self.Spin_DirectApply('RotateAngle')
        
    def Spin_DirectApply(self, SelectedParam):
        """ Apply spin control parameters to above functions - space saver function"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            self.Plot.__dict__[SelectedParam] = self.__dict__['m_SpinCtrl_' + 
                                                              SelectedParam ].GetValue()
            self.MakePlot()
######################################
            
    def OnComboBoxSelect_AxisUnits (self, event):
        """ set axis units"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            n = self.m_ComboBox_AxisUnits.GetCurrentSelection()
            AxisUnitsString = self.m_ComboBox_AxisUnits.GetString(n)
            AxisUnits = AxisUnitsConvert(AxisUnitsString)
            self.Plot.Axis_Units = AxisUnits
            self.MakePlot()

    def OnComboBoxSelect_Cbar_Label(self, event):
        """ select colour label preset options"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            n = self.m_ComboBox_Cbar_Label.GetCurrentSelection()
            Cbar_LabelString = self.m_ComboBox_Cbar_Label.GetString(n)
            self.Plot.Cbar_label = Cbar_LabelString
            self.Plot.Cbar_lim = []
            self.MakePlot()
            self.Populate_Gui_Values(event)
        
    def OnTextCtrl_ManualCbar(self, event):
        """ apply a manual colour bar label"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            NewCbarLabel = self.m_textCtrl_ManualCbar_label.GetValue()
            self.Plot.Cbar_label = NewCbarLabel
            self.MakePlot()
        
    def OnComboBoxSelect_CbarManualMag(self, event):
        """ Apply a magnitude defined multiplication factor to the colour bar scale"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            n = self.m_ComboBox_CbarManualMag.GetCurrentSelection()
            CbarManualMag = self.m_ComboBox_CbarManualMag.GetString(n)
            self.Plot.Cbar_MagChange = int(CbarManualMag)
            self.MakePlot()

    def OnComboBoxSelect_ExportFormat(self, event):
        """ Set the export figure format"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            n = self.m_ComboBox_ExportFormat.GetCurrentSelection()
            ExportFormat = self.m_ComboBox_CbarManualMag.GetString(n)
            self.Plot.ExportFormat = ExportFormat

    def On_CHKBox_FlipX(self, event):
        """ Check box to refelct plot data in x direction"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            self.Plot.FlipX = self.m_CHKBox_FlipX.GetValue()
            self.MakePlot()

    def On_CHKBox_FlipY(self, event):
        """ check box to refect in y direction"""
        if self.Plot == None:
            self.OnButtonClick_select_file(wx.PostEvent)
        else:
            self.Plot.FlipY = self.m_CHKBox_FlipY.GetValue()
            self.MakePlot()
        
    def Populate_Gui_Values(self, event):
        """ Populate the gui control widgets with plot object parameters"""
        if self.Plot == None:
            self.OnButtonClick_select_file(event)

        self.m_SpinCtrl_XLowLimit.SetValue(self.Plot.X_lim[0])
        
        self.m_SpinCtrl_XHighLimit.SetValue(self.Plot.X_lim[1])
        
        self.m_SpinCtrl_Num_X_Ticks.SetValue(self.Plot.Num_X_Ticks)
        
        self.m_SpinCtrl_YLowLimit.SetValue(self.Plot.Y_lim[0])
        
        self.m_SpinCtrl_YHighLimit.SetValue(self.Plot.Y_lim[1])
        
        self.m_SpinCtrl_Num_Y_Ticks.SetValue(self.Plot.Num_Y_Ticks)
        
        self.m_SpinCtrl_CbarLowLimit.SetValue(self.Plot.Cbar_lim[0])
        
        self.m_SpinCtrl_CbarHighLimit.SetValue(self.Plot.Cbar_lim[1])
        
        self.m_SpinCtrl_Num_Cbar_Ticks.SetValue(self.Plot.Num_Cbar_Ticks)
        
        self.m_SpinCtrl_Cbar_SkewHi.SetValue(self.Plot.Cbar_SkewHi)
        
        self.m_SpinCtrl_Cbar_SkewLo.SetValue(self.Plot.Cbar_SkewLo)
        
        AxisUnitCode = AxisUnitsConvertRev(self.Plot.Axis_Units)
        
        AxisUnits_List = LengthUnitArray()
        
        self.m_ComboBox_AxisUnits.SetSelection(AxisUnits_List.index(AxisUnitCode))
        
        AxisLabel_List = AxisLabel_Array()
        
        self.m_ComboBox_y_label.SetSelection(AxisLabel_List.index(self.Plot.y_label))
        
        self.m_ComboBox_x_label.SetSelection(AxisLabel_List.index(self.Plot.x_label))
        
        Cbar_Label_List = CbarLabel_Array()
        
        self.m_ComboBox_Cbar_Label.SetSelection(Cbar_Label_List.index(self.Plot.Cbar_label))
        
        self.m_textCtrl_ManualCbar_label.SetValue(self.Plot.Cbar_label)
        
        CbarManualMag_List = CbarManualMag_Array()
        
        self.m_ComboBox_CbarManualMag.SetSelection(CbarManualMag_List.index(str(self.Plot.Cbar_MagChange)))
        
        ExportFormat_List = ExportFormat_Array()

        self.m_ComboBox_ExportFormat.SetSelection(ExportFormat_List.index(self.Plot.ExportFormat))
        
        Cbar_ColourMap_List = Cbar_ColourMapArray()
        
        self.m_ComboBox_Cbar_ColourMap.SetSelection(Cbar_ColourMap_List.index(self.Plot.Cbar_ColourMap))

        Cbar_Reverse_List = Cbar_ReverseArray()
        
        self.m_ComboBox_Cbar_Reverse.SetSelection( Cbar_Reverse_List.index(self.Plot.Cbar_Reverse))
        
        self.m_SpinCtrl_SMALL_SIZE.SetValue(self.Plot.SMALL_SIZE)
        
        self.m_SpinCtrl_MEDIUM_SIZE.SetValue(self.Plot.MEDIUM_SIZE)
        
        self.m_SpinCtrl_BIGGER_SIZE.SetValue(self.Plot.BIGGER_SIZE)
        
        self.m_SpinCtrl_RotateAngle.SetValue(self.Plot.RotateAngle)
        
        self.m_CHKBox_FlipX.SetValue(self.Plot.FlipX) 
        
        self.m_CHKBox_FlipY.SetValue(self.Plot.FlipY) 
        