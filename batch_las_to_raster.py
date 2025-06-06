#!/usr/bin/env python3
'''Converts all las files in a directory to a geotiff.  
Change kwargs for parameter changes...'''

__author__ = 'Gerry Gabrisch/Lummi GIS Division'
__date__ = 'May 2021'
__copyright__ = '(C) 2021, Lummi Indian Business Council'
__license__ = "MIT"
__version__ = "1.0"
__email__ = "geraldg@lummi-nsn.gov"
__status__ = "Production"

import sys
import traceback
import os
import arcpy
arcpy.env.overwriteOutput = True
#save time - don't build pyramids...
arcpy.env.pyramid = "NONE"


try:
    #The input directory of las
    in_dir = r"C:\gTemp\las2024acme"
    #the directory to store the geotiffs
    out_dir = r"C:\gTemp\las"
    
    
    def file_name(file, out_dir):
        '''build the new file path and name'''
        file_list = file.split("\\")
        file_name = file_list[-1]
        file_name = file_name.split(".")[0]
        out_file = file_name+ '.tif'
        out_file =  os.path.join(out_dir, out_file)
        return out_file
    

    for root, dirs, files in os.walk(in_dir):
        for file in files:
            if(file.endswith(".las")):
                out_file = file_name(file, out_dir)
                in_las = os.path.join(root, file)
               
                print('Working on: ',in_las)
                kwargs = {'value_field': 'INTENSITY', 'data_type': 'FLOAT', 'sampling_type': 'CELLSIZE', 'sampling_value':0.5, 'z_factor':1}
                arcpy.conversion.LasDatasetToRaster(in_las, out_file, **kwargs)    
  

except arcpy.ExecuteError: 
    # Get the tool error messages 
    msgs = arcpy.GetMessages(2) 

    # Return tool error messages for use with a script tool 
    arcpy.AddError(msgs) 

    # Print tool error messages for use in Python
    print(msgs)

except:
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    # Return Python error messages for use in script tool or Python window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python window
    print(pymsg)
    print(msgs)
