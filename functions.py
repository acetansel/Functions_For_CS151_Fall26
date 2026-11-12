def isFloat(value):
	if value.replace(".","",1).replace("-","",1).isdigit():
		return True
	return False

def isPositiveFloat(value):
    if value.replace(".","",1).isdigit():
        return True
    return False

def isInteger(value, errorMessage):
	while not value.isdigit():
		value = input(errorMessage)
	return int(value)

def isString(entry, validOptions, errorMessage):
	while not entry in validOptions:
		entry = input(errorMessage).strip().lower()
	return entry

def giveFile(errorMessage):
	while True:
		try:
			filename = input()
			return filename
		except FileNotFoundError:
			filename = input(errorMessage)
