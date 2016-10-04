import abc
from Mongo_Routines import MongoRoutines
from pymongo import MongoClient 
import json


class Concrete_getAll_DATE(MongoRoutines):
    
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


MongoRoutines.register(Concrete_getAll_DATE)

if __name__ == '__main__':
	
	

	instruction = "getAll" #dummy instruction, this should be obtainded from jsoncontract

	if instruction == "getAll":
		sample = Concrete_getAll_DATE()
		print sample.getAll(instruction)