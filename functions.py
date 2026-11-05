def isfloat(value):
	if value.replace(".","",1).replace("-","",1).isdigit():
		return True
	return False

def isPositiveFloat(value):
    if value.replace(".","",1).isdigit():
        return True
    return False

def isinteger(value):
	while not value.isdigit():
		value = input(error)
	return int(value)

