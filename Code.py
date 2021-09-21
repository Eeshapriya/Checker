import folium
import pandas
vol = pandas.read_csv("volcano.csv", encoding = "ISO-8859-1")
latitude = list(vol["LAT"])
longitude = list(vol["LON"])
loc = list(vol["LOCATION"])
name = list(vol["NAME"])
elevation = list(vol["ELE"])
Type = list(vol["Type"])

def altitude_checker(alt):
    if alt<2000:
        return 'green'
    elif  2000<=alt<=3000:
        return 'orange'
    else:
        return 'red'
    

m = folium.Map(location=[10,45], zoom_start=3, tiles="Stamen Toner")

groupV = folium.FeatureGroup(name="Volcanoes")

for lt,ln,lo,na,el,ty in zip(latitude,longitude,loc,name,elevation,Type):
    groupV.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup = "{}\n{}\n{}\n{}".format(lo,na,ty,str(el)+" m"), fill_color = altitude_checker(el),color = 'grey', fill_opacity = 1))
    #groupV.add_child(folium.Marker(location=[lt,ln], popup=ty, icon=folium.Icon(color=altitude_checker(el))))

cri = pandas.read_csv("country.csv", encoding = "ISO-8859-1")
country = list(cri['country'])
crime = list(cri['crime'])
saftey = list(cri['saftey'])
vert = list(cri['vertical'])
hori = list(cri['horizontal'])

def crime_rate(cr):
    if cr<30:
        return "green"
    elif 30<=cr<=50:
        return "orange"
    else:
        return "red"

groupY = folium.FeatureGroup("Crime Rate")
for vert,hori,country,crime,saftey in zip(vert,hori,country,crime,saftey):
    groupY.add_child(folium.CircleMarker(location = [vert,hori], radius = 6, popup = "{}\n{}\n{}".format(country,str(crime)+"%",str(saftey)+"%"), fill_color = crime_rate(crime),color = 'grey', fill_opacity = 1))

won = pandas.read_csv("wonders.csv", encoding = "ISO-8859-1")
X =  list(won['xy'])
Lati =  list(won["lat"])
Long =  list(won["lon"])


groupZ = folium.FeatureGroup(name="Wonders")

for Lati,Long,na in zip(Lati,Long,X):
    groupZ.add_child(folium.Marker(location=[Lati,Long], popup=na, icon=folium.Icon(color='green')))



groupP = folium.FeatureGroup(name="Population")
groupP.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


m.add_child(groupP)
m.add_child(groupV)
m.add_child(groupY)
m.add_child(groupZ)
m.add_child(folium.LayerControl())
m.save("test.html")