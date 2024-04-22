import requests
from utils import format_number_to_CLP

URL_BASE = "https://www.buda.com/api/v2"


def get_trades(market_id, timestamp, limit):
    response = requests.get(f"{URL_BASE}/markets/{market_id}/trades", params={"timestamp": timestamp, "limit": limit})
    data = response.json()
    
    # Estrucutra de respuesta
    
    # {
    #   "trades": {
    #     "timestamp": "1476905551698",
    #     "last_timestamp": "1476380738941",
    #     "market_id": "BTC-CLP",
    #     "entries": [
    #       ["1476905551687", "0.00984662", "435447.12", "buy"],
    #       ["1476905551676", "3.01572553", "435283.3", "buy"],
    #       ...
    #     ]
    #   }
    # }
    
    # timestamp: Unix timestamp del trade más reciente incluido en la respuesta, es decir, el que paso último en el tiempo
    # last_timestamp: Unix timestamp del trade más antiguo incluido en la respuesta, es decir, el que paso primero en el tiempo
    # entries: arreglo de transacciones, donde cada transacción es un arreglo con los siguientes elementos: [timestamp, amount, price, direction]
    
    
    # Chequear que la data de la llamada cubra el rango de tiempo solicitado, el cual es desde el timestamp de inicio del evento hasta el timestamp de fin del evento
    # Unix timestamp in milliseconds for March 1, 2024, at 12:00 PM (GMT -03:00): 1709305200000
    # Unix timestamp in milliseconds for March 1, 2024, at 13:00 PM (GMT -03:00): 1709308800000
    
    # Si la data no cubre el rango de tiempo solicitado, hacer llamadas adicionales hasta que se cubra el rango de tiempo solicitado
    # Si la data cubre el rango de tiempo solicitado, retornar la data
    
    if int(data["trades"]["timestamp"]) < timestamp:
        current_timestamp = int(data["trades"]["last_timestamp"])
        entries = data["trades"]["entries"]
        while current_timestamp < timestamp:
            print("ENTRO AL WHILE")
            response = requests.get(f"{URL_BASE}/markets/{market_id}/trades", params={"timestamp": timestamp, "limit": limit})
            data = response.json()
            current_timestamp = int(data["trades"]["last_timestamp"])
            entries += data["trades"]["entries"]
        return entries
    else:
        return data["trades"]["entries"]