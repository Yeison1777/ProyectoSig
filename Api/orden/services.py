# Api/orden/services.py

import requests
from django.conf import settings

def calcular_ruta_optima(origen, destinos):
    """
    origen: string 'lat,lng'
    destinos: lista de strings ['lat1,lng1', 'lat2,lng2', ...]
    """
    #destinos_str = "|".join(destinos)
    #url = (
    #    f"https://maps.googleapis.com/maps/api/directions/json?"
    #    f"origin={origen}&destination={origen}&waypoints=optimize:true|{destinos_str}&key={settings.GOOGLE_MAPS_API_KEY}"
    #)
    #response = requests.get(url)
    #return response.json()

    if destinos:
       destino_final = destinos[-1]
       waypoints = destinos[:-1]
    else:
       destino_final = origen
       waypoints = []
    waypoints_str = "|".join(waypoints)
    url = (
       #este codigo es para obtener la ruta optima
        #f"https://maps.googleapis.com/maps/api/directions/json?"
        #f"origin={origen}&destination={destino_final}"
        #f"&waypoints=optimize:true|{waypoints_str}"  # solo si hay waypoints
        #f"&key={settings.GOOGLE_MAPS_API_KEY}"
       

        # este codigo es para obtener la ruta optima con el trafico
        f"https://maps.googleapis.com/maps/api/directions/json?"
        f"origin={origen}&destination={destino_final}"
        f"&waypoints=optimize:true|{waypoints_str}" if waypoints else ""
        f"&departure_time=now"
        f"&traffic_model=best_guess"
        f"&key={settings.GOOGLE_MAPS_API_KEY}"
    )
    response = requests.get(url)
    return response.json()