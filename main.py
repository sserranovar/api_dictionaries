#rest apis
#application programming interface
import requests #requests something from the internet
import json #json stands for javascript obect notation
response=requests.get("https://randomuser.me/api/")
#print(response.json())
gender=response.json()['results'][0]['gender']
print(gender)
title=response.json()['results'][0]['name']['title']
print(title)
email=response.json()['results'][0]['email']
print(email)
phonumber=response.json()['results'][0]['phone']
print(phonumber)
city=response.json()['results'][0]['location']['city']
print(city)
postalcode=response.json()['results'][0]['location']['postcode']
print(postalcode)
streetaddress=response.json()['results'][0]['location']['street']
print(streetaddress)
dateObirth=response.json()['results'][0]['dob']['date']
print(dateObirth)
userid=response.json()['results'][0]['id']['value']
print(userid)
registeredage=response.json()['results'][0]['registered']['date']
print(registeredage)