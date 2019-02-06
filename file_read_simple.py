#!/usr/bin/python3.6

f = open("/home/criii/Scrivania/script.py","r")

text = ' '

#leggi fino a quando non trovi riga vuota
while text != '':
	# leggi i primi 100 bytes per ogni riga
	text = f.read(50)
	print (text)

f.close()