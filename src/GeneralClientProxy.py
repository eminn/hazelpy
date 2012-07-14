from ProxyHelper import ProxyHelper
class GeneralClientProxy:
	FLAG = 0
	def __init__(self,connection):
		self.__proxyHelper = ProxyHelper(connection)
	def destroy(self,type,name):
		return self.__proxyHelper.doOp("DESTROY", GeneralClientProxy.FLAG, 0, None, type, name)
	def txnBegin(self):
		return self.__proxyHelper.doOp("TRXBEGIN", GeneralClientProxy.FLAG, 0, None)
	def txnCommit(self):
		return self.__proxyHelper.doOp("TRXCOMMIT", GeneralClientProxy.FLAG, 0, None)
	def txnRollback(self):
		return self.__proxyHelper.doOp("TRXROLLBACK", GeneralClientProxy.FLAG, 0, None)
	def instances(self):
		raise NotImplementedError
	def members(self):
		raise NotImplementedError
	def clusterTime(self):
		raise NotImplementedError
	def ping(self):
		raise NotImplementedError
	def partitions(self):
		raise NotImplementedError
