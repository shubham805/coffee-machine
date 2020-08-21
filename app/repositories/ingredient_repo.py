from app.entities.ingredient import Ingredient
from app.repositories.repository import Repository


class IngredientRepo(Repository):
    entity_class = Ingredient

