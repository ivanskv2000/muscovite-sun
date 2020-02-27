import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt # colormaps
import numpy as np
import osmnx as ox


# Load previously created objects

M = pickle.load(open('moscow_map_el.obj', 'rb'))
colorHEX = pickle.load(open('colorHEX.obj', 'rb'))
widths = pickle.load(open('widths.obj', 'rb'))
month_name = pickle.load(open('month_name.obj', 'rb'))

# Map center

latitude = 55.7518
longitude = 37.6224

# Plotting

fig, ax = ox.plot_graph(M, node_size=0, margin = 0.035,
                        fig_height=50, fig_width=50, bgcolor = bg_color,
                        save = False, edge_color=colorsHEX,
                        edge_linewidth=widths, use_geom = True)

# Legend
