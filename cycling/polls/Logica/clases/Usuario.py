class Usuario:
	def __init__(self,nombre,apellido,edad,mail,nickname):
		self.nombre = nombre
		self.apellido=apellido
		self.edad=edad
		self.mail=mail
		self.nickname=nickname

	def setNombre(self,nombre):
		self.nombre=nombre

	def setApellido(self,apellido):
		self.apellido=apellido

	def setEdad(self,edad):
		self.edad=edad

	def setMail(self,mail):
		self.mail=mail

	def setNickname(self,nickname):
		self.nickname=nickname

	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getEdad(self):
		return self.edad

	def getMail(self):
		return self.mail

	def getNickname(self):
		return self.nickname

	def setEquipo(self,Equipo):
		self.equipo = Equipo

