
#Creo una lista y una tupla con al menos tres elementos que contengan strings
lista = ["cinco","dos","tres","siete"]
tupla = ("hola", "buenas", "que tal","encantado")

#Muestro la lista y la tupla
print(lista) #['cinco', 'dos', 'tres', 'siete']
print(tupla) #('hola', 'buenas', 'que tal', 'encantado')

#Muestro el segundo elemento de la lista y el penultimo de la tupla
print(lista[1]) #dos
print(tupla[-2]) #que tal

#Modifico un elemento de la lista y de la tupla(si se puede), y muestro el resultado
lista[3] = "cuatro"
print(lista[3]) #cuatro
#Las tuplas son inmutables por lo que no se puede modificar 
#Aunque también se podría hacer una lista con los mismos elementos, 
#modificar el elemento y luego cambiar la tupla entera por la lista

#Muestro el tamaño  de la lista y tupla
print("Tamaño de la lista:", len(lista)) #Tamaño de la lista: 4
print("Tamaño de la tupla:", len(tupla)) #Tamaño de la tupla: 4

#Busco si existe un elemento dentro de la lista y tupla
print("¿Esta cinco en la lista?:", "cinco" in lista) #¿Esta cinco en la lista?: True
print("¿Esta adios en la tupla:?", "adios" in tupla) #¿Esta adios en la tupla:? False

#Añado (si se puede) un elemento a la lista y tupla, y lo muestro
lista.append("siete")
print(lista) #['cinco', 'dos', 'tres', 'cuatro', 'siete']
# Por ser inmutable no puedo añadir elemetos a la tupla
# pero si puedo reemplazar el valor actual por otro igual con elemento añadido

#Borro el contenido de la lista y de la tupla
lista.clear()
tupla = ()
print(lista) #[]
print(tupla) #()


#Creo un set y un diccionario con al menos tres elementos para el set y conjuntos claves:valor para el diccionario
conjuntoletras = {"a","b","c","d"}
diccionario = {
    "primero":"Lunes",
    "segundo":"martes",
    "tercero":"miércoles",
    "cuarto":"jueves"
}

#Muestro el set y el diccionario
print(conjuntoletras)
print(diccionario) #{'primero': 'Lunes', 'segundo': 'martes', 'tercero': 'miércoles', 'cuarto': 'jueves'}

#Muestro (si se puede) el segundo elemento del set y el primer clave-valor del diccionario 
print(diccionario["primero"]) #Lunes
#Los valores de los sets están desordenados,
#por lo que no hay un segundo elemento 

#Modifico (si se puede) algún elemento del set o del diccionario
conjuntoletras.discard("a")
conjuntoletras.add("g")
diccionario["tercero"] = "libre"
print(conjuntoletras)
print(diccionario) #{'primero': 'Lunes', 'segundo': 'martes', 'tercero': 'libre', 'cuarto': 'jueves'}
#Los sets no soportan item assignment, 
#pero si puedo quitar el elemento y añadir el elemento modificado 

#Muestro el tamaño del set y diccionario
print("El tamaño del set es:", len(conjuntoletras)) #El tamaño del set es: 4
print("El tamaño del diccionario es:", len(diccionario)) #El tamaño del diccionario es: 4

#Hago una busqueda dentro del set y el diccionario y muestro si es True o False
print("¿Existe a dentro del conjuntoletras?:", "a" in conjuntoletras) #¿Existe a dentro del conjuntoletras?: False
print("¿Existe la clase segundo en diccionario?:", "segundo" in diccionario) #¿Existe la clase segundo en diccionario?: True

#Añado (si se puede) algún elemento al set y algún clave-valor al diccionario, y lo muestro
conjuntoletras.add("w")
diccionario["quinto"] = "viernes"
print(conjuntoletras) #{'g', 'b', 'c', 'w', 'd'}
print(diccionario) #{'primero': 'Lunes', 'segundo': 'martes', 'tercero': 'libre', 'cuarto': 'jueves', 'quinto': 'viernes'}

#Borro el contenido del set y del diccionario, y lo muestro de nuevo
conjuntoletras.clear()
diccionario.clear()
print(conjuntoletras) #set()
print(diccionario) #{}

#3.
def pedirFloat(pre):
    try: 
        num = float(input(pre))
    except:
        pedirFloat(pre)
    else:    
     return num     

num1 = pedirFloat("Dame un número: ")
num2 = pedirFloat("Dame otro número: ")
num3 = pedirFloat("Dame un último número: ")
listaejer = [num1, num2, num3]
sumatorio = sum(listaejer)
print(sumatorio)

#4.
def mediaAritmetica(x):
    return sum(x)/len(x)
print(mediaAritmetica(listaejer))