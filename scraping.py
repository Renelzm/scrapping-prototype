import bs4
import requests
import uuid
from datetime import datetime
import json
from unidecode import unidecode
import re
import time

# >2 LISTA DE URLS:
listas_trbajar_individual =[    {
        "clasificador": "PODER EJECUTIVO",
        "dependencia": "COMISION ESTATAL DE SEGURIDAD PUBLICA",
        "total": "3172",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=E0064&q2=4"
    },
     {
        "clasificador": "ORGANISMOS PUBLICOS AUTONOMOS",
        "dependencia": "FISCALIA GENERAL DEL ESTADO",
        "total": "5635",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=M0077&q2=136"
    },]

urls_list = [
   

   
    {
        "clasificador": "ORGANISMOS PUBLICOS AUTONOMOS",
        "dependencia": "INSTITUTO COAHUILENSE DE ACCESO A LA INFORMACION PUBLICA",
        "total": "371",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=M0078&q2=137"
    },
    {
        "clasificador": "ORGANISMOS PUBLICOS AUTONOMOS",
        "dependencia": "INSTITUTO ELECTORAL DE COAHUILA",
        "total": "1537",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=M0082&q2=7"
    },
    {
        "clasificador": "ORGANISMOS PUBLICOS AUTONOMOS",
        "dependencia": "SECRETARIA EJECUTIVA DEL SISTEMA ESTATAL ANTICORRUPCION",
        "total": "96",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=E0068&q2=148"
    },
    {
        "clasificador": "ORGANISMOS PUBLICOS AUTONOMOS",
        "dependencia": "TRIBUNAL DE JUSTICIA ADMINISTRATIVA",
        "total": "45",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=E0104&q2=201"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ABASOLO",
        "total": "349",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=61&q2=001"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ACUÑA",
        "total": "3892",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=62&q2=002"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ALLENDE",
        "total": "874",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=63&q2=003"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ARTEAGA",
        "total": "1356",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=64&q2=004"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "CANDELA",
        "total": "139",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=65&q2=005"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "CASTAÑOS",
        "total": "250",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=66&q2=006"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "CUATROCIENEGAS",
        "total": "659",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=67&q2=007"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ESCOBEDO",
        "total": "67",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=68&q2=008"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "FRANCISCO I. MADERO",
        "total": "1208",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=69&q2=009"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "FRONTERA",
        "total": "1010",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=70&q2=010"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "GENERAL CEPEDA",
        "total": "527",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=71&q2=011"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "GUERRERO",
        "total": "138",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=72&q2=012"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "HIDALGO",
        "total": "291",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=73&q2=013"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "JIMENEZ",
        "total": "141",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=74&q2=014"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "JUAREZ",
        "total": "120",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=75&q2=015"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "LAMADRID",
        "total": "287",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=76&q2=016"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "MATAMOROS",
        "total": "3316",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=77&q2=017"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "MONCLOVA",
        "total": "3454",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=1&q2=018"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "MORELOS",
        "total": "311",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=78&q2=019"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "MUZQUIZ",
        "total": "1203",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=79&q2=020"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "NADADORES",
        "total": "520",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=80&q2=021"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "NAVA",
        "total": "900",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=81&q2=022"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "OCAMPO",
        "total": "258",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=82&q2=023"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "PARRAS",
        "total": "595",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=83&q2=024"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "PIEDRAS NEGRAS",
        "total": "5090",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=84&q2=025"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "PROGRESO",
        "total": "272",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=85&q2=026"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "RAMOS ARIZPE",
        "total": "1441",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=86&q2=027"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SABINAS",
        "total": "2443",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=87&q2=028"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SACRAMENTO",
        "total": "239",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=88&q2=029"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SALTILLO",
        "total": "13460",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=89&q2=030"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SAN BUENAVENTURA",
        "total": "528",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=90&q2=031"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SAN JUAN DE SABINAS",
        "total": "1053",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=91&q2=032"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SAN PEDRO",
        "total": "2062",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=92&q2=033"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "SIERRA MOJADA",
        "total": "176",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=93&q2=034"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "VIESCA",
        "total": "384",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=95&q2=036"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "VILLA UNION",
        "total": "496",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=96&q2=037"
    },
    {
        "clasificador": "MUNICIPIOS",
        "dependencia": "ZARAGOZA",
        "total": "866",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=97&q2=038"
    },
     {
        "clasificador": "PODER LEGISLATIVO",
        "dependencia": "AUDITORIA SUPERIOR DEL ESTADO DE COAHUILA",
        "total": "1488",
        "url": "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/.?q=E0065&q2=2"
    }
]



