#!/usr/bin/python2

#importo i moduli 

import os, nmap

#dichiaro le variabili

#PortScanner e' la classe che si trova all'interno del modulo nmap
oggetto = nmap.PortScanner()
#queste sono le porte che vogliamo analizzare
#in questo caso vogliamo analizzare le porte che vanno da 20 a 80
porte = '20-80'
devices = ''

#ottengo i device presenti nella rete
print("Getting devices from network...")
#pip open, per introdurre il comando nel bash
#attraverso pipopen io trasmetto al SO un comando e con il metodo read prendo questi dati ottenuti e li metto nella variabile devices
devices = os.popen('arp -n | cut -f1 -d \' \' | grep [0-9]').read()
#split e' un metodo delle stringhe, che in questo caso ci permette di dividere togliendo i new line (\n) presenti dopo ogni riga 
devices = devices.split('\n')
#non facciamo vedere l'ultimo elemento della lista, ne nostro caso l'ultimo elemento e' ''
devices = devices[:-1]

print(devices)

print("Waiting to scan...")

nr = 1
for ip in devices:
	print ("Scanning device " + str(nr))
	res = oggetto.scan(ip, porte)
	print(res)
	nr += 1
	print ("\n\n")

print("Scan is done!")