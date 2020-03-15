import sys
import json
from requests import get


def return_error():
    print("It seems this service is currently unavailable, sorry.")
    print("Visit AccuWeather.com for weather updates")


def return_help():
    print("Weather Help")
    print("Will display current conditions and the daily forcast")
    print("\tUsage: /spork weather [city]")


def loc_search(value):
    try:
        location_key = (get(
            "http://dataservice.accuweather.com/locations/v1/search?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty&q=" + value)).json()
        key = (location_key[0]["Key"])
        return(key)
    except KeyError:
        return_error()


def post_search(value):
    try:
        postal_key = (get(
            "http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFt&q=" + value)).json()
        key = (postal_key[0]["Key"])
        return(key)
    except KeyError:
        return_error()


def current_weather(loc_key):
    current = (get(
        "http://dataservice.accuweather.com/currentconditions/v1/" + loc_key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
    print(current[0]["LocalObservationDateTime"])
    print(current[0]["WeatherText"])
    print(current[0]["Temperature"]["Imperial"])
    if (current[0]["HasPrecipitation"]) is True:
        print("It is curently " + current[0]["PrecipitationType"])
    else:
        print("It is curently not precipitating.")


def daily_fcst(loc_key):
    # Run Today's Forcast API
    day_forecast = (get(
        "http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + loc_key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
    return(day_forecast)


def hourly_fcst(loc_key):
    hourly_forecast = (get(
        "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + loc_key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
    return(hourly_forecast)


arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]


if type(arg1) == str:
    loc_search(arg2)
elif type(arg1) == int:
    post_search(arg2)

if arg3.lower() == "current":
    current_weather(key)
elif arg3.lower() == "today":
    daily_fcst(key)
elif arg3.lower() == "hourly":
    hourly_fcst(key)





