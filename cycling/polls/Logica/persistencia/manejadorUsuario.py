import sys 
sys.path.insert(0,'/home/martin/proyectopython/cyclingproject/logica/clases')
from Usuario import *

import pickle
class manejadorUsuarios:
	def __init__(self):
		return

	def guardarUsuarios(self,Usuario):
		with open(Usuario.getNombre() + Usuario.getApellido() + '.pickle', 'wb') as handle:
			pickle.dump(Usuario, handle, protocol=pickle.HIGHEST_PROTOCOL)

		
