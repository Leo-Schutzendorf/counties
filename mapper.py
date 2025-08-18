import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box
import pandas as pd


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

    # Bounding box (minx, miny, maxx, maxy)
    bbox = [-176, 18.9, -66.91, 71.4]
    bbox_geom = gpd.GeoDataFrame(
        geometry=[box(*bbox)],
        crs=counties.crs
    )

    # Clip to bounding box
    counties = gpd.clip(counties, bbox_geom)

    # Create figure
    fig, ax = plt.subplots(figsize=(20, 12), dpi=150)
    counties.plot(ax=ax, color="red", edgecolor="white", linewidth=0.1)

    ax.set_title("Counties", fontsize=20)
    ax.set_axis_off()

    # Enable interactive mode & scroll zoom
    def on_scroll(event):
        base_scale = 1.2
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        xdata = event.xdata  # get event x location
        ydata = event.ydata  # get event y location
        if event.button == 'up':  # zoom in
            scale_factor = 1 / base_scale
        elif event.button == 'down':  # zoom out
            scale_factor = base_scale
        else:
            scale_factor = 1
        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])
        ax.set_xlim([xdata - new_width * (1 - relx),
                     xdata + new_width * (relx)])
        ax.set_ylim([ydata - new_height * (1 - rely),
                     ydata + new_height * (rely)])
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('scroll_event', on_scroll)

    plt.show()

displayMap()