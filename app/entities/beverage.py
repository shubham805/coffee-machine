from typing import List

from app.entities.entity import Entity
from app.entities.ingredient import Ingredient


class Beverage(Entity):
    def __init__(self, name: str, ingredients: List[Ingredient]):
        super(Beverage, self).__init__(name)
        self.name = name
        self.ingredients = ingredients

    @classmethod
    def from_dict(cls, adict):
        return cls(
            adict['name'],
            [Ingredient.from_dict(ingredient) for ingredient in adict['ingredients']])

