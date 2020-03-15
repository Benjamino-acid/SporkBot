##try:
##    #Runs Location API and and set the key variable
##    location_key = (get("http://dataservice.accuweather.com/locations/v1/search?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty&q=" + search)).json()
##    key = (location_key[0]["Key"])
##    print(key)
##
##    postal_key = (get("http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFt&q=" + search)).json()
##    key = (postal_key[0]["Key"])
##    print(key)

    #Run Current Weather API and pulls information
##    current = (get("http://dataservice.accuweather.com/currentconditions/v1/" + key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
##    print(current[0]["LocalObservationDateTime"])
##    print(current[0]["WeatherText"])
##    print(current[0]["Temperature"]["Imperial"])
##    if (current[0]["HasPrecipitation"]) == True:
##        print("It is curently " + current[0]["PrecipitationType"])
##
##    else:
##        print("It is curently not precipitating.")
##
##    #Run Today's Forcast API
##    day_forcast = (get("http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
##    print(day_forcast)
##
##    hourly_forcast = (get("http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + key + "?apikey=YxIMPCwpe0eE1xnCphoBSskWWFzJaFty")).json()
##    print(hourly_forcast)
##
##    
##except KeyError:
##    return_error()
