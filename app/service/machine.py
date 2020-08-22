from typing import List

from app.entities.beverage import Beverage
from app.errors import IngredientUnavailableException
from app.service.inventory import Inventory
from app.service.outlet import Outlet


class Machine:
    def __init__(self, inventory: Inventory, outlets: List[Outlet]):
        """
        Machine with n outlets and invetory service.
        Currently outlets work in sync, can be easily extended by any
        concurrent/threaded pool.
        :param inventory: Inventory
        :param outlets: List[Outlet]
        """
        self.inventory = inventory
        self.outlets = outlets
        self.pool_map = map  # can replace with any thread/coroutine pool

    def brew(self, beverage_names: List[str]):
        """
        Brew beverages sequentially
        :param beverage_names:
        :return:
        """
        outlets = self.outlets[0:len(beverage_names)]
        list(self.pool_map(self._brew, outlets, beverage_names))

    def _brew(self, outlet:Outlet, beverage_name: str):
        try:
            beverage: Beverage = outlet.get_beverage(
                beverage_name, self.inventory
            )
            print(
                '{} is prepared'.format(beverage.name)
            )
        except IngredientUnavailableException as e:
            print(
                '{} cannot be prepared because {}'.format(
                    beverage_name, str(e))
            )
