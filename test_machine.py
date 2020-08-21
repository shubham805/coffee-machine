from app.repositories.beverage_repo import BeverageRepo
from app.repositories.ingredient_repo import IngredientRepo
from app.service.inventory import Inventory
from app.service.machine import Machine
from app.service.outlet import Outlet
from initial_state import InitialState


class MachineTest:
    initial_state = InitialState()

    def __init__(self):
        self.inventory = Inventory(
            IngredientRepo(self.initial_state.ingredients())
        )
        self.beverage_repo = BeverageRepo(self.initial_state.beverages())
        self.machine = Machine(
            self.inventory,
            [Outlet(
                self.beverage_repo
            ) for i in range(self.initial_state.outlets())]
        )

    def test_brew(self):
        self.machine.brew(["green_tea", "black_tea","hot_coffee","hot_tea"])
        for ingredient in self.inventory.get_all_ingredients():
            print('{}:{}'.format(ingredient.name, ingredient.quantity))


MachineTest().test_brew()