# >4 PARA CREAR LISTA
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

# >4 HELPERS PARA DECLARACIONES
def extraer_tipo_y_fecha(tipoyfecha):
    tipo_declaracion = tipoyfecha.split(":")[1].strip().split(".")[0]

    if not tipo_declaracion ==  "INICIAL" or tipo_declaracion ==  "MODIFICACIÓN" or  tipo_declaracion == "CONCLUSIÓN":
        if tipo_declaracion == 'CONCLUSION':
            tipo_declaracion = 'CONCLUSIÓN'
        else:
            tipo_declaracion = "MODIFICACIÓN" 
    fecha_referente = tipoyfecha.split(":")[2].strip().replace(".","")
    fecha_referente = datetime.strptime(fecha_referente, '%d/%m/%Y').strftime("%Y-%m-%dT%H:%M:%SZ")
    return(tipo_declaracion, fecha_referente)
def extraer_nombres(datos):

    data  = datos.split(",")
    if len(data) == 5:
        nombre = datos.split(",")[2].split(":")[1].strip()
        apellido_paterno = datos.split(",")[3].strip()
        apellido_materno = datos.split(",")[4].strip().rstrip('.')
    return(nombre, apellido_paterno, apellido_materno)
def extraer_datos_Puesto(datos):
    diccionario_entidades = {
    "Abasolo":"001",
    "Acuña":"002",
    "Allende":"003",
    "Arteaga":"004",
    "Candela":"005",
    "Castaños":"006",
    "Cuatro Ciénegas":"007",
    "Escobedo":"008",
    "Francisco I. Madero":"009",
    "Frontera":"010",
    "General Cepeda":"011",
    "Guerrero":"012",
    "Hidalgo":"013",
    "Jiménez":"014",
    "Juárez":"015",
    "Lamadrid":"016",
    "Matamoros":"017",
    "Monclova":"018",
    "Morelos":"019",
    "Múzquiz":"020",
    "Nadadores":"021",
    "Nava":"022",
    "Ocampo":"023",
    "Parras":"024",
    "Piedras Negras":"025",
    "Progreso":"026",
    "Ramos Arizpe":"027",
    "Sabinas":"028",
    "Sacramento":"029",
    "Saltillo":"030",
    "San Buenaventura":"031",
    "San Juan de Sabinas":"032",
    "San Pedro":"033",
    "Sierra Mojada":"034",
    "Torreón":"035",
    "Viesca":"036",
    "Villa Unión":"037",
    "Zaragoza":"038"
}
    datos = datos.split("\n")
    sector = datos[0].split(":")[1].strip().replace(".","")
    if not sector == "ESTATAL" or sector == "MUNICIPAL" or sector == "FEDERAL" or sector == "MUNICIPAL_ALCALDIA":
        sector = "ESTATAL"
    elif sector == "MUNICIPAL":
        sector = "MUNICIPAL_ALCALDIA"
    municipio = datos[1].split(":")[1].strip().replace(".","")

    dependencia = datos[2].split(":")[1].strip().replace(".","")
    nombre_puesto = datos[3].split(":")[1].strip().replace(".","")
    municipio_clave = unidecode(municipio).capitalize().strip()
    clave = ""
    for key, value in diccionario_entidades.items():
        if unidecode(key) == municipio_clave:
            municipio = key.upper()
            clave = value
    if not clave:
        municipio = "SALTILLO"  
        clave= "030"
   
    iniciales_puesto = nombre_puesto[:3]
    datos_puesto = {"sector": sector, "municipio": municipio, "dependencia": dependencia, "nombre_puesto": nombre_puesto, "iniciales_nivel" : iniciales_puesto, "clave": clave}
    
    return(datos_puesto)
