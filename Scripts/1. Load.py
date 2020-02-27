import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt # colormaps
import numpy as np
import pickle
import osmnx as ox
import requests



lat = 55.7518
long = 37.6224
distance = 2600
elevation_api = 'dpdc1bp92p4d1VgcMg-uvifid514-t'

# Raw map

M = ox.geo_utils.add_edge_bearings(
    ox.graph_from_point((lat, long), distance=distance, network_type='drive'))

# Add elevation & edge grades

for node in M.nodes():
    y = M.nodes[node]['y'] # latitude
    x = M.nodes[node]['x'] # longitude
    response = requests.get('https://elevation-api.io/api/elevation?points=(' +
                           str(y) + ',' + str(x) + ')&key=' + elevation_api)
    if response:
        elevation = response.json()['elevations'][0]['elevation']
        M.node[node]['elevation'] = elevation
    else:
        M.node[node]['elevation'] = -9999
        print('No response!')

M = ox.elevation.add_edge_grades(M, add_absolute=True)

# Save as pickle

pickle.dump(M, open('moscow_map_el.obj', 'wb'))
