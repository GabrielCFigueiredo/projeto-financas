class transaction:
    def __init__(self,type,value,description):
        self.type = type
        self.value = value
        self.description = description

        def to_dict(self):
            return {
                "type":self.type,
                "value": self.value,
                "description": self.description
            }