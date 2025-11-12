from motoFP import *

ruta = "data/mundial_motofp.csv"

#def test_lee_carreras():
 #   carreras = lee_carreras(ruta)
  #  print(f"Las dos primeras carreras son: {carreras[0:2]}, las dos últimas carreras son: {carreras[-2:]}")

def test_piloto_mas_podios_por_circuito():
    carreras = lee_carreras(ruta)
    resultado = piloto_mas_podios_por_circuito(carreras)
    print("Piloto con más podios por circuito:", resultado)
    
def test_escuderias_con_solo_un_piloto():
    carreras = lee_carreras(ruta)
    resultado = escuderias_con_solo_un_piloto(carreras)
    print("Escuderías con solo un piloto:", resultado)


    
def test_piloto_racha_mas_larga():
    carreras = lee_carreras(ruta)
    resultado = piloto_racha_mas_larga_victorias_consecutivas(carreras, año= None)
    print(resultado)

def funcion_principal():
    # test_lee_carreras()
    #test_piloto_mas_podios_por_circuito()
    #test_escuderias_con_solo_un_piloto()
    test_piloto_racha_mas_larga()

if __name__ == "__main__":
    funcion_principal()
