from pymongo import MongoClient 

class _Singleton(object):

	def __init__(self):
		client = MongoClient() #might be singleton
		db = client.timeline
		# just for the sake of information
		self.instance = "Instance at %d" % self.__hash__()


_singleton = _Singleton()

def Singleton(): return _singleton