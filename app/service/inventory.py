from typing import List

from app.entities.ingredient import Ingredient
from app.errors import IngredientUnavailableException
from app.repositories.repository import Repository


class Inventory:
    def __init__(self, ingredient_repo: Repository):
        self.ingredient_repo = ingredient_repo

    def get_all_ingredients(self) -> List[Ingredient]:
        return self.ingredient_repo.get_all()

    def get(self, ingredients: List[Ingredient]) -> List[Ingredient]:
        current_ingredients: dict = self._get_current_ingredients(
            ingredients
        )
        for ingredient in ingredients:
            if current_ingredients.get(
                    ingredient.name,
                    Ingredient(None, 0)).quantity < ingredient.quantity:
                raise IngredientUnavailableException(
                    "{} is not available".format(ingredient.name)
                )
        self._update_quantity(current_ingredients, ingredients, True)
        return ingredients

    def refill(self, ingredients: List[Ingredient]) -> List[Ingredient]:
        current_ingredients: dict = self._get_current_ingredients(
            ingredients)
        return self._update_quantity(current_ingredients, ingredients, False)

    def _get_current_ingredients(self, ingredients: List[Ingredient]) -> dict:
        ingredient_names: List[str] = [ingredient.name for ingredient in ingredients]
        current_ingredients = self.ingredient_repo.get_by_ids(ingredient_names)
        return {
            ingredient.name: ingredient for ingredient in current_ingredients
        }

    def _update_quantity(self, current_ingredients: dict,
                         ingredients: List[Ingredient], reduce: bool) -> List[Ingredient]:
        updated_ingredients = []
        for ingredient in ingredients:
            if reduce:
                current_ingredients[ingredient.name].quantity -= ingredient.quantity
            else:
                current_ingredients[ingredient.name].quantity += ingredient.quantity
            updated_ingredients.append(
                self.ingredient_repo.update(
                    current_ingredients[ingredient.name]
                )
            )
        return updated_ingredients
