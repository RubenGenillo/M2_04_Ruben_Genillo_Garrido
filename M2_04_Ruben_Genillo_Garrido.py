
#1.1
from typing import Set


lista = ["cinco","dos","tres","siete"]
tupla = ("hola", "buenas", "que tal","encantado")
#???
print(lista)
print(tupla)
#
print(lista[1])
print(tupla[-2])
#(las tuplas son inmutables por lo que no puedo modificar ningún elemento suyo)
lista[3] = "cuatro"
print(lista[3])

#
print("Tamaño de la lista:", len(lista))
print("Tamaño de la tupla:", len(tupla))
#
print("¿Esta cinco en la lista?:", "cinco" in lista)
print("¿Esta adios en la tupla:?", "adios" in tupla)

#(Por ser inmutable no puedo añadir elemetos a la tupla)
lista.append("siete")
print(lista)

#CAMBIALO PERO AQUÏ TIENES VARIAS FORMAS DE HACERLO, PERO CREO QUE SOLO TE PIDE QUE BORRES TODO ASÏ QUE... (haz una funcion seguro le intersa)
tupla = ("hola")
print(tupla)
tupla = ("buenas") + tupla

lista.clear()
tupla = ()
print(lista)
print(tupla)



#Tambien podrias hacer con el diccionario el for(mira distintas maneras de mostrar elementos en pantalla)
conjuntoletras = {"a","b","c","d"}
diccionario = {
    "primero":"Lunes",
    "segundo":"martes",
    "tercero":"miércoles",
    "cuarto":"jueves"
}

#
print(conjuntoletras)
print(diccionario)

#Los valores de los sets están desordenados,(por lo que no hay un segundo elemnto) por lo que no puedes buscar un elemento por su indice, (podria transformarlo en una lista, pero saldrian elemntos aleatoriamente (probablemente debido al desorden)(osea que cada vez que los llamo es distinto))
listletras = list(conjuntoletras)
print(listletras[0])
print(diccionario["primero"])