def extraer_datos_ingreso(datos, tipo):
    
    if tipo == "INICIAL":
        datosIngreso = datos.split('$')
        if "MENSUAL" in datos:
            ingreso = float(datosIngreso[-1].rstrip('.'))
        elif "ANUAL" in datos:
            ingreso = (float(datosIngreso[-1].rstrip('.')) / 12)
        else:
            ingreso = float(datosIngreso[-1].rstrip('.'))
      
        datos_ingreso_general =  {
					            "remuneracionMensualCargoPublico": {
					            	"valor": ingreso,
					            	"moneda": "MXN"
					            },
					            "ingresoMensualNetoDeclarante": {
					            	"valor": ingreso,
					            	"moneda": "MXN"
					            },
					            "totalIngresosMensualesNetos": {
					            	"valor": ingreso,
					            	"moneda": "MXN"
					            }
                            }
        return datos_ingreso_general
    elif tipo == "MODIFICACIÓN":
        datosIngreso = datos.split('$')
        if "MENSUAL" in datos:
            ingreso = (float(datosIngreso[-1].rstrip('.')) * 12)
        elif "ANUAL" in datos:
            ingreso = float(datosIngreso[-1].rstrip('.'))
        else:
            ingreso = (float(datosIngreso[-1].rstrip('.')) * 12 )
        datos_ingreso_general =  {
                                "remuneracionAnualCargoPublico": {
                                    "valor": ingreso,
	                            "moneda":"MXN"
                                },
                                "ingresoAnualNetoDeclarante": {
	                            "valor": ingreso,
	                            "moneda": "MXN"
                                },
                                "totalIngresosAnualesNetos": {
                                    "valor": ingreso,
                                    "moneda": "MXN"
                              } }
                              
        return datos_ingreso_general
    elif tipo == "CONCLUSIÓN":
        datosIngreso = datos.split('$')
        if "MENSUAL" in datos:
            ingreso = (float(datosIngreso[-1].rstrip('.') )* 12)
        elif "ANUAL" in datos:
            ingreso = float(datosIngreso[-1].rstrip('.'))
        else:
            ingreso = (float(datosIngreso[-1].rstrip('.') )* 12 )
        datos_ingreso_general = {
                                "remuneracionConclusionCargoPublico": {
                                    "valor": ingreso,
	                                "moneda":"MXN"
                                },
                                "ingresoConclusionNetoDeclarante": {
	                            "valor": ingreso,
	                            "moneda": "MXN"
                                },
                                "totalIngresosConclusionNetos": {
                                    "valor": ingreso,
                                    "moneda": "MXN"
                              } }
                              
        return datos_ingreso_general
