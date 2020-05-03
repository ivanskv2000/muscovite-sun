# Python Raw Scripts

Python scripts in this folder enable you to compile a street network map based on sunrise and sunset bearings.
You can customize the appearance of map by changing defined variables, such as edge colors and widths.
You can even built a map of another location, but in this case **a new set of sun data** is required!
More detailed process of map compilation is described in `muscovite_sun.ipynb`.

# 1st script
`1. Load.py` loads multidigraph-class map with a set of additional properties (including elevation, which is retrieved
using [elevation](https://]elevation-api.io) API). `latitude`, `longitude` and `distance` parameters define center and
radius characteristics of the map.

# 2nd script
`2. Process.py` unpacks graph object and processes it in order to get color and width vectors. They are based on sun
bearings that change month by month.

# 3rd script
`3. Compile.py` builds the final map (including legend) based on previous steps.
