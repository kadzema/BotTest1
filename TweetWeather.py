# Dependencies
import tweepy
import time
import json
import requests as req 
import datetime

# Twitter API Keys
#kristine keys
consumer_key = "HQ1Xg26ORFk9Ry8aCYIPO1cn2"
consumer_secret = "gFMayjKXJwLGN0ilUyhk3aIfhGYwepT4vCFXtljx7NXB9qyyX2"
access_token = "35740765-Z8VkREBVuYzEnoKwfKU9NqbJp1FRJEEUZ1VKQ5yNY"
access_token_secret = "N3VeKhoiOgFfrW65uFJflIfAxhDT24MHR2NVkFH5vd0XR"

#Open Weather API
api_key="fa175c2789ea78e45896267c2a85aa5c"

url = "http://api.openweathermap.org/data/2.5/weather?"



# Create a function that tweets
def TweetOut(city):

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    #get the weather

    units = "imperial"

    query_url = url + "appid=" + api_key + "&q=" + city + "&units=" + units

    print(query_url)

    weather_response = req.get(query_url)
    weather_json = weather_response.json()

    api.update_status(
        "%s Weather as of %s: %s F" %
        (city, datetime.datetime.now().strftime("%I:%M %p"),
         weather_json["main"]["temp"]))


# counter = 0

# Infinitely loop
while(True): # and counter <2):

    city = "Montclair, NJ"
    # Call the TweetQuotes function and specify the tweet number
    TweetOut(city)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(3600)

    # counter += 1
