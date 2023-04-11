# pip install gmaps
import gmaps
import gmaps.datasets
from IPython.display import display

# Read the latitude and longitude coordinates from your text file
with open('coordinates.txt') as f:
    coordinates = [tuple(map(float, line.split())) for line in f]

# Create a map with the coordinates as markers
gmaps.configure(api_key='API_KEY')
fig = gmaps.figure()
markers = gmaps.marker_layer(coordinates)
fig.add_layer(markers)
display(fig)
