import datetime
from recipe import Recipe


class Book:
    name = "default"
    last_update = datetime.datetime.now()
    creation_date = datetime.datetime.now()
    recipe_list = {}

    def get_recipe_by_name(self, name):
        # Print a recipe with the name `name` and return the instance
        for key in self.recipe_list:
            if name in self.recipe_list[key]:
                rep = self.recipe_list[key][name]
                print(str(rep))
                return rep

    def get_recipes_by_types(self, recipe_type):
        # """Get all recipe names for a given recipe_type """
        try:
            return (self.recipe_list[recipe_type].keys())
        except KeyError:
            print("No recipe with this type in the book")
            quit()

    def add_recipe(self, recipe):
        # """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Wrong type, need to add a recipe to the book")
            quit()
        print(recipe.recipe_type)
        if recipe.recipe_type in self.recipe_list:
            self.recipe_list[recipe.recipe_type][recipe.name] = recipe
            self.last_update = datetime.datetime.now()
        else:
            print("Wrong type of meal")
        print("Recipe for {} added to {}".format(recipe.name, self.name))

    def __init__(self, name):
        if not isinstance(name, str):
            print("Name must be a string")
            quit()
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipe_list['starter'] = {}
        self.recipe_list['lunch'] = {}
        self.recipe_list['dessert'] = {}
        print("Book called {} created".format(self.name))