def extraer_bienes(datos):
    datos = datos.split("\n")
    valores_adquisicion = {
        "COMPRAVENTA" : "CPV",
        "CESIÓN" : "CSN",
        "DONACIÓN" : "DNC",
        "HERENCIA" : "HRN",
        "PERMUTA" : "PRM",
        "RIFA O SORTEO" : "RST",
        "SENTENCIA" : "STC"
    }
    valores_tipo = {
         "CASA" : "CASA",
         "DEPARTAMENTO" : "DPTO",
         "EDIFICIO" : "EDIF",
         "LOCAL COMERCIAL" : "LOCC",
         "BODEGA" : "BODG",
         "PALCO" : "PALC",
         "RANCHO" : "RACH",
         "TERRENO" : "TERR",
         "OTROS (ESPECIFIQUE)" : "OTRO"
    }
    tipo_inmueble = datos[1].split(":")[1].strip().rstrip('.')
    forma_adquisicion = datos[2].split(":")[1].strip().rstrip('.').split(" ")[0]
    forma_pago = "NO APLICA"
    titular_propiedad = datos[4].split(":")[1].strip().rstrip('.').split(" ")[0]
   
    if tipo_inmueble in valores_tipo:
        valor_clave = valores_tipo[tipo_inmueble]
    else:
        valor_clave = "OTRO"
    
    
    if forma_adquisicion in ["COMPRAVENTA","CESIÓN", "HERENCIA", "PERMUTA", "RIFA O SORTEO", "SENTENCIA"]:
        forma_adquisicion = forma_adquisicion
    elif forma_adquisicion in ["DONACIÓN", "DONACION"]:
        forma_adquisicion = "DONACIÓN"
    elif forma_adquisicion in ["CREDITO", "CRÉDITO" ]:
        forma_adquisicion = "COMPRAVENTA"
        forma_pago = "CRÉDITO"
    else:   
        forma_adquisicion = "COMPRAVENTA"
    
    bienes_dommi =  {
            "ninguno": False,
            "bienInmueble": [
              {
                "tipoOperacion": "SIN_CAMBIOS",
                "tipoInmueble": {
                  "clave": valor_clave,
                  "valor": tipo_inmueble
                },
                "titular": [
                  {
                    "clave": "DEC",
                    "valor": "DECLARANTE"
                  }
                ],
                "superficieTerreno": {
                  "valor": 120,
                  "unidad": "m2"
                },
                 "superficieConstruccion": {
                  "valor": 120,
                  "unidad": "m2"
                },
                
                "formaAdquisicion": {
                  "clave": valores_adquisicion[forma_adquisicion],
                  "valor": forma_adquisicion
                },
                "formaPago": forma_pago,
                "valorAdquisicion": {
                  "valor": 0,
                  "moneda": "MXN"
                },
                }
            ],
            "aclaracionesObservaciones": "Observaciones"
          }
    
    return bienes_dommi
def extraer_datos_curriculares(datos):
    diccionario_escolaridad = {
    "PRIMARIA": "PRI",
    "SECUNDARIA": "SEC",
    "BACHILLERATO": "BCH",
    "CARRERA TÉCNICA O COMERCIAL": "CTC",
    "LICENCIATURA": "LIC",
    "ESPECIALIDAD": "ESP",
    "MAESTRÍA": "MAE",
    "DOCTORADO": "DOC"}
    
    datos_split = datos.split("\n")
    # ! DATO DE PRUEBA PARA VERIFICAR SI ALGUN DATO SE OBTIENE MAL
    nivel_test = datos_split[0].split(':')[1].replace('.', '').strip().upper()
    nivel_obtenido = datos_split[0].split(':')[1].replace('.', '').strip().upper()
    institucion_educativa = datos_split[1].split(':')[1].replace('.', '').strip()
    area_conocimiento = datos_split[2].split(':')[1].replace('.', '').strip()
    estatus =  datos_split[3].split(':')[1].replace('.', '').strip()
    documento = unidecode(datos_split[4].split(':')[1].replace('.', '').strip())
    nivel = "PRIMARIA"
    clave = "PRI"
    for key, value in diccionario_escolaridad.items():
        if unidecode(nivel_obtenido) == unidecode(key):
            nivel = key
            clave = value
            break


    if not documento in ["BOLETA", "CERTIFICADO", "CONSTANCIA", "TÍTULO", "TITULO"]:
        documento = "CERTIFICADO"
    if not estatus in ["CURSANDO", "FINALIZADO", "TRUNCO"]:
        estatus = "FINALIZADO"
    # Todo manejar fechas

    final_data =  {
					"escolaridad": [
						{
							"tipoOperacion": "SIN_CAMBIOS",
							"nivel": {
								"clave": clave,
								"valor": nivel
							},
							"institucionEducativa": {
								"nombre": institucion_educativa,
								"ubicacion": "MX"
							},
                            "carreraAreaConocimiento": area_conocimiento,
							"estatus": estatus,
							"documentoObtenido": documento,
							"fechaObtencion": "2017-11-29"
						}
					],
					"aclaracionesObservaciones": ""
				}

    return final_data
