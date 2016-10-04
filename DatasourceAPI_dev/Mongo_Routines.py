import abc


class MongoRoutines(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def getAll(self, mongo_data):
		print 'in base clase, getall'
		return

	@abc.abstractmethod
	def getAll_byDate(self, mongo_data):
		print 'in base clase, getbydate'
		return 




