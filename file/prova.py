print("Ciao! Come ti chiami? ")
nome = input()
print("Ok" + nome + ", quanti anni hai? ")
eta = input()

try:
    f = open("dati.txt","w")
    f.write(f"Nome: {nome} \nEtà: {eta} \n---------------------")
except:
    print("ERRORE FILE! Controlla bene il file! :D")
finally:
    f.close()