import pandas as pd

class Recipe:
    def __init__(self, title, ingredients, instructions, cooking_time, difficulty):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.cooking_time = cooking_time
        self.difficulty = difficulty

    def display_recipe(self):
        print(f"\n{self.title}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("\nInstructions:")
        print(self.instructions)
        print(f"\nCooking Time: {self.cooking_time} minutes")
        print(f"Difficulty: {self.difficulty}")

class RecipeApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_recipes(self, keyword):
        results = [recipe for recipe in self.recipes if keyword.lower() in recipe.title.lower()]
        return results

def load_recipes_from_excel(file_path):
    df = pd.read_excel(file_path)
    recipes = []

    for _, row in df.iterrows():
        recipe = Recipe(
            title=row['Title'],
            ingredients=row['Ingredients'].split(','),
            instructions=row['Instructions'],
            cooking_time=row['Cooking Time'],
            difficulty=row['Difficulty']
        )
        recipes.append(recipe)

    return recipes

import requests

def get_recipes_from_spoonacular(api_key, query, number=5):
    base_url = 'https://api.spoonacular.com/recipes/search'
    params = {
        'apiKey': api_key,
        'query': query,
        'number': number,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('results', [])
    else:
        return None



def main():
    print("Welcome to the Recipe App")

    api_key = '2aa24e7071244a338a29c011ec282199'

    recipe_app = RecipeApp()

    # Ask the user to choose between Spoonacular and local recipes
    print("Choose an option:")
    print("1. Search for recipes using Spoonacular")
    print("2. Search for recipes in your local app")

    user_choice = input("Enter the option number (1 or 2): ")

    if user_choice == '1':
        # Ask the user for the ingredient they want to search for on Spoonacular
        user_input = input("Enter an ingredient to search for recipes on Spoonacular: ")
        recipes = get_recipes_from_spoonacular(api_key, user_input)

        if recipes:
            print(f"\nRecipes for '{user_input}' from Spoonacular:")
            for recipe in recipes:
                print(f"- {recipe['title']}")
        else:
            print(f"\nNo recipes found for '{user_input}' on Spoonacular.")
    elif user_choice == '2':
        # Load recipes from Excel file
        file_path = 'C:\\Users\\maria\\OneDrive\\Área de Trabalho\\Introdução ao Python\\Recipes.xlsx'
        recipes_from_excel = load_recipes_from_excel(file_path)

        # Add recipes to the app
        for recipe in recipes_from_excel:
            recipe_app.add_recipe(recipe)

        # Search for recipes in the local app
        keyword = input("Search for recipes in your app (enter keyword): ")
        results = recipe_app.search_recipes(keyword)

        if results:
            print("\nSearch Results in your app:")
            for result in results:
                result.display_recipe()
        else:
            print("\nNo recipes found in your app.")
    else:
        print("Invalid option. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()

# HII