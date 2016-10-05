import abc
from Mongo_sets import MongoRoutines
from pymongo import MongoClient 
import json


class Concrete(MongoRoutines):
	
	def setContent(self,content):
		return content


	def setDate(self,date):
		return date



MongoRoutines.register(Concrete)

if __name__ == '__main__':
	sample = Concrete()
	

	instruction = "setContent" #dummy instruction, this should be obtainded from jsoncontract

	if instruction == "setAll":
		print sample.getContent(instruction)
	elif instruction.startswith("setDate"):
		byDateparameters = "getKpressed+Thu Jun 09 17:38:40 MDT 2016+Thu Jun 09 17:38:50 MDT 2016"
		print sample.setDate(byDateparameters)