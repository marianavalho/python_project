import pytest
import pandas as pd 
from project import load_recipes_from_excel, Recipe

def test_load_recipes_from_excel(tmp_path):
    test_data = {
        'Title': ['Recipe 1', 'Recipe 2'],
        'Ingredients': ['Ingredient1, Ingredient2', 'Ingredient3, Ingredient4'],
        'Instructions': ['Step 1', 'Step 2'],
        'Cooking Time': [30, 45],
        'Difficulty': ['Easy', 'Medium']
    }

    test_df = pd.DataFrame(test_data)
    test_excel_path = tmp_path / "test_recipes.xlsx"
    test_df.to_excel(test_excel_path, index=False)

    recipes = load_recipes_from_excel(test_excel_path)

    assert len(recipes) == 2

    assert recipes[0].title == 'Recipe 1'
    assert recipes[0].ingredients == ['Ingredient1', 'Ingredient2']
    assert recipes[0].instructions == 'Step 1'
    assert recipes[0].cooking_time == 30
    assert recipes[0].difficulty == 'Easy'

    assert recipes[1].title == 'Recipe 2'
    assert recipes[1].ingredients == ['Ingredient3', 'Ingredient4']
    assert recipes[1].instructions == 'Step 2'
    assert recipes[1].cooking_time == 45
    assert recipes[1].difficulty == 'Medium'


from project import save_recipes_to_excel, Recipe

@pytest.fixture
def sample_recipes():
    recipe1 = Recipe(title="Pasta", ingredients=["Pasta", "Tomato Sauce"], instructions="Boil pasta, add sauce", cooking_time=20, difficulty="Easy")
    recipe2 = Recipe(title="Salad", ingredients=["Lettuce", "Tomato", "Cucumber"], instructions="Mix ingredients, add dressing", cooking_time=10, difficulty="Simple")
    return [recipe1, recipe2]

def test_save_recipes_to_excel(tmp_path, sample_recipes):
    test_excel_path = tmp_path / "test_recipes.xlsx"

    save_recipes_to_excel(test_excel_path, sample_recipes)

    saved_df = pd.read_excel(test_excel_path)

    # Check if the data in the Excel file matches the expected data
    assert saved_df.shape[0] == len(sample_recipes)  # Check the number of rows
    assert all(saved_df['Title'] == [recipe.title for recipe in sample_recipes])  # Check the 'Title' column
    assert all(saved_df['Ingredients'] == [', '.join(recipe.ingredients) for recipe in sample_recipes])  # Check the 'Ingredients' column
    assert all(saved_df['Instructions'] == [recipe.instructions for recipe in sample_recipes])  # Check the 'Instructions' column
    assert all(saved_df['Cooking Time'] == [recipe.cooking_time for recipe in sample_recipes])  # Check the 'Cooking Time' column
    assert all(saved_df['Difficulty'] == [recipe.difficulty for recipe in sample_recipes])  # Check the 'Difficulty' column

import pytest
import pandas as pd 
import requests
from unittest.mock import patch
from project import get_recipes_from_spoonacular

@pytest.fixture
def sample_spoonacular_data():
    return {
        'results': [
            {'title': 'Spaghetti Bolognese', 'id': 1},
            {'title': 'Chicken Alfredo', 'id': 2},
            {'title': 'Vegetable Stir Fry', 'id': 3},
        ]
    }

@patch('requests.get')
def test_get_recipes_from_spoonacular(mock_get, sample_spoonacular_data):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_spoonacular_data

    api_key = 'cd73c8c7ed7b4b68858b59d394336523' 
    query = 'pasta'
    number = 3
    recipes = get_recipes_from_spoonacular(api_key, query, number)

    assert recipes == sample_spoonacular_data['results']

    # Check if the request to Spoonacular was made with the correct parameters
    mock_get.assert_called_once_with('https://api.spoonacular.com/recipes/search', params={'apiKey': api_key, 'query': query, 'number': number})
