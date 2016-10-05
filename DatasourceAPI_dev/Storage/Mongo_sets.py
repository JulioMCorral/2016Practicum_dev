import abc


class MongoRoutines(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def setContent(self,content):
		print 'interface; content field a document in mongo'
		return

	@abc.abstractmethod
	def setDate(self, date):
		print 'interface; date field in a document in mongo'
		return

	# interface signatures for set data instructions
	# .....
	# .....



