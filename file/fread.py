try:
    f = open("file.txt","r")
    for x in f:
        print("\n"+x)
except:
    print("ERRORE FILE! Qualcosa è andato storto :(")
finally:
    f.close()