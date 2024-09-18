import pytest
import pandas as pd
from all_functions import filter_food_by_name

@pytest.fixture
def food_data():
    file_path = './Food_Nutrition_Dataset.csv'
    return pd.read_csv(file_path)

@pytest.mark.parametrize("food_name", [
    'cheese', 'bread', 'apple', 'butter'
])
def test_filter_food_by_name_parametrized(food_data, food_name):
    """Parametrized test for multiple food names."""
    result = filter_food_by_name(food_name, food_data)
    assert len(result) > 0, f"Expected at least one match for '{food_name}'"

def test_filter_food_by_name_invalid(food_data):
    """Test filtering with a food name not present."""
    with pytest.raises(ValueError, match="No food item found for 'nonexistentfood' in the database."):
        filter_food_by_name('nonexistentfood', food_data)

def test_filter_food_by_name_case_insensitivity(food_data):
    """Test case-insensitive filtering."""
    result = filter_food_by_name('CHEESE', food_data)
    assert len(result) > 0, "Expected case-insensitive match for 'CHEESE'"

def test_filter_food_by_name_invalid_input_type():
    """Test error handling for invalid data input (not a DataFrame)."""
    with pytest.raises(TypeError):
        filter_food_by_name('cheese', 'invalid_data')

def test_filter_food_by_name_empty_string(food_data):
    """Test error handling for empty string as a food name."""
    with pytest.raises(ValueError):
        filter_food_by_name('', food_data)
