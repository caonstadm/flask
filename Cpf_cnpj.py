class Cpf_cnpj:
	def __init__(self, documento):
		documento = str(documento)
		if self.Cpf_cnpj_he_Valido(documento):
			self.Cpf_cnpj = documento
		else:
			raise ValueError('Nok')

	def Cpf_cnpj_he_Valido(self, documento):
		if len(documento) == 11:
			return True  
		else:
			return False

