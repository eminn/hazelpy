**===== This project is under development and it's not ready for production. Also Hazelcast team does not introduced client protocol with official release =====
**

hazelpy is a python client for hazelcast.It is compatible with the client protocol which is introduced with hazelcast 2.2 . It supports only Map interface for now. other data structures will be added as soon as possible.

**--using hazelpy--**

In order to use hazelpy you should  download the archive from {LINK}

After extracting it run the command below in the extracted directory ,

`python setup.py install`

It will install hazelpy module to you python distrubition.After that you can use it just like,

	import hazelpy

	hc = HazelcastClient(Config())

	mymap = hc.getMap("mymap") 
	
	mymap.put("1","Joe")
	
	print mymap.get(1) # prints "Joe""

pretty easy huh ? 

you can also have a look at the MapTest.py for further usage of the Map interface.

**--contrubuting hazelpy--
**

You are welcomed if you'd like to contribute to hazelpy. You can either report issues or send pull requests.You can also help me with the documentation of the code.

Thanks for helping !

