import random
lista = [1,2,3,4,5,6,7,8,9,10]
aleatorio = random.choice(lista)
cuenta = 11
hasPaintedPoints = False
print("Has encontrado una bomba y para desactivarla tienes que cortar uno de los diez cables, ¿cual cortas?")

while cuenta >= 0:
 intento = float(input("¿Cual cortas?"))

 if intento != aleatorio:
    cuenta-=1
    print(cuenta)
 elif intento == aleatorio:
   print("Bien, nos has salvado a todos")
   break  
 if (cuenta < 8 and cuenta >2):
   if not hasPaintedPoints:
     print("...")
     hasPaintedPoints = True
     continue
  
 if cuenta == 0:
   print("BOOOOM has muerto")

 
