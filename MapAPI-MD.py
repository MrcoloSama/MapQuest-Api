import requests
from urllib.parse import urlencode

def obtener_distancia(ciudad_origen, ciudad_destino):
    url = 'https://www.mapquestapi.com/directions/v2/route?'
    apikey = input("Ingresar apiKey: ")

    consulta = url + urlencode({"key": apikey, "from": ciudad_origen, "to": ciudad_destino})
    print(" ")
    print("La URL es:", consulta)
    print(" ")

    response = requests.get(consulta).json()
    if response["info"]["statuscode"] == 0:
        distancia = round(response["route"]["distance"], 1)
        return distancia, response["route"]["legs"][0]["maneuvers"]
    else:
        print("No se pudo obtener la distancia. Código de estado:", response["info"]["statuscode"])
        return None, None

def calcular_duracion(distancia):
    velocidad_promedio = 80  # km/h
    tiempo_en_horas = round(distancia / velocidad_promedio, 1)
    tiempo_en_minutos = round(tiempo_en_horas * 60, 1)
    tiempo_en_segundos = round(tiempo_en_minutos * 60, 1)
    return tiempo_en_horas, tiempo_en_minutos, tiempo_en_segundos

def calcular_combustible(distancia):
    rendimiento = 12  # km/l
    combustible_requerido = round(distancia / rendimiento, 1)
    return combustible_requerido

def imprimir_narrativa(narrativa):
    print("Narrativa del viaje paso a paso:")
    for i, paso in enumerate(narrativa, start=1):
        print(f"Paso {i}: {paso['narrative']}")

while True:
    print("==== Calculadora de Viaje ====")
    print("Ingrese 'S' para salir.")
    ciudad_origen = input("Ingrese la ciudad de origen (Chile): ")
    if ciudad_origen.lower() == "s":
        break
    ciudad_destino = input("Ingrese la ciudad de destino (Latinoamérica): ")
    if ciudad_destino.lower() == "s":
        break

    distancia, narrativa = obtener_distancia(ciudad_origen, ciudad_destino)
    if distancia is not None:
        duracion_horas, duracion_minutos, duracion_segundos = calcular_duracion(distancia)
        combustible_requerido = calcular_combustible(distancia)

        print("La distancia entre", ciudad_origen, "y", ciudad_destino, "es de", format(distancia, ".1f"), "km.")
        print("La duración del viaje es de", format(duracion_horas, ".1f"), "horas,", format(duracion_minutos, ".1f"), "minutos y", format(duracion_segundos, ".1f"), "segundos.")
        print("Se requieren", format(combustible_requerido, ".1f"), "litros de combustible.")
        print("")
        
        if narrativa is not None:
            imprimir_narrativa(narrativa)
            print("")

print("¡Hasta luego!")

