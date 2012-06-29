class EntryEvent:
    TYPE_ADDED = "ADDED"
    TYPE_REMOVED = "REMOVED"
    TYPE_UPDATED = "UPDATED"
    TYPE_EVICTED = "EVICTED"
    def __init__(self, eventType, listenerType, name, key, value, oldValue=None):
        self.eventType = eventType
        self.key = key
        self.value = value
        self.oldValue = oldValue
        self.name = name
        self.listenerType = listenerType
        
