#!/usr/bin/python3.6

f = open("/home/criii/Scrivania/file2.py", "w")

print("Writting in file ...")
print("0%")
print("25%")
print("50%")
print("75%")
print("100%")
f.write("Ciao a tutti!")
print("Done with writting!")

f.close()
