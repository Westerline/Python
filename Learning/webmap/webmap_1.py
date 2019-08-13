#List the functions available in folium
import folium
import pandas
print(dir(folium))

#Create a map object, we need the HTML file from this object to create a map.
#Note, map and Map are two different items. Map is a method from the folium package.
#Tiles lets you pick between different views, similar to Google Maps Street View
map =   folium.Map(location=[45.3733, -84.9553], 
                    zoom_start = 15)

#List the methods we can apply to the object returned by the Map function
print(dir(folium.Map))

#Next, let's add some markers to our map
folium.Marker(location=[45.3735698, -84.9585], 
                popup= 'Mitchell Street Market', 
                tooltip='Convenience Store', 
                icon = folium.Icon(icon = 'cloud')
                ).add_to(map)

#Add a circle
folium.Circle(location=[45.3735698, -84.9585], 
                radius = 10
                ).add_to(map)

#Save the variable map to test.html
print(map.save('Petoskey.html'))