def extraer_datos_adicional(datos):
    diccionario_escolaridad = {
    "PRIMARIA": "PRI",
    "SECUNDARIA": "SEC",
    "BACHILLERATO": "BCH",
    "CARRERA TÉCNICA O COMERCIAL": "CTC",
    "LICENCIATURA": "LIC",
    "ESPECIALIDAD": "ESP",
    "MAESTRÍA": "MAE",
    "DOCTORADO": "DOC"}
    datos_split = datos.split(":")
    nivel = datos_split[-1].rstrip(".").strip().upper()
    nivel_escolaridad = "PRIMARIA"
    clave = "PRI"
    if unidecode(nivel).upper() == unidecode('Licenciatura/Ingeniería').upper():
        nivel_escolaridad = "LICENCIATURA"
        clave = "LIC"
    for key, value in diccionario_escolaridad.items():
        if unidecode(nivel) == unidecode(key):
            nivel_escolaridad = key
            clave = value
            break
    # Todo manejar fechas
    final_data = {
					"escolaridad": [
						{
							"tipoOperacion": "SIN_CAMBIOS",
							"nivel": {
								"clave": clave,
								"valor": nivel_escolaridad
							},
							"institucionEducativa": {
								"nombre": "RESERVADO",
								"ubicacion": "MX"
							},
							"estatus": "FINALIZADO",
							"documentoObtenido": "CERTIFICADO",
							"fechaObtencion": "2017-11-29"
						}
					],
					"aclaracionesObservaciones": ""
				}
    return final_data
def extraer_experiencia_laboral(datos):
     datos_split = datos.split("\n")
     ambito = datos_split[1].split(":")[1].strip().rstrip(".")
     ente_o_empresa = datos_split[2].split(":")[1].strip().rstrip(".")
     ingreso = datos_split[3].split(":")[1].strip().rstrip(".")
     egreso = datos_split[4].split(":")[1].strip().rstrip(".")
     cargo = datos_split[5].split(":")[1].strip().rstrip(".")
     lugar = datos_split[6].split(":")[1].strip().rstrip(".")
     datos_empleo_anterior = {}
     if ambito and ente_o_empresa and ingreso and egreso and cargo and lugar:
        datos_empleo_anterior = {
                "tipoOperacion": "AGREGAR",
                "ambitoSector": {
                  "clave": "PUB",
                  "valor": "Público"
                },
                "nivelOrdenGobierno": "FEDERAL",
                "ambitoPublico": ambito,
                "nombreEntePublico": ente_o_empresa,
                "areaAdscripcion": "Unidad de Concesiones y Servicios",
                "empleoCargoComision": cargo,
                "funcionPrincipal": "",
                "fechaIngreso": ingreso,
                "fechaEgreso": egreso,
                "ubicacion": "MX"
              }

     return(datos_empleo_anterior)

