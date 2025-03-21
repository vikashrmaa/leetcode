from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Step 1: Create graph and in-degree map
        ingredient_to_recipes = {}  # Graph adjacency list
        in_degree = {}  # Count of missing ingredients for each recipe
        
        # Initialize recipes in the in-degree dictionary
        for recipe in recipes:
            in_degree[recipe] = 0  # Initially, we will count their dependencies
        
        # Build the graph
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient not in ingredient_to_recipes:
                    ingredient_to_recipes[ingredient] = []
                ingredient_to_recipes[ingredient].append(recipe)  # Ingredient → Recipe
                in_degree[recipe] += 1  # Each recipe depends on its ingredients
        
        # Step 2: Add initial supplies to the queue
        queue = deque(supplies)
        possible_recipes = set(supplies)  # Track what we can make
        
        # Step 3: Process the queue
        result = []
        
        while queue:
            item = queue.popleft()
            
            # If it's a recipe, add it to the result
            if item in in_degree:
                result.append(item)
            
            # If this item is an ingredient for recipes, reduce in-degree
            if item in ingredient_to_recipes:
                for recipe in ingredient_to_recipes[item]:
                    in_degree[recipe] -= 1
                    # If all ingredients are available, add the recipe to queue
                    if in_degree[recipe] == 0:
                        queue.append(recipe)
        
        return result
