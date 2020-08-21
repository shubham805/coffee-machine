from app.entities.beverage import Beverage
from app.repositories.repository import Repository


class BeverageRepo(Repository):
    entity_class = Beverage
