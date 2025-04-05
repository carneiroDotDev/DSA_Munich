#write an example of decorator pattern in python
class Coffee:
    def cost(self):
        return 5
    
    
class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2
    
    
class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1
    
    
class VanillaDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 3
    
    
class MakeCoffee:
    def __init__(self):
        self._coffee = Coffee()

    def add_milk(self):
        self._coffee = MilkDecorator(self._coffee)

    def add_sugar(self):
        self._coffee = SugarDecorator(self._coffee)

    def add_vanilla(self):
        self._coffee = VanillaDecorator(self._coffee)

    def get_cost(self):
        return self._coffee.cost()
    
    
if __name__ == "__main__":
    coffee_shop = MakeCoffee()
    coffee_shop.add_milk()
    coffee_shop.add_sugar()
    coffee_shop.add_vanilla()
    print(f"Total cost: {coffee_shop.get_cost()}")
# Output: Total cost: 11
# This code demonstrates the decorator pattern in Python by creating a simple coffee shop system.
# The Coffee class represents a basic coffee with a cost.
# The MilkDecorator, SugarDecorator, and VanillaDecorator classes are decorators that add additional costs to the coffee.
# The MakeCoffee class allows you to create a coffee and add various decorators to it.
# The final cost is calculated by summing the costs of the base coffee and the added decorators.
# The output shows the total cost of the coffee with the added decorators.
# This pattern allows for flexible and dynamic addition of responsibilities to objects without modifying their structure.
# The decorator pattern is useful for adding functionality to objects at runtime.
# The decorators can be combined in various ways to create different variations of the coffee.          