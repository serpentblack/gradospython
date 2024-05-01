'''
Este código define varias rutas que corresponden a las conversiones que 
quieres realizar, y cada una toma un parámetro valor_grados en la URL y
devuelve el resultado de la conversión en formato JSON. Por ejemplo, para
convertir grados Celsius a grados Fahrenheit, puedes hacer una solicitud 
GET a /celsius_to_fahrenheit/{valor_grados} donde {valor_grados} es el valor
en grados Celsius que deseas convertir.

Una vez que tengas este código, puedes ejecutar tu servicio web ejecutando
el archivo Python y luego accediendo a las rutas definidas en tu navegador
o mediante herramientas como cURL o Postman.
'''
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a los orígenes que desees permitir
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/celsius_to_fahrenheit/{valor_grados}")
def celsius_to_fahrenheit(valor_grados: float):
    return {"resultado": valor_grados * 9 / 5 + 32}

@app.get("/celsius_to_kelvin/{valor_grados}")
def celsius_to_kelvin(valor_grados: float):
    return {"resultado": valor_grados + 273.15}

@app.get("/fahrenheit_to_celsius/{valor_grados}")
def fahrenheit_to_celsius(valor_grados: float):
    return {"resultado": round(((valor_grados) - 32) * (5 / 9), 2)}

@app.get("/fahrenheit_to_kelvin/{valor_grados}")
def fahrenheit_to_kelvin(valor_grados: float):
    return {"resultado": round((valor_grados - 32) * 5 / 9 + 273.15, 2)}

@app.get("/kelvin_to_celsius/{valor_grados}")
def kelvin_to_celsius(valor_grados: float):
    return {"resultado": valor_grados - 273.15}

@app.get("/kelvin_to_fahrenheit/{valor_grados}")
def kelvin_to_fahrenheit(valor_grados: float):
    return {"resultado": round((valor_grados - 273.15) * 9 / 5 + 32, 2)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
