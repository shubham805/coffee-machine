from app.entities.beverage import Beverage
from app.repositories.beverage_repo import BeverageRepo
from app.service.inventory import Inventory


class Outlet:
    def __init__(self, beverage_repo: BeverageRepo):
        self.beverage_repo = beverage_repo

    def get_beverage(self, beverage_name: str, inventory: Inventory) -> Beverage:
        beverage: Beverage = self.beverage_repo.get_by_id(beverage_name)
        inventory.get(beverage.ingredients)
        return beverage
