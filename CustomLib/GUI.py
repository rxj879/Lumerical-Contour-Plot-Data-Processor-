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
import wx.xrc

from CustomLib.Funcs import(LengthUnitArray, 
                            AxisLabel_Array, 
                            CbarLabel_Array, 
                            CbarManualMag_Array,
                            ExportFormat_Array,
                            Cbar_ColourMapArray,
                            Cbar_ReverseArray,
                            ExportDPI_Array)

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
    """Define the design of the gui"""
    
    def __init__( self, parent ):
        
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, 
                     title = u"Spectrum Analyser",
                     pos = wx.Point(10,10),#wx.DefaultPosition, 
                     size = wx.Size( 1000,650 ), 
                     style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

################################################################
        # Menu bar stuff
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'status msg....')
        
        menuBar.Append(fileButton, 'File')
        
        self.SetMenuBar(menuBar)
################################################################
        # panel stuff
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
       
        bSizer10 = wx.BoxSizer( wx.VERTICAL )
        gSizer10 = wx.GridSizer( 0, 5, 0, 0 )
        
        bSizer11 = wx.BoxSizer( wx.VERTICAL )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )
        bSizer13 = wx.BoxSizer( wx.VERTICAL )
        bSizer14 = wx.BoxSizer( wx.VERTICAL )
        bSizer15 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer20 = wx.BoxSizer( wx.VERTICAL )
        gSizer20 = wx.GridSizer( 0, 4, 0, 0 )
        
        bSizer21 = wx.BoxSizer( wx.VERTICAL )
        bSizer22 = wx.BoxSizer( wx.VERTICAL )
        bSizer23 = wx.BoxSizer( wx.VERTICAL )
        bSizer24 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        gSizer30 = wx.GridSizer( 0, 5, 0, 0 )
        
        bSizer31 = wx.BoxSizer( wx.VERTICAL )
        bSizer32 = wx.BoxSizer( wx.VERTICAL )
        bSizer33 = wx.BoxSizer( wx.VERTICAL )
        bSizer34 = wx.BoxSizer( wx.VERTICAL )
        bSizer35 = wx.BoxSizer( wx.VERTICAL )


        
