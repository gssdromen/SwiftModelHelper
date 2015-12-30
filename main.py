# coding:UTF-8

import os

def mapping():
	vars = []
	with open("./a.txt", "r") as file:
		for line in file:
			text = line.strip()
			if text[0:3] == "var" or text[0:3] == "let":
				vars.append(text[4:].split(":")[0])

	for item in vars:
		print "self." + item + " <- " + 'map["' + item + '"]'

def nscoding():
	vars = []
	types = []
	with open("./a.txt", "r") as file:
		for line in file:
			text = line.strip()
			if text[0:3] == "var" or text[0:3] == "let":
				vars.append(text[4:].split(":")[0])
				temp = text[4:].split(":")[1].strip().split(" ")[0].strip()
				if temp[len(temp) - 1] == "!" or temp[len(temp) - 1] == "?":
					types.append(temp[:len(temp) - 1])
				else:
					types.append(temp)
	if len(vars) == len(types):
		count = len(types)
		for i in xrange(count):
			if types[i] in ["String"]:
				print 'aCoder.encodeObject(self.' + vars[i] + 'forKey: "' + vars[i] + '")'
			elif types[i] == "Int":
				print 'aCoder.encodeInteger(self.' + vars[i] + 'forKey: "' + vars[i] + '")'
			else:
				print 'aCoder.encode' + types[i] + '(self.' + vars[i] + 'forKey: "' + vars[i] + '")'
		print "==========================="
		for i in xrange(count):
			if types[i] in ["String"]:
				print 'self.' + vars[i] + ' = aDecoder.decodeObjectForKey("' + vars[i] + '") as! ' + types[i]
			elif types[i] == "Int":
				print 'self.' + vars[i] + ' = aDecoder.decodeIntegerForKey("' + vars[i] + '") as! ' + types[i]
			else:
				print 'self.' + vars[i] + ' = aDecoder.decode' + types[i] + 'ForKey("' + vars[i] + '") as! ' + types[i]
	else:
		print "count error"

def nscopying():
	vars = []
	types = []
	with open("./a.txt", "r") as file:
		for line in file:
			text = line.strip()
			if text[0:3] == "var" or text[0:3] == "let":
				vars.append(text[4:].split(":")[0])

	for item in vars:
		print "newInstance." + item + " = " + 'self.' + item

while True:
	print "1 for func mapping"
	print "2 for NSCoding"
	print "3 for NSCopying"
	command = int(raw_input("command number: "))
	if command == 1:
		mapping()
	elif command == 2:
		nscoding()
	elif command == 3:
		nscopying()

