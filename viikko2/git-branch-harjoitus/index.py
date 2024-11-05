from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo

<<<<<<< HEAD
logger("aloitetaan ohjelma")
=======
logger("aloitetaan! ohjelma") # muutos mainissa
>>>>>>> d195904 (Modified index in local copy 2)

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") 
print(f"{x} - {y} = {erotus(x, y)}") 
print(f"{x} * {y} = {tulo(x, y)}") 

logger("lopetetaan")
print("goodbye!!")