import cPickle as pickle    

def serializeObject(pythonObj):
    return pickle.dumps(pythonObj, pickle.HIGHEST_PROTOCOL)

def deSerializeObject(pickledObj):
    return pickle.loads(pickledObj)

print type(deSerializeObject(list(serializeObject("test"))))