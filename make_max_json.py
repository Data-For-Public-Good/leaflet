'''
The way the current leaflet map is written, we need access to the maximum values in each column
of the geojson.  I was having a really hard time doing this in javascript because I'm still
new to the language, so I decided to do it in python, save it as a json, and load it into
javascript.  Obviously this is not ideal, the main problem is that we will have to remember to update
the dictionary whenever we make changes to the geojsons, but for now it's all I got.
'''

import json
import pandas as pd 
import geopandas as gpd 

maxValueDict = {year:{} for year in map(str, range(2005, 2016))}

for year in maxValueDict.keys():
    filename = 'geojsons/zip_' + year + '.geojson'
    df = gpd.read_file(filename)
    for column_name in df.columns:
        if column_name != 'geometry':
            maxValueDict[year][column_name] = int(df[column_name].max())

with open('geojsons/maxValueDict.geojson', 'w') as outfile:
    json.dump(maxValueDict, outfile)