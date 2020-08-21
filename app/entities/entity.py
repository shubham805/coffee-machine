import abc


class Entity(object):
    def __init__(self, entity_id: str):
        self.id = entity_id

    @classmethod
    def from_dict(cls, adict):
        abc.abstractclassmethod()

