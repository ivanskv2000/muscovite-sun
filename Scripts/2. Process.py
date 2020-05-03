import networkx as nx
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt # colormaps
import numpy as np
import pickle
import osmnx as ox
import requests
from colormap import rgb2hex, hex2rgb
import calendar
import astral
from astral.sun import sun
from astral.sun import azimuth
from datetime import datetime
import pytz



month_num = 12

rise_color = '#FFFE03' # yellow
set_color = '#E70074'  # magenta
no_color = '#3A3F80'   # blue
bg_color = '#181A34'   # dark blue


# Load map

M = pickle.load(open('moscow_map_el.obj', 'rb'))


# Load month data

l = astral.LocationInfo()    # location initialization
l.name = 'Moscow'            # city name
l.region = 'Russia'          # region
l.timezone = 'Europe/Moscow' # timezone (pytz style)
l.latitude = lat             # latitude
l.longitude = long           # longitude

date_str = str(datetime.now().year) + '-' + str(month_num) + '-' + '15' # set date (based on month)
date_obj = datetime.strptime(date_str, '%Y-%m-%d') # convert to datetime object
s = sun(l.observer, date = date_obj) # get dictionary with solar time data

rise_time_obj = s['sunrise'].astimezone(tz = pytz.timezone(l.timezone))
set_time_obj = s['sunset'].astimezone(tz = pytz.timezone(l.timezone))

rise_time = datetime.strftime(rise_time_obj, '%H:%M:%S')
set_time = datetime.strftime(set_time_obj, '%H:%M:%S')

rise_angle = azimuth(l.observer, rise_time_obj)
set_angle = azimuth(l.observer, set_time_obj)

month_name = calendar.month_name[month_num]


# Unpack

u = []
v = []
data = []
for uu, vv, ddata in M.edges(data=True):
    u.append(uu)
    v.append(vv)
    data.append(ddata)

for item in data:
    if 'bearing' in item.keys():
        item['bearing'] = float(item['bearing'])


# Process (set attributes)

colorsHEX = [] # color vector

for item in data:
    if item['length'] > 10:
        if abs(item['bearing'] - rise_angle) <= 10 or abs(item['bearing'] - rise_angle - 180) <= 10:
            colorHEX = rise_color
        elif abs(item['bearing'] - set_angle) <= 10 or abs(item['bearing'] - set_angle + 180) <= 10:
            colorHEX = set_color
        else:
            colorHEX = no_color
    else:
        colorHEX = bg_color
    colorsHEX.append(colorHEX)

widths = [] # width vector

for item in data:
    if 'primary' or 'primary_link' in item['highway']:
        width = 5
    elif 'secondary' or 'secondary_link' in item['highway']:
        width = 3
    elif 'tertiary' or 'tertiary_link' in item['highway']:
        width = 2
    elif 'residential' or 'living_street' in item['highway']:
        width = 1
    else:
        width = 0
    widths.append(width)


# Save as pickle

pickle.dump(colorsHEX, open('colorsHEX.obj', 'wb'))
pickle.dump(widths, open('widths.obj', 'wb'))
pickle.dump(month_name, open('month_name.obj', 'wb'))
