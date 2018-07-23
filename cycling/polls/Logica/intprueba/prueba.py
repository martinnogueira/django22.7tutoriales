import sys 
sys.path.insert(0,'/home/martin/proyectopython/cyclingproject/logica/controladores')
from CtrlUsuario import *

print ("ingrese un Usuario")

print ("nombre,apellido,edad,mail,nickname")

nombre = input()
apellido=input()
edad=input()
mail=input()
nickname=input()

ctrlus = CtrlUsuario.getInstance()
ctrlus.registrarUsuario(nombre,apellido,edad,mail,nickname)

print ("usuario ingresado" + nombre)



