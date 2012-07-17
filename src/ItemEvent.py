class ItemEvent:
    TYPE_ADDED = "ADDED"
    TYPE_REMOVED = "REMOVED"    
    def __init__(self, eventType, listenerType, name, value):
        self.eventType = eventType
        self.listenerType = listenerType
        self.name = name
        self.value = value