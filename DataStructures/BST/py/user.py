"""
This module defines a `User` class and a utility function `get_users` for generating 
a list of unique users with randomized IDs. 

The `User` class includes:
- An `id` attribute for unique identification.
- A `user_name` attribute generated based on the `id` and a predefined list of names.
- Comparison methods (`__eq__`, `__lt__`, `__gt__`) for comparing users by their IDs.
- A `__repr__` method for string representation of the user.

The `get_users` function:
- Generates a specified number of unique `User` objects with shuffled IDs.
- Ensures randomness by using Python's `random` module.

This module can be used in scenarios where a collection of uniquely identifiable 
users is required, such as in data structures or simulations.
"""

import random

class User:
    def __init__(self, id):
        self.id = id
        user_names = [
            "Blake",
            "Ricky",
            "Shelley",
            "Dave",
            "George",
            "John",
            "James",
            "Mitch",
            "Williamson",
            "Burry",
            "Vennett",
            "Shipley",
            "Geller",
            "Rickert",
            "Carrell",
            "Baum",
            "Brownfield",
            "Lippmann",
            "Moses",
        ]
        self.user_name = f"{user_names[id % len(user_names)]}#{id}"

    def __eq__(self, other):
        return isinstance(other, User) and self.id == other.id

    def __lt__(self, other):
        return isinstance(other, User) and self.id < other.id

    def __gt__(self, other):
        return isinstance(other, User) and self.id > other.id
    
    def __repr__(self):
        return "".join(self.user_name)

def get_users(num):
    random.seed(1)
    users = []
    ids = []
    for i in range(num * 3):
        ids.append(i)
    random.shuffle(ids)
    ids = ids[:num]
    for id in ids:
        user = User(id)
        users.append(user)
    return users
