from pymongo import MongoClient
import json



def main():
	client = MongoClient()
	db = client.timeline

	while 1:

		instruction = raw_input()

		if instruction == "getAll":
			jsonOutput = "["
			cursor = db.keypress.find()
			for document in cursor:
				document.pop('_id', None)
				jsonOutput = jsonOutput + json.dumps(document)
				jsonOutput = jsonOutput + ","
			jsonOutput = jsonOutput + "]"
			print(jsonOutput[:-2]+"]")

		elif instruction.startswith("getKpressed"):
			args = instruction[11:].split('+')
			jsonOutput = "["
			cursor = db.keypress.find( { "$and": [ {"start": {"$gte": args[1]}}, {"start": {"$lte": args[2]} } ] } )
			for document in cursor:
				document.pop('_id', None)
				jsonOutput = jsonOutput + json.dumps(document)
				jsonOutput = jsonOutput + ","
			jsonOutput = jsonOutput + "]"
			print(jsonOutput[:-2]+"]")


if __name__ == '__main__':
	main()
