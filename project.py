import pandas as pd
import requests

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

    # Ask the user to choose between searching in Excel or on Spoonacular
    print("Choose an option:")
    print("1. Search for recipes using the Excel file")
    print("2. Search for recipes using Spoonacular")

    user_choice = input("Enter the option number (1 or 2): ")

    if user_choice == '1':
        # Local app search code (existing code)
        file_path = 'C:\\Users\\maria\\OneDrive\\Área de Trabalho\\Introdução ao Python\\Recipes.xlsx'
        recipes_from_excel = load_recipes_from_excel(file_path)

        for recipe in recipes_from_excel:
            recipe_app.add_recipe(recipe)

        # Search for recipes
        keyword = input("Search for recipes (enter keyword): ")
        results = recipe_app.search_recipes(keyword)

        if results:
            print("\nSearch Results:")
            for idx, result in enumerate(results, 1):
                print(f"{idx}. {result.title}")

            # Ask the user to select a recipe
            selected_index = int(input("Enter the number of the recipe to view details: "))
            if 1 <= selected_index <= len(results):
                selected_recipe = results[selected_index - 1]

                # Display the details for the selected recipe
                selected_recipe.display_recipe()
            else:
                print("Invalid selection.")
        else:
            print("\nNo recipes found.")

    elif user_choice == '2':
        # Spoonacular search code
        keyword = input("Enter an ingredient to search for recipes: ")
        recipes = get_recipes_from_spoonacular(api_key, keyword)

        if recipes:
            print(f"\nRecipes for '{keyword}' from Spoonacular:")
            for idx, recipe in enumerate(recipes, 1):
                print(f"{idx}. {recipe['title']}")

        else:
            print(f"\nNo recipes found for '{keyword}' on Spoonacular.")
    else:
        print("Invalid option. Please choose either 1 or 2.")

if __name__ == "__main__":
    main()