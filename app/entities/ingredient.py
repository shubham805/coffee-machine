from app.entities.entity import Entity


class Ingredient(Entity):
    def __init__(self, name, quantity):
        super(Ingredient, self).__init__(name)
        self.name = name
        self.quantity = quantity

    @classmethod
    def from_dict(cls, adict):
        return cls(
            adict['name'],
            adict['quantity']
        )
