import abc
from Mongo_gets import MongoRoutines
from pymongo import MongoClient 
import json


class Concrete(MongoRoutines):
	
	def getAll(self):
		jsonOutput = "["

		client = MongoClient() 
		db = client.timeline
		

		collection = db.keypress.find()
		for document in collection:
			document.pop('_id', None)
			jsonOutput = jsonOutput + json.dumps(document)
			jsonOutput = jsonOutput + ","
		jsonOutput = jsonOutput + "]"
		return jsonOutput[:-2] + "]"


	def getAll_byDate(self, frontEnd_instruccion):
		args = mongo_data[11:].split('+')
		jsonOutput = "["

		client = MongoClient() 
		db = client.timeline

		cursor = db.keypress.find( { "$and": [ {"start": {"$gte": args[1]}}, {"start": {"$lte": args[2]} } ] } )
		for document in cursor:
			document.pop('_id', None)
			jsonOutput = jsonOutput + json.dumps(document)
			jsonOutput = jsonOutput + ","
		jsonOutput = jsonOutput + "]"
		return jsonOutput[:-2]+"]"

