import bs4
import requests
import uuid
from datetime import datetime
import json
from unidecode import unidecode
import re
import time



def crear_lista_instutuciones_sefirc():
    response = requests.get('http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/IUListadoDependencias.jsp')
    sopa = bs4.BeautifulSoup(response.text, 'html.parser')
    # Recolecta nombre de clasificador y Dependencia
    intituciones_datos = sopa.find_all('tr')
    lista_intitucciones = []
    for e in intituciones_datos:
        nombre_clasificador = e.find_all('td')
        
        if len(nombre_clasificador) > 6:
            if len(nombre_clasificador[2].text) > 2:
                clasificador = nombre_clasificador[2].text
            else:
                clasificador = "Desconocido"
            dependencia = nombre_clasificador[5].text
            total = nombre_clasificador[6].text
            url = "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/" + nombre_clasificador[7].a.get('href')
            lista_intitucciones.append({"clasificador": clasificador, "dependencia": dependencia, "total": total, "url": url })
    return(lista_intitucciones)
lista_intitucciones = crear_lista_instutuciones_sefirc()


with open('declaraciones.json', 'w', encoding='utf-8') as file:
    json.dump(lista_intitucciones, file, ensure_ascii=False, indent=4)
print(lista_intitucciones)