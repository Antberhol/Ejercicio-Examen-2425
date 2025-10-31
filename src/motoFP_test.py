from motoFP import *

ruta = "data/mundial_motofp.csv"
def test_lee_carreras():
    carreras= lee_carreras(ruta)
    
    print("las dos primeras carreras son:{carreras[0:2]}, las dos ultimas carreras son:{carreras[-2:]1}")
    
    
def funcion_principal():
   test_lee_carreras()
   
   
if __name__ == "__main__":
    funcion_principal()
     
