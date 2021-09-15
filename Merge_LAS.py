#!/usr/bin/env python3
__author__ = 'Gerry Gabrisch/Shuksan Geomatics'
__date__ = 'August 2021'
__copyright__ = '2021, Gerry Gabrisch'

import sys
import traceback
#import pylas
import laspy
import os
try:
    print('Running LAZ_to_LAS.py')
    
    out_las = '/home/gerry/all_points.las'
    inDir = '/home/gerry/lidarcloud/'    
    
    def append_to_las(in_laz, out_las):
        with laspy.open(out_las, mode='a') as outlas:
            with laspy.open(in_las) as inlas:
                for points in inlas.chunk_iterator(2_000_000):
                    outlas.append_points(points)
        
    
    for (dirpath, dirnames, filenames) in os.walk(inDir):
        for inFile in filenames:
            if inFile.endswith('.las'):
                in_las = os.path.join(dirpath, inFile)
                append_to_las(in_las, out_las)
        
    
   
    
    
   
    
       
       
                             
    print('Finished without errors - merge_LAS.py')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print('Error in read_xmp.py')
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1]))    