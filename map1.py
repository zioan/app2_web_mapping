#tiles = "Stamen Terrain"

import folium
import pandas


#US VOLCANOES
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
loc = list(data["LOCATION"])
typ = list(data["TYPE"])
elev = list(data["ELEV"])

def color_producer(elevation):
  if elevation < 1000:
    return "green"
  elif 1000<= elevation < 3000:
    return "orange"
  else:
    return "red" 

  #map starting point
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")



fgv = folium.FeatureGroup(name="US Volcanoes")

  # zip() iterete on bouth lists 1 by 1

for lt, ln, lc, tp, el in zip(lat, lon, loc, typ, elev):
  fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=f"Volcano -{lc} -Elevation:{el}m -Type:{tp}", icon=folium.Icon, fill_color=color_producer(el), color = "gray", fill_opacity = 0.7))

  # OR
#map.add_child(folium.Marker(location=[38.2, -99.1], popup="I am a Marker", icon=folium.Icon(color="green")))


  #WORLD POPULATION
#polygon markers(country border lines)
fgp = folium.FeatureGroup(name="World Population")

fgp.add_child(folium.GeoJson(data = (open("world.json", "r", encoding="utf-8-sig").read()), style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
else " orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 
else "red"}))


map.add_child(fgv)
map.add_child(fgp)

  #Layer Control Panel
map.add_child(folium.LayerControl())

map.save("Map1.html")