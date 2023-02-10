class Event:
    def __init__(self, index, event_type, time, description, roles):
        self.index = index
        self.time = time
        self.description = description
        self.roles = roles
        self.type = event_type

    def __str__(self):
        return f"{self.index}: {self.time} {self.type} event ({self.description}) for roles {self.roles}"

    def show(self):
        pass

    @classmethod
    def create(cls, **kwargs):
        event = cls(None, None, None, None, None)
        [event.__setattr__(attr, kwargs[attr]) for attr in kwargs]
        return event
