from ProxyHelper import ProxyHelper
import time
class GeneralClientProxy:
	def __init__(self,connection):
		self.__proxyHelper = ProxyHelper(connection)
	
	def destroy(self,type,name):
		response = self.__proxyHelper.doOp("DESTROY", 0, None, type, name)
		return self.__proxyHelper.readOKResponse(response)
	
	def txnBegin(self):
		response = self.__proxyHelper.doOp("TRXBEGIN", 0, None)
		return self.__proxyHelper.readOKResponse(response)
	
	def txnCommit(self):
		response = self.__proxyHelper.doOp("TRXCOMMIT", 0, None)
		return self.__proxyHelper.readOKResponse(response)

	def txnRollback(self):
		response = self.__proxyHelper.doOp("TRXROLLBACK", 0, None)
		return self.__proxyHelper.readOKResponse(response)
	
	def instances(self):
		response = self.__proxyHelper.doOp("INSTANCES", 0, None)
		response = response["commandLine"].split()
		types = response[1::2]
		names = response[2::2]
		return dict(zip(names,types))
	
	def members(self):
		response =  self.__proxyHelper.doOp("MEMBERS", 0, None)
		response = response["commandLine"].split()
		return response[1:]
	
	def ping(self): # we are getting unknown_error
		response =  self.__proxyHelper.doOp("PING", 0, None)
		return self.__proxyHelper.readOKResponse(response)
	
	def clusterTime(self):
		response =  self.__proxyHelper.doOp("CLUSTERTIME", 0, None)
		milis =  self.__proxyHelper.readSingleIntResponse(response)
		return time.gmtime((milis/1000)) # hazelcast returns time in miliseconds granularity but built in python methods in seconds granularity.
	
	def partitions(self,key=None):
		if key is None:
			response = self.__proxyHelper.doOp("PARTITIONS", 0, None)
		else:
			response = self.__proxyHelper.doOp("PARTITIONS", 1, key)
		response = response["commandLine"].split()
		pids = response[1::2]
		pids = [int(x) for x in pids] # convert string keys to int
		addresses = response[2::2]
		return dict(zip(pids,addresses))


