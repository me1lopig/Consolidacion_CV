# calculo de el Cv según el método computacional de Sivaram
# A computational method for consolidation coefficient
# B.Sivaram and Prabhata, R Swamee
# The Japanese Geotechnical Society
# September 1976

import math

# entrada de los datos del ensayo

d1=float(input("Lectura 1 de la zona de inicio de la consolidacion "))
t1=float(input("Tiempo 1 de la zona de inicio de la consolidacion "))

d2=float(input("Lectura 2 de la zona de inicio de la consolidacion "))
t2=float(input("Tiempo 2 de la zona de inicio de la consolidacion "))

d3=float(input("Lectura 3 de la zona final de la consolidacion "))
t3=float(input("Tiempo 3 de la zona final de la consolidacion "))

hd=float(input("Distancia de drenaje "))


# procesado de los datos cálculos intermedios
rt=(d1-d2*math.sqrt(t1/t2))/(1-math.sqrt(t1/t2))
rf=rt-(rt-d3)/(1-((rt-d3)*(math.sqrt(t2)-math.sqrt(t1))/((d1-d2)*math.sqrt(t3)))**5.6)**0.179

# cálculo del Coeficiente de consolidacion
cv=math.pi*0.25*((d1-d2)*hd/((rt-rf)*(math.sqrt(t2)-math.sqrt(t1))))**2

# impresion de resultados
print("Rt=",rt)
print("Rf=",rf)
print("Cv=",cv)

