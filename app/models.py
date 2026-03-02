import uuid
class Transaction:
    def __init__(self,type,value,description,id=None):
        self.id = id if id else str(uuid.uuid4())
        self.type = type
        self.value = value
        self.description = description

    def to_dict(self):
            return {
                "id": self.id,
                "type":self.type,
                "value": self.value,
                "description": self.description
            }