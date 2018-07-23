import sys 
sys.path.insert(0,'/home/martin/proyectopython/cyclingproject/logica/clases')
sys.path.insert(0,'/home/martin/proyectopython/cyclingproject/persistencia')
from Usuario import *
from manejadorUsuario import *

class CtrlUsuario():
	
	__instance = None
    
    

	@staticmethod
	def getInstance():
		if CtrlUsuario.__instance == None:
			CtrlUsuario()
		return CtrlUsuario.__instance

	def __init__(self):
		CtrlUsuario.__instance = self


	def registrarUsuario(self,nombre,apellido,edad,mail,nickname):

		nuevoUs = Usuario(nombre,apellido,edad,mail,nickname)
		mjUs = manejadorUsuarios() 
		mjUs.guardarUsuarios(nuevoUs)





