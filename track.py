import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode
number=input("enter a number with country code:")

# Parsing String to the Phone number
phoneNumber = phonenumbers.parse(number)

Key = "e75c3cff85a2437f8cc264376befef0e"

# printing the geolocation of the given number using the geocoder module
yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("location : "+yourLocation)
# Using the carrier module of phonenumbers to print the service provider name in console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print("service provider : " + yourServiceProvider)

# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat, lng], zoom_start=9)

# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")