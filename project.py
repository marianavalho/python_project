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

    def save_to_excel(self, file_path):
        try:
            existing_df = pd.read_excel(file_path)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        new_recipe_data = {
            'Title': [recipe.title for recipe in self.recipes],
            'Ingredients': [', '.join(recipe.ingredients) for recipe in self.recipes],
            'Instructions': [recipe.instructions for recipe in self.recipes],
            'Cooking Time': [recipe.cooking_time for recipe in self.recipes],
            'Difficulty': [recipe.difficulty for recipe in self.recipes]
        }

        new_df = pd.DataFrame(new_recipe_data)

        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        combined_df.to_excel(file_path, index=False)

def load_recipes_from_excel(file_path):
    df = pd.read_excel(file_path)
    recipes = []

    for _, row in df.iterrows():
        recipe = Recipe(
            title=row['Title'],
            ingredients=row['Ingredients'].split(', '),
            instructions=row['Instructions'],
            cooking_time=row['Cooking Time'],
            difficulty=row['Difficulty']
        )
        recipes.append(recipe)

    return recipes


def save_recipes_to_excel(file_path, recipes):
    existing_df = pd.DataFrame()
    try:
        existing_df = pd.read_excel(file_path)
    except FileNotFoundError:
        pass

    new_recipe_data = {
        'Title': [recipe.title for recipe in recipes],
        'Ingredients': [', '.join(recipe.ingredients) for recipe in recipes],
        'Instructions': [recipe.instructions for recipe in recipes],
        'Cooking Time': [recipe.cooking_time for recipe in recipes],
        'Difficulty': [recipe.difficulty for recipe in recipes]
    }

    new_df = pd.DataFrame(new_recipe_data)

    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_excel(file_path, index=False)


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

    api_key = '231f1e24b7524afbb129b9d40a5acd08'

    # Define file_path outside of the if blocks
    file_path = 'C:\\Users\\maria\\OneDrive\\Área de Trabalho\\Introdução ao Python\\Recipes.xlsx'

    recipe_app = RecipeApp()

    # Ask the user to choose between searching in Excel, adding a recipe, or searching on Spoonacular
    print("Choose an option:")
    print("1. Search for your recipes")
    print("2. Add a new recipe")
    print("3. Search for recipes using Spoonacular")

    user_choice = input("Enter the option number (1, 2, or 3): ")

    if user_choice == '1':
        # Existing code for searching in Excel
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
        # Adding a new recipe
        title = input("Enter the title of the recipe: ")
        ingredients = input("Enter the ingredients (comma-separated): ").split(', ')
        instructions = input("Enter the instructions: ")
        cooking_time = input("Enter the cooking time (in minutes): ")
        difficulty = input("Enter the difficulty level: ")

        new_recipe = Recipe(title, ingredients, instructions, cooking_time, difficulty)
        recipe_app.add_recipe(new_recipe)

        print("\nRecipe added successfully!")

        # Save updated recipes to Excel
        recipe_app.save_to_excel(file_path)

    elif user_choice == '3':
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
        print("Invalid option. Please choose either 1, 2, or 3.")

if __name__ == "__main__":
    main()
