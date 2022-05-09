import json
from folium import Map
from folium.plugins import HeatMap
from html2image import Html2Image
import requests
import dash_leaflet as dl
import gmaps
import numpy as np

# def elevation(lat, lng):
#     apikey = "AIzaSyBHPjDQ-HkbJ6QBvG44wTFr5Q5MEkudnJA"
#     url = "https://maps.googleapis.com/maps/api/elevation/json"
#     request = requests.get(url + "?locations=" + str(lat) + "," + str(lng) + "&key=" + apikey)
#     try:
#         results = json.loads(request.text).get('results')
#         if 0 < len(results):
#             elevation = results[0].get('elevation')
#             # resolution = results[0].get('resolution') # for RESOLUTION
#             # ELEVATION
#             return elevation
#         else:
#             print('HTTP GET Request failed.')
#     except ValueError as e:
#         print('JSON decode failed: ' + str(request) + str(e))
#
# print(elevation(-0.6455571, -90.28158))

# Google maps
# api_key = "AIzaSyBHPjDQ-HkbJ6QBvG44wTFr5Q5MEkudnJA"
# gmaps.configure(api_key="AIzaSyBHPjDQ-HkbJ6QBvG44wTFr5Q5MEkudnJA")

# Folium
# initial_map = Map(location=[-1.37314, -89.67134], zoom_start=8, )
# hm_wide = HeatMap(
#     list(zip(df.lat.values, df.lon.values)),
#     min_opacity=0.2,
#     radius=17,
#     blur=15,
#     max_zoom=1,
# )
# initial_map.add_child(hm_wide)
# initial_map.save("map.html")