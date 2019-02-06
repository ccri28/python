#!/usr/bin/python3.6

def sommatoria(valori):
	somma = 0
	for i in range(int(valori) + 1):
		somma += i
	return somma


valori = input("Quanti valori vuoi inserire? ")

print(f"Somma totale: {sommatoria(valori)}")