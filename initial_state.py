class InitialState:
    state = {
        "machine": {
            "outlets": {
                "count_n": 4
            },
            "total_items_quantity": {
                "hot_water": 500,
                "hot_milk": 500,
                "ginger_syrup": 100,
                "sugar_syrup": 100,
                "tea_leaves_syrup": 100
            },
            "beverages": {
                "hot_tea": {
                    "hot_water": 200,
                    "hot_milk": 100,
                    "ginger_syrup": 10,
                    "sugar_syrup": 10,
                    "tea_leaves_syrup": 30
                },
                "hot_coffee": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "hot_milk": 400,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "black_tea": {
                    "hot_water": 300,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "tea_leaves_syrup": 30
                },
                "green_tea": {
                    "hot_water": 100,
                    "ginger_syrup": 30,
                    "sugar_syrup": 50,
                    "green_mixture": 30
                },
            }
        }
    }

    def outlets(self):
        return self.state['machine']['outlets']['count_n']

    def _ingredients(self, adict: dict) -> dict:
        store_ingredients = {}
        for key, value in adict.items():
            store_ingredients[key] = {
                'name': key,
                'quantity': value
            }
        return store_ingredients

    def _beverages(self, adict: dict):
        store_beverages = {}
        for key, value in adict.items():
            store_beverages[key] = {
                'name': key,
                'ingredients': list(self._ingredients(value).values())
            }
        return store_beverages

    def ingredients(self):
        return self._ingredients(self.state['machine']['total_items_quantity'])

    def beverages(self):
        return self._beverages(self.state['machine']['beverages'])
