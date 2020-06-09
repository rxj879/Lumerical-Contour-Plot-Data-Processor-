# Lumerical-Contour-Plot-Data-Processor-
These scripts take the text output from Lumerical, a photonic simulation software, import the data and creates contour plots

This set of scripts will help those wishing to plot mode data from Lumerical.

When you export data from a lumerical monitor such as the electric field
strength in a plane it can be quite labourious to process this in standard 
plotting software as a contour plot.

---------------------
To get this working on a fresh python install:

Install packages needed do:

--> pip install -U wxPython
---------------------

1) In Lumerical, simply export the E-field or H-field data into a text format. 
2) Open the script "main.py" in your IDE such as spyder. 
3) run the program --> press select file --> then navigate dialogue window and select the file
4) Review plot and set contour plot options accordingly in the gui
5) Export plot in chosen file format

