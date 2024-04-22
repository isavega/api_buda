# Buda Test

## Usage

```python
python main.py
```

## Problem

Imagina que el 1 de marzo de 2024, en el lapso de una hora, de 12:00 a 13:00, Buda.com lanzó una oferta especial llamada BlackBuda. Durante este período, ¡todos los usuarios que operaran en el mercado BTC-CLP disfrutaron de un asombroso 100% de descuento en las comisiones de transacción! 

Fue una oportunidad increíble para comprar y vender bitcoin  y ahora necesitamos de tu ayuda para evaluar el desempeño del BlackBuda.

Utilizando nuestra API pública, necesitamos que recopiles la información necesaria para analizar las siguientes situaciones. 

## Questions

1. ¿Cuánto dinero (en CLP) se transó durante el evento "Black Buda" BTC-CLP ? (truncar en 2 decimales)

2. En comparación con el mismo día del año anterior, ¿cuál fue el aumento porcentual en el volumen de transacciones (en BTC)? (truncar en 2 decimales)

3. Considerando que la comisión normal corresponde a un 0.8% ¿Cuánto dinero (en CLP) se dejó de ganar debido a la liberación de comisiones durante el BlackBuda? (truncar en 2 decimales)

## Assumptions

- Las comisiones se cobran en CLP.
- Para todos los cálculos utilizar el horario entre 12:00 y 13:00, ambos inclusive, considera la zona horaria GMT -03:00.
- Para todas las respuestas truncar en 2 decimales, ocupando un punto como separador de decimales.
- Recuerda que en un mercado del tipo Moneda_1-Moneda_2, la cantidad transada está en Moneda_1 y el precio en Moneda_2.

## API

[API de Buda](https://api.buda.com/#rest-api-llamadas-publicas-libro-de-ordenes)
