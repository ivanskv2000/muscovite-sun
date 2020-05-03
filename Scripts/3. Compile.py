import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt # colormaps
import numpy as np
import osmnx as ox
import pickle


# Load previously created objects

M = pickle.load(open('moscow_map_el.obj', 'rb'))
colorsHEX = pickle.load(open('colorsHEX.obj', 'rb'))
widths = pickle.load(open('widths.obj', 'rb'))
month_name = pickle.load(open('month_name.obj', 'rb'))

rise_color = '#FFFE03'
set_color = '#E70074'
no_color = '#3A3F80'
bg_color = '#181A34'


# Plotting

fig, ax = ox.plot_graph(M, node_size = 0, margin = 0.035,
                        fig_height = 50, fig_width = 50, bgcolor = bg_color,
                        save = False, edge_color = colorsHEX,
                        edge_linewidth = widths, use_geom = True)

# Legend (it might be better :) )

markersize = 12
fontsize = 40

legend_elements = [Line2D([0], [0], marker = '_', color = rise_color, label = 'Sunrise watching appropriate',
                          markersize=markersize, linewidth=5),
                          
                  Line2D([0], [0], marker = '_', color = set_color, label = 'Sunset watching appropriate',
                         markersize=markersize, linewidth=5),
                  
                  Line2D([0], [0], marker = '_', color = no_color, label = 'Inappropriate for sun observation',
                         markersize=markersize, linewidth=5)
                  ]    
                      
l = ax.legend(handles = legend_elements, bbox_to_anchor = (0.0, 0.0), frameon = True, ncol = 1,
              facecolor = bg_color, framealpha = 0.9,
              loc = 'lower left',  fontsize = fontsize, prop = {'family' : 'monospace', 'size' : fontsize})

for text in l.get_texts():
    text.set_color("w")


# Save

format = 'png'

fig.savefig('Moscow.' + format, dpi = 50, bbox_inches = 'tight', 
            format = format, facecolor = fig.get_facecolor(), 
            transparent = True)