################################################################
        
        
        self.m_staticText_FILE = wx.StaticText( self, wx.ID_ANY, u"Spectra File", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_FILE.Wrap( -1 )
                     
        self.m_textCtrl_FILE = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (350, -1), 0 )
              
        self.m_button_select_file = wx.Button( self, wx.ID_ANY, u"Select File", wx.DefaultPosition, wx.DefaultSize, 0 )
        


        self.m_staticText_ExportFormat = wx.StaticText( self, wx.ID_ANY, u"Export File Format", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ExportFormat.Wrap( -1 )
        
        ExportFormat_List = ExportFormat_Array()
        
        self.m_ComboBox_ExportFormat = wx.ComboBox(self, wx.ID_ANY, "Export File Format", wx.DefaultPosition,
                                             (150,-1), ExportFormat_List , 0)
        
        self.m_staticText_ExportDPI = wx.StaticText( self, wx.ID_ANY, u"Export Resolution", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_ExportFormat.Wrap( -1 )
        
        ExportDPI_List = ExportDPI_Array()
        
        self.m_ComboBox_ExportDPI = wx.ComboBox(self, wx.ID_ANY, "Export Res", wx.DefaultPosition,
                                             (150,-1), ExportDPI_List , 0)
        
        self.m_button_ExportFig = wx.Button( self, wx.ID_ANY, u"Export Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_button_SavePrefs = wx.Button( self, wx.ID_ANY, u"Save Prefs", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button_LoadPrefs = wx.Button( self, wx.ID_ANY, u"Load Prefs", wx.DefaultPosition, wx.DefaultSize, 0 )


        self.m_button_RestorePrefs = wx.Button( self, wx.ID_ANY, u"Restore Default Prefs", wx.DefaultPosition, wx.DefaultSize, 0 )
        


        bSizer11.Add( self.m_staticText_FILE, 0, wx.ALL, 5 )
        bSizer11.Add( self.m_textCtrl_FILE, 0, wx.ALL, 5 )
        bSizer11.Add( self.m_button_select_file, 0, wx.ALL, 5 )
        gSizer10.Add( bSizer11, 0, wx.ALL,5 )
        
        bSizer12.AddSpacer( 0)
        
        gSizer10.Add( bSizer12, 0, wx.ALL,5 )

        bSizer13.Add( self.m_staticText_ExportFormat, 0, wx.ALL, 5 )
        bSizer13.Add( self.m_ComboBox_ExportFormat, 0, wx.ALL, 5 )
        bSizer13.Add( self.m_button_ExportFig, 0, wx.ALL, 5 )
        
        gSizer10.Add( bSizer13, 0, wx.ALL,5 )
        
        bSizer14.Add( self.m_staticText_ExportDPI, 0, wx.ALL, 5 )
        bSizer14.Add( self.m_ComboBox_ExportDPI, 0, wx.ALL, 5 )
        
        gSizer10.Add( bSizer14, 0, wx.ALL,5 )
        
        bSizer15.Add( self.m_button_SavePrefs, 0, wx.ALL, 5 )
        bSizer15.Add( self.m_button_LoadPrefs, 0, wx.ALL, 5 )
        bSizer15.Add( self.m_button_RestorePrefs, 0, wx.ALL, 5 )        
        
       
        gSizer10.Add( bSizer15, 0, wx.ALL,5 )

        
        bSizer10.Add( gSizer10, 1, wx.EXPAND, 5 )
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )



        
################################################################
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )       

################################################################
        self.m_staticText_XLowLimit = wx.StaticText( self, wx.ID_ANY, u"x axis lower limit (nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_XLowLimit.Wrap( -1 )
        
        self.m_SpinCtrl_XLowLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-2000, max=2000, initial=0,  name="x axis lower limit")

        self.m_staticText_XHighLimit = wx.StaticText( self, wx.ID_ANY, u"x axis upper limit (nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_XHighLimit.Wrap( -1 )
        
        self.m_SpinCtrl_XHighLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-2000, max=2000, initial=0,  name="x axis upper limit")
        
        self.m_staticText_Num_X_Ticks = wx.StaticText( self, wx.ID_ANY, u"x axis ticks (num)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_X_Ticks.Wrap( -1 )
        
        self.m_SpinCtrl_Num_X_Ticks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=2, max=20, initial=5,  name="x axis ticks")
        
        self.m_staticText_YLowLimit = wx.StaticText( self, wx.ID_ANY, u"y axis lower limit (nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_YLowLimit.Wrap( -1 )
        
        self.m_SpinCtrl_YLowLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-2000, max=2000, initial=0,  name="y axis lower limit")

        self.m_staticText_YHighLimit = wx.StaticText( self, wx.ID_ANY, u"y axis upper limit (nm)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_YHighLimit.Wrap( -1 )
        
        self.m_SpinCtrl_YHighLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-2000, max=2000, initial=0,  name="y axis upper limit")
        
        self.m_staticText_Num_Y_Ticks = wx.StaticText( self, wx.ID_ANY, u"y axis ticks (num)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_Y_Ticks.Wrap( -1 )
        
        self.m_SpinCtrl_Num_Y_Ticks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=2, max=20, initial=5,  name="y axis ticks")
        
        
        self.m_staticText_Cbar_Lowlim = wx.StaticText( self, wx.ID_ANY, u"Colour bar lower limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_Lowlim.Wrap( -1 )
        
        self.m_SpinCtrl_CbarLowLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-1000000, max=1000000, initial=0,  name="Colour bar lower limit")

        self.m_staticText_Cbar_Highlim = wx.StaticText( self, wx.ID_ANY, u"Colour bar upper limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_Highlim.Wrap( -1 )
        
        self.m_SpinCtrl_CbarHighLimit = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-1000000, max=1000000, initial=0,  name="Colour bar upper limit")
        
        self.m_staticText_Num_Cbar_Ticks = wx.StaticText( self, wx.ID_ANY, u"Colour bar ticks (num)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Num_Cbar_Ticks.Wrap( -1 )
        
        self.m_SpinCtrl_Num_Cbar_Ticks = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=2, max=20, initial=5,  name="c bar ticks")
        
        self.m_staticText_Cbar_SkewHi = wx.StaticText( self, wx.ID_ANY, u"Colour bar High Offset (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_SkewHi.Wrap( -1 )
        
        self.m_SpinCtrl_Cbar_SkewHi = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-200, max=200, initial=100,  name="Colour bar High Offset (%)")
        
        self.m_staticText_Cbar_SkewLo = wx.StaticText( self, wx.ID_ANY, u"Colour bar Low Offset (%)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_SkewLo.Wrap( -1 )
        
        self.m_SpinCtrl_Cbar_SkewLo = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=-200, max=200, initial=0,  name="Colour bar Low Offset (%)")


        self.m_staticText_Rotate = wx.StaticText( self, wx.ID_ANY, u"Rotate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Rotate.Wrap( -1 )
        
        self.m_SpinCtrl_RotateAngle = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,  (100,-1), 
                                    wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER |wx.SP_WRAP, 
                                     min=-180, max=180, initial=0,  name="Rotate")

        self.m_CHKBox_FlipX = wx.CheckBox(self, id=wx.ID_ANY, label="Flip x", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Flip x') 
        
        self.m_CHKBox_FlipY = wx.CheckBox(self, id=wx.ID_ANY, label="Flip y", pos=wx.DefaultPosition,
                                                  size=wx.DefaultSize, style=0, validator=wx.DefaultValidator,
                                                  name='Flip y') 
        
        bSizer21.Add( self.m_staticText_XLowLimit, 0, wx.ALL, 5 )
        bSizer21.Add( self.m_SpinCtrl_XLowLimit, 0, wx.ALL, 5 )

        bSizer21.Add( self.m_staticText_YLowLimit, 0, wx.ALL, 5 )
        bSizer21.Add( self.m_SpinCtrl_YLowLimit, 0, wx.ALL, 5 )
        
        bSizer21.Add( self.m_staticText_Cbar_Lowlim, 0, wx.ALL, 5 )
        bSizer21.Add( self.m_SpinCtrl_CbarLowLimit, 0, wx.ALL, 5 )    
        
        bSizer21.Add( self.m_staticText_Cbar_SkewLo, 0, wx.ALL, 5 )
        bSizer21.Add( self.m_SpinCtrl_Cbar_SkewLo, 0, wx.ALL, 5 )   
        
        gSizer20.Add( bSizer21, 0, wx.ALL,5 )


        bSizer22.Add( self.m_staticText_XHighLimit, 0, wx.ALL, 5 )
        bSizer22.Add( self.m_SpinCtrl_XHighLimit, 0, wx.ALL, 5 )

        bSizer22.Add( self.m_staticText_YHighLimit, 0, wx.ALL, 5 )
        bSizer22.Add( self.m_SpinCtrl_YHighLimit, 0, wx.ALL, 5 )
        
        bSizer22.Add( self.m_staticText_Cbar_Highlim, 0, wx.ALL, 5 )
        bSizer22.Add( self.m_SpinCtrl_CbarHighLimit, 0, wx.ALL, 5 )

        bSizer22.Add( self.m_staticText_Cbar_SkewHi, 0, wx.ALL, 5 )
        bSizer22.Add( self.m_SpinCtrl_Cbar_SkewHi, 0, wx.ALL, 5 )  
        
        gSizer20.Add( bSizer22, 0, wx.ALL,5 )

        bSizer23.Add( self.m_staticText_Num_X_Ticks, 0, wx.ALL, 5 )
        bSizer23.Add( self.m_SpinCtrl_Num_X_Ticks, 0, wx.ALL, 5 )
        
        bSizer23.Add( self.m_staticText_Num_Y_Ticks, 0, wx.ALL, 5 )
        bSizer23.Add( self.m_SpinCtrl_Num_Y_Ticks, 0, wx.ALL, 5 )
        
        bSizer23.Add( self.m_staticText_Num_Cbar_Ticks, 0, wx.ALL, 5 )
        bSizer23.Add( self.m_SpinCtrl_Num_Cbar_Ticks, 0, wx.ALL, 5 )
        
        gSizer20.Add( bSizer23, 0, wx.ALL,5 )
        
        bSizer24.Add( self.m_staticText_Rotate, 0, wx.ALL, 5 )
        bSizer24.Add( self.m_SpinCtrl_RotateAngle , 0, wx.ALL, 5 )
        bSizer24.Add( self.m_CHKBox_FlipX , 0, wx.ALL, 5 )
        bSizer24.Add( self.m_CHKBox_FlipY , 0, wx.ALL, 5 )

        
        gSizer20.Add( bSizer24, 0, wx.ALL,5 )
        
        bSizer20.Add( gSizer20, 1, wx.EXPAND, 5 )
        bSizer1.Add( bSizer20, 1, wx.EXPAND, 5 )
################################################################
        
        self.m_staticText_Cbar_ColourMap = wx.StaticText( self, wx.ID_ANY, u"Colour bar map", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_ColourMap.Wrap( -1 )
        
        Cbar_ColourMap_List = Cbar_ColourMapArray()

        self.m_ComboBox_Cbar_ColourMap = wx.ComboBox(self, wx.ID_ANY, "Colour bar map", wx.DefaultPosition,
                                             (150,-1), Cbar_ColourMap_List, 0)
        
        self.m_staticText_Cbar_Reverse = wx.StaticText( self, wx.ID_ANY, u"Colour bar Direction", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_Reverse.Wrap( -1 )
        
        Cbar_Reverse_List = Cbar_ReverseArray()

        self.m_ComboBox_Cbar_Reverse = wx.ComboBox(self, wx.ID_ANY, "Colour bar Direction", wx.DefaultPosition,
                                             (150,-1), Cbar_Reverse_List, 0)
        
        self.m_staticText_Axis_Units = wx.StaticText( self, wx.ID_ANY, u"x and y axis units", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Axis_Units.Wrap( -1 )
        
        AxisUnits_List = LengthUnitArray()

        self.m_ComboBox_AxisUnits = wx.ComboBox(self, wx.ID_ANY, "Axis Units", wx.DefaultPosition,
                                             (150,-1), AxisUnits_List, 0)
        
        
        AxisLabel_List = AxisLabel_Array()
        
        self.m_staticText_XAxis_Label = wx.StaticText( self, wx.ID_ANY, u"x axis label", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_XAxis_Label.Wrap( -1 )

        self.m_ComboBox_x_label = wx.ComboBox(self, wx.ID_ANY, "x axis Label", wx.DefaultPosition,
                                             (150,-1), AxisLabel_List, 0)
        
        self.m_staticText_YAxis_Label = wx.StaticText( self, wx.ID_ANY, u"y axis label", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_YAxis_Label.Wrap( -1 )
        
        self.m_ComboBox_y_label = wx.ComboBox(self, wx.ID_ANY, "y axis Label", wx.DefaultPosition,
                                             (150,-1), AxisLabel_List, 0)
        
        self.m_staticText_Cbar_Label = wx.StaticText( self, wx.ID_ANY, u"Colour bar label", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_Cbar_Label.Wrap( -1 )
        
        CbarLabel_List = CbarLabel_Array()
        
        self.m_ComboBox_Cbar_Label = wx.ComboBox(self, wx.ID_ANY, "Colour bar Label", wx.DefaultPosition,
                                             (150,-1), CbarLabel_List , 0)
        
        self.m_StaticText_ManualCbar_label =  wx.StaticText( self, wx.ID_ANY, u"Manual Cbar Label", wx.DefaultPosition, wx.DefaultSize, 0 )
        
        self.m_textCtrl_ManualCbar_label  = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString , wx.DefaultPosition, (150,-1), 0 | wx.TE_PROCESS_ENTER   )

        self.m_staticText_CbarManualMag = wx.StaticText( self, wx.ID_ANY, u"Colour Bar Re-scale magnitude", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_CbarManualMag.Wrap( -1 )
        
        CbarManualMag_List = CbarManualMag_Array()
        
        self.m_ComboBox_CbarManualMag = wx.ComboBox(self, wx.ID_ANY, "Colour Bar Re-scale magnitude", wx.DefaultPosition,
                                             (150,-1), CbarManualMag_List , 0)
        
        self.m_staticText_SmallText = wx.StaticText( self, wx.ID_ANY, u"Small Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_SmallText.Wrap( -1 )
        
        self.m_SpinCtrl_SMALL_SIZE = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=100, initial=22,  name="Small Text Size")
        
        self.m_staticText_MidText = wx.StaticText( self, wx.ID_ANY, u"Medium Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_MidText.Wrap( -1 )
        
        self.m_SpinCtrl_MEDIUM_SIZE = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=100, initial=25,  name="Medium Text Size")
        
        self.m_staticText_LargeText = wx.StaticText( self, wx.ID_ANY, u"Large Text Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText_LargeText.Wrap( -1 )
        
        self.m_SpinCtrl_BIGGER_SIZE = wx.SpinCtrl(self, wx.ID_ANY, "", wx.DefaultPosition,
                                     (100,-1), wx.SP_ARROW_KEYS | wx.ALIGN_LEFT | wx.TE_PROCESS_ENTER, 
                                     min=1, max=100, initial=30,  name="Large Text Size")
        
        bSizer31.Add( self.m_staticText_Cbar_ColourMap, 0, wx.ALL, 5 )
        bSizer31.Add( self.m_ComboBox_Cbar_ColourMap, 0, wx.ALL, 5 )
        bSizer31.Add( self.m_staticText_Cbar_Reverse, 0, wx.ALL, 5 )
        bSizer31.Add( self.m_ComboBox_Cbar_Reverse, 0, wx.ALL, 5 )
        bSizer31.Add( self.m_staticText_Axis_Units, 0, wx.ALL, 5 )
        bSizer31.Add( self.m_ComboBox_AxisUnits, 0, wx.ALL, 5 )
        
        gSizer30.Add( bSizer31, 0, wx.ALL,5 )
        
        bSizer32.Add( self.m_staticText_XAxis_Label, 0, wx.ALL, 5 )
        bSizer32.Add( self.m_ComboBox_x_label, 0, wx.ALL, 5 )
        
        gSizer30.Add( bSizer32, 0, wx.ALL,5 )
        
        bSizer33.Add( self.m_staticText_YAxis_Label, 0, wx.ALL, 5 )
        bSizer33.Add( self.m_ComboBox_y_label, 0, wx.ALL, 5 )
        
        gSizer30.Add( bSizer33, 0, wx.ALL,5 )
        
        bSizer34.Add( self.m_staticText_Cbar_Label, 0, wx.ALL, 5 )
        bSizer34.Add( self.m_ComboBox_Cbar_Label, 0, wx.ALL, 5 )
        bSizer34.Add( self.m_StaticText_ManualCbar_label, 0, wx.ALL, 5 )
        bSizer34.Add( self.m_textCtrl_ManualCbar_label, 0, wx.ALL, 5 )
        bSizer34.Add( self.m_staticText_CbarManualMag, 0, wx.ALL, 5 )
        bSizer34.Add( self.m_ComboBox_CbarManualMag, 0, wx.ALL, 5 )
        
        gSizer30.Add( bSizer34, 0, wx.ALL,5 )
        
        bSizer35.Add( self.m_staticText_SmallText, 0, wx.ALL, 5 )
        bSizer35.Add( self.m_SpinCtrl_SMALL_SIZE, 0, wx.ALL, 5 )
        bSizer35.Add( self.m_staticText_MidText, 0, wx.ALL, 5 )
        bSizer35.Add( self.m_SpinCtrl_MEDIUM_SIZE, 0, wx.ALL, 5 )
        bSizer35.Add( self.m_staticText_LargeText, 0, wx.ALL, 5 )
        bSizer35.Add( self.m_SpinCtrl_BIGGER_SIZE, 0, wx.ALL, 5 )
        
        gSizer30.Add( bSizer35, 0, wx.ALL,5 )
        
        bSizer30.Add( gSizer30, 1, wx.EXPAND, 5 )
        
        bSizer1.Add( bSizer30, 1, wx.EXPAND, 5 )

################################################################
        self.SetSizer( bSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
################################################################
        # Connect Events:
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
        self.Bind( wx.EVT_CLOSE, self.Quit, exitItem)
        self.m_button_select_file.Bind( wx.EVT_BUTTON, self.OnButtonClick_select_file )
        
        self.m_SpinCtrl_XLowLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_XLowLimit )
        self.m_SpinCtrl_XLowLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_XLowLimit )
        self.m_SpinCtrl_XHighLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_XHighLimit )
        self.m_SpinCtrl_XHighLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_XHighLimit )
        self.m_SpinCtrl_Num_X_Ticks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_X_Ticks )
        self.m_SpinCtrl_Num_X_Ticks.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Num_X_Ticks )
        
        self.m_SpinCtrl_YLowLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_YLowLimit )
        self.m_SpinCtrl_YLowLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_YLowLimit )
        self.m_SpinCtrl_YHighLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_YHighLimit )
        self.m_SpinCtrl_YHighLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_YHighLimit )
        self.m_SpinCtrl_Num_Y_Ticks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_Y_Ticks )
        self.m_SpinCtrl_Num_Y_Ticks.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Num_Y_Ticks )
        
        self.m_SpinCtrl_CbarLowLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Cbar_Lowlim )
        self.m_SpinCtrl_CbarLowLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Cbar_Lowlim )
        self.m_SpinCtrl_CbarHighLimit.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Cbar_Highlim )
        self.m_SpinCtrl_CbarHighLimit.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Cbar_Highlim )
        self.m_SpinCtrl_Num_Cbar_Ticks.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Num_Cbar_Ticks )
        self.m_SpinCtrl_Num_Cbar_Ticks.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Num_Cbar_Ticks )
        
        self.m_SpinCtrl_RotateAngle.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Rotate)
        self.m_SpinCtrl_RotateAngle.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Rotate )
        self.m_CHKBox_FlipX.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_FlipX )
        self.m_CHKBox_FlipY.Bind(wx.EVT_CHECKBOX, self.On_CHKBox_FlipY )
        
        self.m_SpinCtrl_Cbar_SkewHi.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Cbar_SkewHi )
        self.m_SpinCtrl_Cbar_SkewHi.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Cbar_SkewHi )
        self.m_SpinCtrl_Cbar_SkewLo.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_Cbar_SkewLo )
        self.m_SpinCtrl_Cbar_SkewLo.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_Cbar_SkewLo )
        
        self.m_ComboBox_Cbar_ColourMap.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_Cbar_ColourMap)
        self.m_ComboBox_Cbar_Reverse.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_Reverse)
        self.m_ComboBox_AxisUnits.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_AxisUnits)
        self.m_ComboBox_x_label.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_XAxis_Label)
        self.m_ComboBox_y_label.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_YAxis_Label)
        self.m_ComboBox_Cbar_Label.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_Cbar_Label)
        
        self.m_SpinCtrl_SMALL_SIZE.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_SmallTextSize)
        self.m_SpinCtrl_SMALL_SIZE.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_SmallTextSize )
        self.m_SpinCtrl_MEDIUM_SIZE.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_MidTextSize)
        self.m_SpinCtrl_MEDIUM_SIZE.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_MidTextSize )
        self.m_SpinCtrl_BIGGER_SIZE.Bind( wx.EVT_SPINCTRL, self.OnSpinCtrl_LargeTextSize)
        self.m_SpinCtrl_BIGGER_SIZE.Bind(wx.EVT_TEXT_ENTER, self.OnSpinCtrl_LargeTextSize )
        
        self.m_textCtrl_ManualCbar_label.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl_ManualCbar)
        self.m_ComboBox_CbarManualMag.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_CbarManualMag)
        
        self.m_ComboBox_ExportFormat.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_ExportFormat)
        self.m_ComboBox_ExportDPI.Bind(wx.EVT_COMBOBOX, self.OnComboBoxSelect_ExportDPI)
        self.m_button_ExportFig.Bind( wx.EVT_BUTTON, self.OnButtonClick_ExportFig )
        self.m_button_SavePrefs.Bind( wx.EVT_BUTTON, self.OnButtonClick_SavePrefs )
        self.m_button_LoadPrefs.Bind( wx.EVT_BUTTON, self.OnButtonClick_LoadPrefs )
        self.m_button_RestorePrefs.Bind( wx.EVT_BUTTON, self.OnButtonClick_RestorePrefs )
