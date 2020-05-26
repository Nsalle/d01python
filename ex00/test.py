from book import Book
from recipe import Recipe

salad = Recipe("salad", 4, 5, ['test'], "starter", "De la salade")
cookbook = Book("JaiFaim")
print()
print("Le book a ete cree a :", cookbook.creation_date)
cookbook.add_recipe(salad)
print()
cookbook.get_recipe_by_name('salad')
print()
cookbook.get_recipes_by_types('starter')
