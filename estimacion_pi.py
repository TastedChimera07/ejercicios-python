#IMPORTAR MÓDULO "RANDOM".
import random

#PUNTOS A GENERAR. 
INTERVAL= 5000
  
circle_points= 0 #PUNTOS DENTRO DEL CUADRADO 
square_points= 0 #PUNTOS DENTRO DEL CÍRCULO
  
for i in range(INTERVAL**2):

    #GENERACIÓN DE PUNTOS
    rand_x= random.uniform(-1, 1)
    rand_y= random.uniform(-1, 1)
  
    #DISTANCIA DE CADA PUNTO DEL ORIGEN
    origin_dist= rand_x**2 + rand_y**2
  
    #COMPROBAR SI EL PUNTO ESTÁ DENTRO DEL CÍRCULO.
    if origin_dist<= 1:
        circle_points+= 1
  
    square_points+= 1

    #OBTENCIÓN DEL VALOR DE PI.
    pi = 4* circle_points/ square_points

#ESTIMACIÓN FINAL.
print("PI ESTIMATION: ", pi)
