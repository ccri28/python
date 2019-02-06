#!/usr/bin/python3.6

# apro il file 
file = open("/home/criii/Scrivania/file.txt","r")

#dichiaro una riga e una lista vuota
riga = ' '
lista =[' ']

#finche' non trovo vuoto, leggo ogni riga e la salvo nella lista
while riga != '':
	riga = file.read(50)
	lista.append(riga)

#scandisco la lista e stampo ogni suo elemento 
for i in lista:
	print(i)

#dopo aver concluso l'operazione di lettura, chiudo il file
file.close()