# >4 EXTRAER DECLARACION SERVIDOR
def  declaracion_servidor_datos(url_declaracion_servidor):
    datos_bienes = {
					"ninguno": True,
					"bienInmueble":[],
                    "aclaracionesObservaciones": "Observaciones"
				}
    experiencia_laboral_anterior = {}
    response = requests.get(url_declaracion_servidor)
    sopa = bs4.BeautifulSoup(response.text, 'html.parser')
    tablas_de_datos = sopa.find_all("table")
    for table in tablas_de_datos:
        datos = table.find_all("td")
        titulo = datos[0].text.strip()
        # RFC
        comments = table.find_all(string=lambda text: isinstance(text, bs4.Comment))
        for e in comments:
            if len(e) == 80:
                try:
                    patron = r'\D{4}\d{6}'
                    RFC_search = re.search(patron, e)
                    RFC = RFC_search.group()
                    HC = e[72:75]
                except Exception as e:
                    print(e)
                    RFC ="RFC not found"
                    HC = 'HC nor found'
                    print("RFC not found")
        if len(datos) > 1:
            contenido = datos[1].text
            # Manejo de datos generales
            if titulo == "Datos Generales":
                datos_generales =  extraer_tipo_y_fecha(contenido)
                tipo = datos_generales[0]
                actualizacion = datos_generales[1]
            # Manejo de datos personales
            if titulo == "Datos Personales":
                datos = extraer_nombres(contenido)
                nombre = datos[0]
                primerApellido = datos[1]
                segundoApellido = datos[2]
            # Manejo de datos del puesto
            if titulo == "Datos del Puesto":
                datospuesto = extraer_datos_Puesto(contenido)
                sector = datospuesto["sector"]
                municipio = datospuesto["municipio"]
                dependencia = datospuesto["dependencia"]
                nombre_puesto = datospuesto["nombre_puesto"]
                nivel = datospuesto["iniciales_nivel"]
                clave = datospuesto["clave"]
            # Manejo de ingresos
            if titulo == "Ingresos":
                datos_ingreso_mensual = extraer_datos_ingreso(contenido, tipo)
            # Manejo de datos curriculares
          
            if titulo == "Datos Curriculares (último nivel de estudios)":
                datos_curriculares = extraer_datos_curriculares(contenido)
            elif titulo == "Resumen adicional":
                datos_curriculares = extraer_datos_adicional(contenido)
            if titulo == "Bienes Inmuebles":
                datos_bienes = extraer_bienes(contenido)
            if titulo == "Experiencia Laboral (último empleo)":
               experiencia_laboral_anterior = extraer_experiencia_laboral(contenido)
            if not titulo in ["Conflictos de interés","Experiencia Laboral (último empleo)","Bienes Inmuebles","Datos Personales", "Resumen adicional","Datos Curriculares (último nivel de estudios)", "Ingresos", "Datos del Puesto", "Datos Generales"]:
                titulo_faltante = titulo
                datos_faltantes = contenido
        else:
            # print(f"{titulo} con datos desconcidos"):
            contenido = "Dato Desconocido"
    # Construir aqui los datos

    uuid_declaracion = (uuid.uuid4())
    datos_declaracion = {
		"id": str(uuid_declaracion),
		"metadata": {
			"actualizacion": actualizacion,
			"institucion": dependencia,
			"tipo": tipo,
			"declaracionCompleta": False,
			"actualizacionConflictoInteres": False
		},
		"declaracion": {
			"situacionPatrimonial": {
				"datosGenerales": {
					"nombre": nombre,
					"primerApellido": primerApellido,
					"segundoApellido": segundoApellido
                    
				},
				"datosCurricularesDeclarante": datos_curriculares,
				"datosEmpleoCargoComision": {
					"nivelOrdenGobierno": sector,
					"nombreEntePublico": dependencia,
					"empleoCargoComision": nombre_puesto,
					"nivelEmpleoCargoComision": nivel,
					"domicilioMexico": {
						"municipioAlcaldia": {
							"clave": clave,
							"valor": municipio
						},
						"entidadFederativa": {
							"clave": "05",
							"valor": "COAHUILA DE ZARAGOZA"
						}
					}
				},
				"experienciaLaboral": {
					"ninguno": True,
					"experiencia": [],
					"aclaracionesObservaciones": ""
				},
				"ingresos": datos_ingreso_mensual,
				"actividadAnualAnterior": {
				    "servidorPublicoAnioAnterior": False
				},
				"bienesInmuebles": datos_bienes,
				"vehiculos": {
					"ninguno": True,
					"vehiculo": [{
                        "formaAdquisicion": {
                                "clave": "CPV",
                                "valor": "COMPRAVENTA"
                                }}],
                     "aclaracionesObservaciones": "Observaciones"
				},
				"bienesMuebles": {
					"ninguno": True,
					"bienMueble": [],
                    "aclaracionesObservaciones": "Observaciones"
				}
			},
			"interes": {
				"participacion": {
					"ninguno": True,
					"participacion": [],
					"aclaracionesObservaciones": ""
				},
				"participacionTomaDecisiones": {
					"ninguno": True,
					"participacion": [],
					"aclaracionesObservaciones": ""
				},
				"apoyos": {
					"ninguno": True,
					"apoyo": [],
					"aclaracionesObservaciones": ""
				},
				"representacion": {
					"ninguno": True,
					"representacion": [],
					"aclaracionesObservaciones": ""
				},
				"clientesPrincipales": {
					"ninguno": True,
					"cliente": [],
					"aclaracionesObservaciones": ""
				},
				"beneficiosPrivados": {
					"ninguno": True,
					"beneficio": [],
					"aclaracionesObservaciones": ""
				},
				"fideicomisos": {
					"ninguno": True,
					"fideicomiso": [],
					"aclaracionesObservaciones": ""
				}
			}
		},
        "adicional": {
                            "rfc": RFC,
                            "homoClave": HC,
                            "datos_curriculares": [experiencia_laboral_anterior],
                }
    }
 
    return datos_declaracion
