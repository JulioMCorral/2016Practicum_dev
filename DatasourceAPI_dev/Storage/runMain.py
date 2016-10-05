from Mongo_gets import MongoRoutines
from Build_gets import Concrete


MongoRoutines.register(Concrete)

if __name__ == '__main__':
	sample = Concrete()
	

	instruction = "getAll" #dummy instruction, this should be obtainded from jsoncontract

	if instruction == "getAll":
		print sample.getAll()
	elif instruction.startswith("getKpressed"):
		byDateparameters = "getKpressed+Thu Jun 09 17:38:40 MDT 2016+Thu Jun 09 17:38:50 MDT 2016"
		print sample.getAll_byDate(byDateparameters)