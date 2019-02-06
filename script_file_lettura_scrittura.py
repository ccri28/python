#!/usr/bin/python3.6

w = open('/home/criii/Scrivania/file.txt','a')

parole = input("Quante parole vuoi aggiungere al file? ")

for i in range (int(parole)):
	parola = input("Inserisci parola: ")
	w.write(parola + "\n")

w.close()

print("\n\n\nNel file hai scritto le seguenti parole: \n")

r = open('/home/criii/Scrivania/file.txt','r')

text = ' '
lista = [' ']

while text != '':
	text = r.read(50)
	lista.append(text)

for i in lista:
	print(i)

r.close()
