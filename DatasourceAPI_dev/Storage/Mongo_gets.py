import abc


class MongoRoutines(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def getAll(self):
		print 'interface; getall'
		return

	@abc.abstractmethod
	def getAll_byDate(self, frontEnd_instruccion):
		print 'interface; getbydate'
		return

	# interface signatures for more function
	# .....
	# .....



