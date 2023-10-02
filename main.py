 # rest apis
#application programming interface
import requests 
#requests something from the internet
import json 
#json stands for javascript object notation

response = requests.get('https://randomuser.me/api')
print(response.json())
gender = response.json()['results'][0]['gender']
print(gender)
title = response.json()['results'][0]['name']['title']
print(title)
lname = response.json()['results'][0]['name']['last']
fname = response.json()['results'][0]['name']['first']
print(lname)
print(fname)
email = response.json()['results'][0]['email']
print(email)
phonenumber = response.json()['results'][0]['phone']
print(phonenumber)
city = response.json()['results'][0]['location']['city']
print(city)
postalcode = response.json()['results'][0]['location']['postcode']
print(postalcode)
saddress = response.json()['results'][0]['location']['street']['name']
saddress2 = str(response.json()['results'][0]['location']['street']['number'])
print(saddress + saddress2)
date = response.json()['results'][0]['dob']['date']
id = response.json()['results'][0]['login']['uuid']
age = response.json()['results'][0]['dob']['age']
print(date)
print(id)
print(age)