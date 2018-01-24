method(self, molecule):
	data = thermo(molecule)
	return data

coolmethod(species):
	ask_for_cool_thermo(species)
	return True
	
method2(self, molecule):
	data = thermo(molecule)
	return data
	
