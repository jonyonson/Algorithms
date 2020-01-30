#!/usr/bin/python

# import math


def recipe_batches(recipe, ingredients):
    batches = []
    for key in recipe.keys():
        if ingredients.get(key) and recipe.get(key):
            batches.append(ingredients[key] // recipe[key])
        else:
            return 0
    return min(batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
    ingredients = {'milk': 1288, 'flour': 40, 'sugar': 95, 'butter': 40}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
