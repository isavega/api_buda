from api import get_trades
from utils import calculate_traded_money, convert_to_milliseconds,format_number_to_CLP


# Obtener trades del evento "Black Buda" BTC-CLP
market = "btc-clp"
limit = 100
start_year, start_month, start_day, start_hour, start_minute = 2024, 3, 1, 12, 0
end_year, end_month, end_day, end_hour, end_minute = 2024, 3, 1, 13, 0
timezone_str = 'America/Santiago'
start_ms, end_ms = convert_to_milliseconds(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute, timezone_str)
timestamp = end_ms
entries = get_trades(market, timestamp, limit)


# ¿Cuánto dinero (en CLP) se transó durante el evento "Black Buda" BTC-CLP ? (truncar en 2 decimales)
# entrie = [timestamp, amount, price, direction]
# price es el precio en CLP de 1 BTC
# amount es la cantidad de BTC transados
# direction es la dirección de la transacción (buy o sell)
# dinero transado = sum(amount * price) para todas las entries

print(f"Dinero transado durante el evento 'Black Buda' BTC-CLP: {format_number_to_CLP(calculate_traded_money(entries))} CLP")