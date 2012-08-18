from ProxyHelper import ProxyHelper
class GeneralClientProxy:
	def __init__(self,connection):
		self.__proxyHelper = ProxyHelper(connection)
	def destroy(self,type,name):
		return self.__proxyHelper.doOp("DESTROY", 0, None, type, name)
	def txnBegin(self):
		return self.__proxyHelper.doOp("TRXBEGIN", 0, None)
	def txnCommit(self):
		return self.__proxyHelper.doOp("TRXCOMMIT", 0, None)
	def txnRollback(self):
		return self.__proxyHelper.doOp("TRXROLLBACK", 0, None)
	def instances(self):
		return self.__proxyHelper.doOp("INSTANCES", 0, None)
	def members(self):
		return self.__proxyHelper.doOp("MEMBERS", 0, None)
	def ping(self):
		return self.__proxyHelper.doOp("PING", 0, None)
	def clusterTime(self):
		raise NotImplementedError
	def partitions(self):
		raise NotImplementedError
