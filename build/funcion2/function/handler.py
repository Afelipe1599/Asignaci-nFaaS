import requests
import random

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    r = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBFDvrnBcieiFv9V0lZc6QXgcLISsVOFFY")
    result = r.json()
    lat= result['location']['lat']
    lng= result['location']['lng']
    a=str(lat)
    b=str(lng)
    q = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+a+","+b+"&key=AIzaSyBFDvrnBcieiFv9V0lZc6QXgcLISsVOFFY")
    result2 = q.json()
    Pais = str(result2['results'][0]['address_components'][6]['long_name'])
    ciudad = str(result2['results'][0]['address_components'][5]['long_name'])
    direccion = str(result2['results'][0]['formatted_address'])
    salida = "El servidor se entra en "+Pais+","+ciudad+","+direccion
    return (salida)
