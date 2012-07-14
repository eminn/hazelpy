from ProxyHelper import ProxyHelper
class GeneralClientProxy:
	def __init__(self,connection):
		self.__proxyHelper = ProxyHelper(connection)
