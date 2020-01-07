import random
from random import choice
#Programa 03
#Brandon Padilla Ruiz
#312139805
class valores:
     def __init__(self,n):
          self.value = None
          self.id = (choice(range(n)))

class clausula:
     def __init__(self,n):
          self.asignacion = [valores(n),valores(n),valores(n)]
          

     def __str__(self):
          lista = []
          for i in self.asignacion:
               lista.append(i.value)
          return str(lista)

     def esVerdadera(self):
          count = []
          for i in self.asignacion:
               if i.value == 1:
                    count.append(i.value)
          if len(count) > 0:
               return True
          else:
               return False
          

     
def creaMatriz(n,m):
      matriz = []
      for i in range(n):
           a = [0]*m
           matriz.append(a)
      return matriz

def matrizstr(matriz):
     cadena = ''
     for i in range(len(matriz)):
         cadena += '['
         for j in range(len(matriz[i])):
             cadena += '{:>4s}'.format(str(matriz[i][j]))
         cadena += ']\n'
     return cadena

def llenaMatriz():
     for i in range(len(matriz)):
         for j in range(len(matriz[i])):
             matriz[i][j] = clausula()
               
     
def calculaVar(matriz,listaPob):
     fitness = [] 
     for i in range(len(matriz)):
         for j in range(len(matriz[i])):
             for k in matriz[i][j].asignacion:
                  if(k.value == 1 and listaPob[k.id] == 1):
                       fitness.append(k.id)
     return list(set(fitness))

def getIds(matriz,poblacion):
     for i in range(len(matriz)):
         for j in range(len(matriz[i])):
             for k in matriz[i][j].asignacion:
                  if poblacion[k.id] == 1:
                       k.value = 1
                  else:
                       k.value = 0
     return matriz

#Funcion que calcula la aptitud de cada individuo
def calculaFitness(aux,listaPob):
     matriz = getIds(aux,listaPob)
     fitness = 0
     for i in range(len(matriz)):
          for j in range(len(matriz[i])):
               if(matriz[i][j].esVerdadera()):
                    fitness+=1
     return fitness

#Cruces

#Partially Mapped Crossover
def PMC(poblacion, padres):
     x = random.randrange(21,70)
     y = x+10
     aux = poblacion
     a = padres
     for i in range(20,x):
          poblacion[i] = a[i]
     for j in range(30,y):
          padres[j] = aux[j]      
     return padres

#Order Crossover, toma un elemento de la población  y un elemento de los padres y hace el intercambio
#Hace el cruce sin alterar el orden, solo devuelve un conjunto
def OrderC(poblacion,padres):
     x = random.randrange(0,50)
     padres[x] = poblacion[x]
     return padres
          
     
#Mutaciones

#Displacement Mutation, toma un subconjunto de la poblacion y lo deslaplaza
#para hacerlo de forma mas sencilla se desplazará hacia el final
def disMutation(poblacion):
     x = random.randrange(10,20)
     aux = poblacion[5:x]
     del poblacion[5:x]
     poblacion.extend(aux)
     return poblacion

#Exchange Mutation, toma dos elementos de la poblacion y los intercambia de lugar
def exMutation(poblacion):
     n = random.randrange(len(poblacion)-1)
     m = random.randrange(len(poblacion)-1)
     x = poblacion[n]
     y = poblacion[m]
     aux = y
     poblacion[m] = x
     poblacion[n] = aux
     return poblacion


     

 
#Algoritmo genetico para el problema MAX-SAT
#clau = clausula(50)
#print(clau)
#print(clau.esVerdadera())
print("¿Cuantas cláusulas desea ingresar? (ingrese un número mayor o igual a 50 y menor igual a 60)")
m = int(input())
if(m < 50 or m > 60):
     print("número incorrecto, vuelva a ingresar un número que sea correcto")
     m = int(input())
print("¿Cuantas variables desea ingresar? (ingrese un número mayor o igual a 100)")
n = int(input())
if(n < 100):
     print("número incorrecto, vuelva a ingresar un número que sea correcto")
     n = int(input())
#Codificación
matriz = creaMatriz(m,n)
for i in range(len(matriz)):
     for j in range(len(matriz[i])):
          matriz[i][j] = clausula(n)          
#print(matrizstr(matriz))
#Creacion de la poblacion inicial
poblacion = []
for i in range(n):
     if i%2 == 0:
          poblacion.append(0)
     elif i%2 != 0:
          poblacion.append(1)
#print("poblacion inicial:")     
#print(poblacion)
#b = calculaFitness(matriz,poblacion)
#a = calculaVar(matriz,poblacion)
#print("Valores fitness")
#print(a)
#print("Fitness:"+str(b))
print("Número de iteraciones que desea hacer: ")
a = int(input())
print("Se harán "+str(a)+" iteraciones")
padres = []
for i in range(n):
     padres.append(random.randrange(0,2))
print("Lista de padres:")
print(padres)     
i = 0
maximo = 0
num = 0
while i < a: #condición de temrinación
     print("iteración:"+" "+str(i+1))
     x = random.randrange(0,2)
     print("poblacion: ")
     print(poblacion)
     if x == 0:
          #print("Se utilizó Partially Mapped CrossOver")
          poblacion = PMC(poblacion,padres)
     elif x == 1:
          #print("Se utilizó Order CrossOver")
          poblacion = OrderC(poblacion,padres)                
     y =  random.randrange(0,11)
     if(y == 1 or y == 2):
          disMutation(poblacion)
          #print("Se hizo un mutacion")
     elif(y == 3 or y == 4):
          exMutation(poblacion)
          #print("Se hizo una mutacion")
     values = calculaFitness(matriz,poblacion)
     if(maximo<values):
          maximo = values
          num = i
     print("Fitness: "+str(values))     
     i += 1.
print(" ")     
print("La mejor aptitud fue de "+str(maximo)+" en la iteración: "+str(num))     

     
     






    






    

    
        
            
    


