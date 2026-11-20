def toContinue():
	input("Return to continue...")
def lineout():
	print("-" * 50)
	return "-" * 50
def toLoop():
	input("This program will now restart on the next key")
def isFloat(value):
	if value.replace(".","",1).replace("-","",1).isdigit():
		return True
	return False
def inputInteger(error):
	number = input()
	while not isFloat(number):
		number = input(error)
	return int(number)
def inputString(options, error):
	entry = input().strip()
	while not entry in options:
		entry = input(error).strip().lower()
	return entry
def inputFile(error):
	while True:
		try:
			filename = open(input())
			return filename
		except FileNotFoundError:
			filename = open(input(error))
def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
def filetoTwoVarList(fileInQuestion, splittingItem):
	list = []
	for line in fileInQuestion:
		list.append(line.split(splittingItem).strip("\n"))
	return list
def leninput(string):
	if len(input(string)) > 0:
		return False
	return True
def randomize(deck):
	import random
	newdeck = []
	for iteration in deck[:]:
		newdeck.append(deck.pop(random.randint(0,len(deck))))
	return newdeck