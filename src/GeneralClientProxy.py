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
		return self.__proxyHelper.doOp("INSTANCES", GeneralClientProxy.FLAG, 0, None)
	def members(self):
		return self.__proxyHelper.doOp("MEMBERS", GeneralClientProxy.FLAG, 0, None)
	def ping(self):
		return self.__proxyHelper.doOp("PING", GeneralClientProxy.FLAG, 0, None)
	def clusterTime(self):
		raise NotImplementedError
	def partitions(self):
		raise NotImplementedError
