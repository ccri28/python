import os

if os.path.exists("file1.txt"):
    os.remove("file1.txt")
    print("File eliminato correttamente! ;)")
else:
    print("Il file da eliminare, non esiste!")