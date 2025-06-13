# LAS_tools

### Scripts to batch process LAZ and LAS files
These tools are meant to be executed from a Python IDE that points to the Python installation for ArcGIS Pro (or in a Python window in ArcGIS Pro after editing paths).
These tools require the laspy library available here:  https://pypi.org/project/laspy/

#### Merge_LAS 
Takes all of the LAS files in a directory and appends them to an existing LAS file.  Take one of the existing LAS files in your directory of LAS files and move it to a new directory, append all the remaining files to that moved LAS.

#### LAZ_to_LAS
Batch converts all of the LAZ files in a directory to LAS files.

####  Batch_las_to_raster
Converts all of the LAS files in a directory to geoTiffs in another directory.  The tool has a **kwargs input where you can change the output geotiff from intensity, first return last return...as detailed in ESRI tool description.

##### Some tools require laspy available via pip and gdal python bindings. Laspy can be installed with pip and conda but you will need a cloned arcpy environment to install that library.  
