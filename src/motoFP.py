from typing import NamedTuple
from datetime import datetime
import csv
from typing import List 
from collections import defaultdict

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])


def lee_carreras(ruta_archivo: str) -> List[CarreraFP]:
    lista_carreras= []
   
    with open(ruta_archivo, 'r' ,encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for campos in lector:
                fecha_hora = datetime.strptime(campos[0], '%Y-%m-%d %H:%M')
                circuito =campos[1]
                pais = campos[2]
                seco = campos[3].strip().lower() == 'true'
                tiempo = float(campos[4])
                piloto1=campos[5]
                escuderia1=campos[6]
                piloto2=campos[7]
                escuderia2=campos[8]
                piloto3=campos[9]
                escuderia3=campos[10]
                podios=[Piloto(piloto1, escuderia1), Piloto(piloto2, escuderia2), Piloto(piloto3, escuderia3)]      
                carrera = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podios)
                lista_carreras.append(carrera)
                        
        return lista_carreras
"""

Devuelve el tiempo máximo (en días)ç
que `nombre_piloto` estuvo sin ganar una carrera.
Es decir, el número máximo de días transcurridos entre dos
carreras ganadas por el piloto. Si el piloto no ha ganado al menos dos carreras,
la función debe devolver `None`.
"""
def dias_entre_fechas(fecha1: datetime, fecha2: datetime) -> int:
        dias= (fecha2 - fecha1).days
        return dias
def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int|None:
        fechas_ganadas= []
        lista_dias= []  
        
        for carrera in carreras:
            if carrera.podio[0].nombre== nombre_piloto:
                fechas_ganadas.append(carrera.fecha_hora)
        if len(fechas_ganadas)<2: 
            return None
        fechas_ganadas.sort()
        
        for r in range(len(fechas_ganadas)-1):
                dias = dias_entre_fechas(fechas_ganadas[r], fechas_ganadas[r+1])
                lista_dias.append(dias)
        
        return max(lista_dias)

"""
Devuelve un diccionario que a cada circuito le hace corresponder el nombre del piloto que
    más veces ha estado en el podio en ese circuito.

    """

def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str, str]:
    podios_por_circuito = {}

    for carrera in carreras:
        circuito = carrera.circuito

        if circuito not in podios_por_circuito:
            podios_por_circuito[circuito] = {}

        for piloto in carrera.podio:
            nombre = piloto.nombre
            if nombre not in podios_por_circuito[circuito]:
                podios_por_circuito[circuito][nombre] = 0
            podios_por_circuito[circuito][nombre] += 1

    resultado = {}
    for circuito, contador_podios in podios_por_circuito.items():
        piloto_top = max(contador_podios.items(), key=lambda x:x[1])[0]
        resultado[circuito] = piloto_top

    return resultado

    """
    
    Devuelve una lista con las escuderías que solo tienen un piloto.
    """
    
def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]:
    escuderias = defaultdict(set)
    resultado = []
    for carrera in carreras:
        for piloto in carrera.podio:
            escuderia = piloto.escuderia.strip()
            nombre_piloto = piloto.nombre.strip()
            escuderias[escuderia].add(nombre_piloto)   
    
    for escuderia, pilotos in escuderias.items():
        if len(pilotos)==1:
            resultado.append(escuderia)
    return resultado


def piloto_racha_mas_larga_victorias_consecutivas(carreras: list[CarreraFP], año: int|None = None) -> tuple[str, int]:
    resultado = defaultdict(list)
    racha_max = 0
    piloto_top = ""
    
    carreras_ordenadas = sorted(carreras, key=lambda x: x.fecha_hora)
    
    for carrera in carreras_ordenadas:
        if año is None or carrera.fecha_hora.year == año:
            if carrera.podio:  # aseguramos que hay podio
                ganador = carrera.podio[0].nombre
                for piloto in carrera.podio:
                    nombre = piloto.nombre
                    resultado[nombre].append(nombre == ganador)  # True si ganó, False si no

    for piloto in resultado:
        resultados = resultado[piloto]
        racha_actual = 0
        racha_max_piloto = 0
        for r in resultados:
            if r==True:
                racha_actual += 1
                if racha_actual > racha_max_piloto:
                    racha_max_piloto = racha_actual
            else:
                racha_actual = 0

        if racha_max_piloto > racha_max:
            racha_max = racha_max_piloto
            piloto_top = piloto
            
    return (piloto_top, racha_max)              
            