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

import CustomLib.GuiControlClass as GuiControl
# Import the custom gui control class

if __name__ == '__main__':
    app = wx.App(False)

    # Create loader frame
    frame = GuiControl.MainFrame(None)
    frame.Show()

    # Start the applications
    app.MainLoop()