# datos_declaracion_final = declaracion_servidor_datos(url2_declaracion_servidor)
# print(datos_declaracion_final)

#  >4  EXTRAER URL DE CADA SERVIDOR y ESCRIBIR JSON
def declaracion_servidores_dependencias(url_intitucion, dependencia):
    init = time.time()
    response = requests.get(url_intitucion)
    sopa = bs4.BeautifulSoup(response.text, 'html.parser')
    all_data = sopa.find_all("tr")
    declaraciones_por_intitcion = []
    declaraciones_PDN = []
    no_datos_agregados = 0
    no_errores = 0
    print(f"Iniciando extraccion de datos de {dependencia}")
    for e in all_data:
        datos_campos = e.find_all('td')
        if len(datos_campos) > 3:
            try:
                nombre = (datos_campos[0].text).strip()
                apellido_paterno = (datos_campos[1].text).strip()
                apellido_materno = (datos_campos[2].text).strip()
                tipo_declaracion = (datos_campos[3].text).strip()
                referente_date = (datos_campos[4].text).strip()
                url_declaracion = "http://www.declaranetcoahuila.gob.mx:9001/sidp/publica/" + datos_campos[5].a.get('href')
                presentada_date = (datos_campos[6].text).strip()
               
                # >1 RECOLECCION DE DATOS
                datos_declaracion_final = declaracion_servidor_datos(url_declaracion)
                no_datos_agregados += 1
                if no_datos_agregados % 25 == 0:
                    print(no_datos_agregados)
            except Exception as e:
                no_errores += 1
                print(e)
                print(nombre + " " + referente_date)
            datos_declaracion = { 
                'nombre': nombre, 
                'apellido paterno':apellido_paterno, 
                'apellido materno':apellido_materno, 
                'tipo_declaracion' : tipo_declaracion,
                'fecha de referencia': referente_date,
                'url_declaracion': url_declaracion,
                'fecha de presentacion': presentada_date,
                }
           
            declaraciones_PDN.append(datos_declaracion_final)
            # declaraciones_por_intitcion.append(datos_declaracion)
    final = time.time()
    print(f'Entidad: {dependencia}')
    print(f'Declaraciones agregadas: {no_datos_agregados}')
    print(f'Errores: {no_errores}')
    print(f'Tiempo de ejecución: {final - init}')
    with open(f'scrapping sefirc\data\{dependencia}.json', 'w', encoding='utf-8') as file:
        json.dump(declaraciones_PDN, file, ensure_ascii=False, indent=4)
    return(declaraciones_PDN)

# >5 Funcion ejecutora
def init(urls_list: list):
    for e in urls_list:
        url = e['url']
        dependencia = e['dependencia']
        declaracion_servidores_dependencias(url, dependencia)


init(urls_list)



# with open('declaraciones.json', 'w', encoding='utf-8') as file:
#     json.dump(declaraciones_datos_final, file, ensure_ascii=False, indent=4)
# print(declaraciones_datos_final)

# declaraciones_de_intitucion = declaracion_servidor(url_intitucion)
# print(declaraciones_de_intitucion)

# acceder a url
# for e in lista_intitucciones:
#     print(e["url"])

