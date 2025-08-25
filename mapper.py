import geopandas as gpd
import folium
import mapclassify
from matplotlib import pyplot as plt
from shapely.geometry import box
import pandas as pd
import mplcursors
import numpy as np


def readdata():
    ageSexData = pd.read_csv('C:/Users/leoth/PycharmProjects/PythonProject/ageSexData.csv')
    population= ageSexData.POPESTIMATE
    men = ageSexData.POPEST_MALE
    women = ageSexData.POPEST_FEM

    youngAdults = ageSexData.AGE1824_TOT
    averageAge = ageSexData.AGE2544_TOT
    olderAdults = ageSexData.AGE4564_TOT
    oldest = ageSexData.AGE65PLUS_TOT

    print(population)
def displayMap():
    # Load shapefile
    counties = gpd.read_file("C:/Users/leoth/PycharmProjects/PythonProject/cb_2022_us_county_500k.shp")
    counties.head()
    mymap=counties.explore("NAMELSAD")
    mymap.save('map.html')
displayMap()