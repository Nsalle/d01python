class Recipe:
    name = "default"
    cooking_level = 0
    cooking_time = 0
    ingredients = ["something", "to", "eat", "Miam miam"]
    description = "Empty description"
    recipe_type = "sometime in a day"

    def check_error(self, name, cooking_level,
                    cooking_time, ingredients, recipe_type, description=''):
        if not isinstance(name, str):
            print("Name of the recipe must be a string")
            quit()
        if not isinstance(cooking_level, int) or\
                cooking_level < 1 or cooking_level > 5:
            print("Cooking level must be a number from 1 to 5")
            quit()
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("Cooking time must be a positive number")
            quit()
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            print("Need list of ingredients")
            quit()
        for ingredients_str in ingredients:
            if not isinstance(ingredients_str, str):
                print("Ingredients must be strings")
                quit()
        if not isinstance(recipe_type, str) or\
                recipe_type not in ['starter', 'lunch', 'dessert']:
            print("The recipe must be a starter lunch or dessert")
            quit()
        if not isinstance(description, str):
            print("The description must be a string")
            quit()
        return 1

    def __init__(self, name, cooking_level, cooking_time,
                 ingredients, recipe_type,  description=''):
        if self.check_error(name, cooking_level, cooking_time,
                            ingredients, recipe_type, description):
            print("Recipe for {} created".format(name))
        self.name = name
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        # Return the string to print with the recipe info"""
        txt = ""
        txt += self.name
        txt += " | level " + str(self.cooking_level)
        txt += "\n{} minutes to cook\n".format(self.cooking_time)
        txt += "The ingredients you need: {}\n".format(self.ingredients)
        txt += str(self.description)
        txt += "\nThis is to be eaten for " + self.recipe_type
        return txt
