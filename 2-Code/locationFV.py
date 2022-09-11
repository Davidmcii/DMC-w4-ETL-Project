def locationFV(municipio):
    
    from  geopy.geocoders import Nominatim
    
    geolocator = Nominatim(user_agent="Your_Name")
    city =str(municipio)
    country ="Spain"
    loc = geolocator.geocode(city+','+ country)

    print(loc.address)

    return '{};{};{}'.format(loc.address,loc.latitude,loc.longitude)

