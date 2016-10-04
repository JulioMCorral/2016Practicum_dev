import abc
from Mongo_Routines import MongoRoutines
from pymongo import MongoClient 
import json


class Concrete(MongoRoutines):
	
	def getAll(self,mongo_data):
		jsonOutput = "["

		client = MongoClient() #might be singleton
		db = client.timeline
		

		collection = db.keypress.find()
		for document in collection:
			document.pop('_id', None)
			jsonOutput = jsonOutput + json.dumps(document)
			jsonOutput = jsonOutput + ","
		jsonOutput = jsonOutput + "]"
		return jsonOutput[:-2] + "]"


	def getAll_byDate(self,mongo_data):
		args = mongo_data[11:].split('+')
		jsonOutput = "["

		client = MongoClient() #might be singleton
		db = client.timeline

		cursor = db.keypress.find( { "$and": [ {"start": {"$gte": args[1]}}, {"start": {"$lte": args[2]} } ] } )
		for document in cursor:
			document.pop('_id', None)
			jsonOutput = jsonOutput + json.dumps(document)
			jsonOutput = jsonOutput + ","
		jsonOutput = jsonOutput + "]"
		return jsonOutput[:-2]+"]"



MongoRoutines.register(Concrete)

if __name__ == '__main__':
	sample = Concrete()
	

	instruction = "getAll" #dummy instruction, this should be obtainded from jsoncontract

	if instruction == "getAll":
		print sample.getAll(instruction)
	elif instruction.startswith("getKpressed"):
		byDateparameters = "getKpressed+Thu Jun 09 17:38:40 MDT 2016+Thu Jun 09 17:38:50 MDT 2016"
		print sample.getAll_byDate(byDateparameters)