################################################################
    # Standard Event handlers    
    def Quit(self , event):
        self.Close()
        
        
################################################################        
	# Virtual event handlers, overide them in your derived class

    def OnComboBoxSelect_ExportDPI(self, event):
        event.Skip()

    def On_CHKBox_FlipX(self, event):
        event.Skip()

    def On_CHKBox_FlipY(self, event):
        event.Skip()


    def OnButtonClick_LoadPrefs(self, event):
        event.Skip()


    def OnSpinCtrl_Rotate(self, event):
        event.Skip()

    def OnButtonClick_SavePrefs(self, event):
        event.Skip()
        
    def OnButtonClick_RestorePrefs(self, event):
        event.Skip()

    def OnSpinCtrl_LargeTextSize(self, event):
        event.Skip()

    def OnSpinCtrl_MidTextSize(self, event):
        event.Skip()
        

    def OnSpinCtrl_SmallTextSize(self, event):
        event.Skip()
        
    def OnComboBoxSelect_Reverse(self, event):
        event.Skip()
        
    def OnComboBoxSelect_Cbar_ColourMap(self, event):
        event.Skip()

    def OnButtonClick_ExportFig(self, event):
        event.Skip()
        
    def OnComboBoxSelect_ExportFormat(self, event):
        event.Skip()

    def OnComboBoxSelect_CbarManualMag(self, event):
        event.Skip()
   
    def OnComboBoxSelect_Cbar_Label(self, event):
        event.Skip()
   
    def OnTextCtrl_ManualCbar(self, event):
        event.Skip()
        
    def OnComboBoxSelect_XAxis_Label(self, event):
        event.Skip()

    def OnComboBoxSelect_YAxis_Label(self, event):
        event.Skip()
           
    def OnSpinCtrl_Cbar_SkewHi(self, event):
        event.Skip()
        
    def OnSpinCtrl_Cbar_SkewLo(self, event):
        event.Skip()
        
        
    def OnButtonClick_select_file(self, event):
        event.Skip()

    def OnSpinCtrl_XLowLimit (self, event):
        event.Skip()

    def OnSpinCtrl_XHighLimit (self, event):
        event.Skip()
        
    def OnSpinCtrl_Num_X_Ticks (self, event):
        event.Skip()
        
    def OnSpinCtrl_YLowLimit (self, event):
        event.Skip()

    def OnSpinCtrl_YHighLimit (self, event):
        event.Skip()
        
    def OnSpinCtrl_Num_Y_Ticks (self, event):
        event.Skip()
        
    def OnSpinCtrl_Cbar_Lowlim  (self, event):
        event.Skip()

    def OnSpinCtrl_Cbar_LHighlim (self, event):
        event.Skip()
        
    def OnSpinCtrl_Num_Cbar_Ticks (self, event):
        event.Skip()

    def OnComboBoxSelect_AxisUnits (self, event):
        event.Skip()