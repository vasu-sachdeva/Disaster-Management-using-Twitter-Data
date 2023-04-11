import gmaps
import gmaps.datasets
import gmaps.geojson_geometries
import json

# Read the latitude and longitude coordinates from your text file
with open("C://Users//20UCS005//Desktop//BTP//LNEx//_Data//coordinates.txt") as f:
    coordinates = [tuple(map(float, line.split())) for line in f]

# coordinates = [(13.34,78.53)]

# Create a map with the coordinates as markers
gmaps.configure(api_key='AIzaSyCYb3NMnEBF6At3FycLpq2jQhAT1T4-97A')
fig = gmaps.figure()
markers = gmaps.marker_layer(coordinates)
fig.add_layer(markers)

from ipywidgets.embed import embed_minimal_html
embed_minimal_html('export.html', views=[fig])