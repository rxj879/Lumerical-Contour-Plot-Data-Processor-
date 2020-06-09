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

1) Simply export the data into a text format. 
2) Open the script "main.py" in your IDE such as spyder. 
3) set the initial path 'Idir' to a conveinient string if desired
4) run the program, then navigate dialogue window and select the file
5) Review plot and set contour plot options accordingly in "main.py" and "Plot.py" files
6) Comment/Uncomment the save plot functions in the "main.py" file
7) rerun program
