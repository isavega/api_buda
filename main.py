from api import get_trades
from utils import calculate_traded_money, convert_to_milliseconds, calculate_percentage_increase


# Obtener trades del evento "Black Buda" BTC-CLP
market = "btc-clp"
limit = 100
start_year, start_month, start_day, start_hour, start_minute = 2024, 3, 1, 12, 0
end_year, end_month, end_day, end_hour, end_minute = 2024, 3, 1, 13, 0
timezone_str = 'America/Santiago'
start_ms, end_ms = convert_to_milliseconds(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute, timezone_str)
timestamp = end_ms
entries = get_trades(market, timestamp, limit)


# entrie = [timestamp, amount, price, direction]
# price es el precio en CLP de 1 BTC
# amount es la cantidad de BTC transados
# direction es la dirección de la transacción (buy o sell)
# dinero transado = sum(amount * price) para todas las entries


# ¿Cuánto dinero (en CLP) se transó durante el evento "Black Buda" BTC-CLP ? (truncar en 2 decimales)

print(f"Dinero transado durante el evento 'Black Buda' BTC-CLP: {calculate_traded_money(entries)} CLP")


# Obtener trades del evento "Black Buda" BTC-CLP del año anterior
start_year, start_month, start_day, start_hour, start_minute = 2023, 3, 1, 12, 0
end_year, end_month, end_day, end_hour, end_minute = 2023, 3, 1, 13, 0
timezone_str = 'America/Santiago'
start_ms, end_ms = convert_to_milliseconds(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute, timezone_str)
timestamp_last_year = end_ms

# En comparación con el mismo día del año anterior, ¿cuál fue el aumento porcentual en el volumen de transacciones (en BTC)? (truncar en 2 decimales)

current_year_entries = get_trades(market, timestamp, limit)
last_year_entries = get_trades(market, timestamp_last_year, limit)


percentage_increase = calculate_percentage_increase(current_year_entries, last_year_entries)

print(f"Aumento porcentual en el volumen de transacciones respecto al mismo día del año anterior en la hora del evento: {percentage_increase}%")
