#!/usr/bin/python3.6

f = open('/home/criii/Scrivania/frutta.txt', 'r')

text = ' '
lista = [' ']

while text != '':
	text = f.read(50)
	lista.append(text)

for i in lista:
	print(i)

f.close()

w = open('/home/criii/Scrivania/frutta.txt', 'a')

w.write("aranci\ngogo\ncoco")

f.close()