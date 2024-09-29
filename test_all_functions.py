import pytest
import pandas as pd
from all_functions import (
    load_data,
    filter_food_by_name,
    filter_food_by_exact_name,
    nutrition_breakdown,
    calculate_nutrients,
    nutrition_range_filter,
    nutrition_filter_min_max,
    nutrition_level_filter
)
from pathlib import Path

# Fixture to load the data once for all tests
@pytest.fixture(scope="module")
def food_data():
    file_path = './Food_Nutrition_Dataset.csv'
    return load_data(file_path)

# Tests for load_data function
def test_load_data_valid_file():
    """Test loading data from a valid file path."""
    file_path = './Food_Nutrition_Dataset.csv'
    df = load_data(file_path)
    assert isinstance(df, pd.DataFrame), "Expected the loaded data to be a DataFrame"
    assert not df.empty, "Expected the DataFrame to be non-empty"

def test_load_data_file_not_found():
    """Test loading data from a non-existent file."""
    file_path = './nonexistent_file.csv'
    with pytest.raises(FileNotFoundError, match="File not found."):
        load_data(file_path)

def test_load_data_empty_file(tmp_path):
    """Test loading data from an empty file."""
    empty_file = tmp_path / "empty.csv"  # Create a Path object
    empty_file.touch()  # Create an empty file
    with pytest.raises(ValueError, match="No data found in the file."):
        load_data(str(empty_file))

# Tests for filter_food_by_name function
@pytest.mark.parametrize("food_name", [
    'cheese', 'bReaD', 'CHEESE', 'butter'
])
def test_filter_food_by_name_valid(food_data, food_name):
    """Parametrized test for multiple food names."""
    result = filter_food_by_name(food_name, food_data)
    assert len(result) > 0, f"Expected at least one match for '{food_name}'"

def test_filter_food_by_name_not_found(food_data):
    """Test filtering with a food name not present."""
    with pytest.raises(ValueError, match="No food item found for 'nonexistentfood' in the database."):
        filter_food_by_name('nonexistentfood', food_data)

def test_filter_food_by_name_invalid_input_type():
    """Test error handling for invalid data input (not a DataFrame)."""
    with pytest.raises(TypeError):
        filter_food_by_name('cheese', 'invalid_data')

def test_filter_food_by_name_empty_string(food_data):
    """Test error handling for empty string as a food name."""
    with pytest.raises(ValueError):
        filter_food_by_name('', food_data)

def test_filter_food_by_name_non_string_input(food_data):
    """Test error handling for a non-string food name input."""
    with pytest.raises(ValueError, match="The food name must be a non-empty string."):
        filter_food_by_name(123, food_data)

# Tests for filter_food_by_exact_name function
@pytest.mark.parametrize("food_name_exact", [
    'cream cheese', 'RiCOTta CheeSE', 'butter croissant', 'cORn rice'
])
def test_filter_food_by_exact_name_valid(food_data, food_name_exact):
    """Test filtering food by an exact name."""
    result = filter_food_by_exact_name(food_name_exact, food_data)
    assert not result.empty, "Expected non-empty result for exact match"

def test_filter_food_by_exact_name_not_found(food_data):
    """Test filtering with a food name not present."""
    with pytest.raises(ValueError, match="No food item found for 'nonexistentfood' in the database."):
        filter_food_by_exact_name('nonexistentfood', food_data)

def test_filter_food_by_exact_name_multiple_entries(food_data):
    """Test handling of multiple entries with the exact same name."""
    duplicated_data = pd.concat([food_data, food_data[food_data['food'].str.lower() == 'cream cheese']])
    with pytest.raises(ValueError, match="Multiple entries found for 'cream cheese'. Please provide a unique food name."):
        filter_food_by_exact_name('cream cheese', duplicated_data)

def test_filter_food_by_exact_name_invalid_input_type():
    """Test error handling for invalid data input."""
    with pytest.raises(TypeError):
        filter_food_by_exact_name('RiCOTta CheeSE', 'invalid_data')

def test_filter_food_by_exact_name_empty_string(food_data):
    """Test error handling for empty string as a food name."""
    with pytest.raises(ValueError):
        filter_food_by_exact_name('', food_data)

def test_filter_food_by_exact_name_non_string_input(food_data):
    """Test error handling for a non-string food name input."""
    with pytest.raises(ValueError, match="The food name must be a non-empty string."):
        filter_food_by_exact_name(123, food_data)

# Tests for nutrition_breakdown function
def test_nutrition_breakdown_valid_all_nutrients(food_data):
    """Test nutrition breakdown with a valid food name and no specified nutrients."""
    food_name = 'cream cheese'
    result = nutrition_breakdown(food_name, food_data)
    assert isinstance(result, pd.Series), "Expected the result to be a pandas Series"
    assert not result.empty, "Expected the result Series to be non-empty"

def test_nutrition_breakdown_valid_specific_nutrients(food_data):
    """Test nutrition breakdown with specific nutrients."""
    food_name = 'cream cheese'
    nutrients = ['Fat', 'Carbohydrates']
    result = nutrition_breakdown(food_name, food_data, nutrients)
    assert isinstance(result, pd.Series), "Expected the result to be a pandas Series"
    assert not result.empty, "Expected the result Series to be non-empty"
    assert all(nutrient in result.index for nutrient in nutrients), "Expected specified nutrients in the result"

def test_nutrition_breakdown_invalid_food_name(food_data):
    """Test nutrition breakdown with invalid food name."""
    with pytest.raises(ValueError):
        nutrition_breakdown('', food_data)

def test_nutrition_breakdown_invalid_data():
    """Test nutrition breakdown with invalid data input."""
    with pytest.raises(TypeError):
        nutrition_breakdown('cream cheese', 'invalid_data')

def test_nutrition_breakdown_invalid_nutrients(food_data):
    """Test nutrition breakdown with invalid nutrient names."""
    nutrients = ['InvalidNutrient']
    result = nutrition_breakdown('cream cheese', food_data, nutrients)
    assert result.empty, "Expected an empty Series for invalid nutrients"

def test_nutrition_breakdown_food_not_found(food_data):
    """Test nutrition breakdown with food not found."""
    result = nutrition_breakdown('nonexistentfood', food_data)
    assert result.empty, "Expected an empty Series when food is not found"

# Tests for calculate_nutrients function
def test_calculate_nutrients_valid(food_data):
    """Test calculate nutrients with valid inputs."""
    food_name = 'cream cheese'
    weight_input = '100'  # grams
    result = calculate_nutrients(food_name, food_data, weight_input)
    assert isinstance(result, pd.Series), "Expected the result to be a pandas Series"
    assert not result.empty, "Expected the result Series to be non-empty"

def test_calculate_nutrients_invalid_weight(food_data):
    """Test calculate nutrients with invalid weight input."""
    food_name = 'cream cheese'
    weight_input = '-100'  # Negative weight
    result = calculate_nutrients(food_name, food_data, weight_input)
    assert result.empty, "Expected an empty Series for invalid weight input"

def test_calculate_nutrients_invalid_weight_non_numeric(food_data):
    """Test calculate nutrients with non-numeric weight input."""
    food_name = 'cream cheese'
    weight_input = 'abc'  # Non-numeric
    result = calculate_nutrients(food_name, food_data, weight_input)
    assert result.empty, "Expected an empty Series for non-numeric weight input"

def test_calculate_nutrients_food_not_found(food_data):
    """Test calculate nutrients with food not found."""
    result = calculate_nutrients('nonexistentfood', food_data, '100')
    assert result.empty, "Expected an empty Series when food is not found"

def test_calculate_nutrients_invalid_data():
    """Test calculate nutrients with invalid data input."""
    with pytest.raises(TypeError):
        calculate_nutrients('cream cheese', 'invalid_data', '100')

def test_calculate_nutrients_invalid_nutrients(food_data):
    """Test calculate nutrients with invalid nutrient names."""
    nutrients = ['InvalidNutrient']
    result = calculate_nutrients('cream cheese', food_data, '100', nutrients)
    assert result.empty, "Expected an empty Series for invalid nutrients"

# Tests for nutrition_range_filter function
def test_nutrition_range_filter_valid(food_data):
    """Test nutrition range filter with valid inputs."""
    nutrient_input = 'Fat'
    nutrient_min_input = '150'
    nutrient_max_input = '200'
    result = nutrition_range_filter(nutrient_input, nutrient_min_input, nutrient_max_input, food_data)
    assert isinstance(result, list), "Expected the result to be a list"
    result = food_data[result]
    assert result.shape[0] == 7, "Expected the result list to match the length of the data"

def test_nutrition_range_filter_invalid_nutrient(food_data):
    """Test nutrition range filter with invalid nutrient name."""
    nutrient_input = 'InvalidNutrient'
    nutrient_min_input = '100'
    nutrient_max_input = '200'
    result = nutrition_range_filter(nutrient_input, nutrient_min_input, nutrient_max_input, food_data)
    assert all(not val for val in result), "Expected all False values when nutrient is invalid"

def test_nutrition_range_filter_invalid_min_max(food_data):
    """Test nutrition range filter with invalid min and max inputs."""
    nutrient_input = 'Calories'
    nutrient_min_input = 'abc'  # Non-numeric
    nutrient_max_input = 'def'  # Non-numeric
    result = nutrition_range_filter(nutrient_input, nutrient_min_input, nutrient_max_input, food_data)
    assert all(not val for val in result), "Expected all False values when min/max are invalid"

def test_nutrition_range_filter_invalid_data():
    """Test nutrition range filter with invalid data input."""
    with pytest.raises(TypeError):
        nutrition_range_filter('Calories', '100', '200', 'invalid_data')

def test_nutrition_range_filter_empty_nutrient_input(food_data):
    """Test nutrition range filter with empty nutrient input."""
    nutrient_input = ''
    nutrient_min_input = '100'
    nutrient_max_input = '200'
    with pytest.raises(ValueError, match="The nutrient name must be a non-empty string."):
        nutrition_range_filter(nutrient_input, nutrient_min_input, nutrient_max_input, food_data)

def test_nutrition_range_filter_empty_column():
    """Test nutrition range filter with empty min/max inputs."""
    nutrient_input = 'Fat'
    nutrient_min_input = '150'
    nutrient_max_input = '200'
    data = {'Fat': []}
    result = nutrition_range_filter(nutrient_input, nutrient_min_input, nutrient_max_input, pd.DataFrame(data))
    assert len(result) == 0, "Expected an empty Series for invalid nutrients"
        
# Tests for nutrition_filter_min_max function
def test_nutrition_filter_min_max_valid():
    """Test nutrition filter min max with valid level inputs."""
    levels = {'low': (0, 33), 'medium': (33, 66), 'high': (66, 100)}
    for level, expected in levels.items():
        p_low, p_high = nutrition_filter_min_max(level)
        assert (p_low, p_high) == expected, f"Expected {expected} for level '{level}'"

def test_nutrition_filter_min_max_invalid():
    """Test nutrition filter min max with invalid level input."""
    level = 'invalid_level'
    p_low, p_high = nutrition_filter_min_max(level)
    assert (p_low, p_high) == (0, 0), "Expected (0, 0) when level is invalid"

def test_nutrition_filter_min_max_empty_level():
    """Test nutrition filter min max with empty level input."""
    level = ''
    p_low, p_high = nutrition_filter_min_max(level)
    assert (p_low, p_high) == (0, 0), "Expected (0, 0) when level is empty"

def test_nutrition_filter_min_max_non_string():
    """Test nutrition filter min max with non-string level input."""
    level = 123
    p_low, p_high = nutrition_filter_min_max(level)
    assert (p_low, p_high) == (0, 0), "Expected (0, 0) when level is non-string"

# Tests for nutrition_level_filter function
def test_nutrition_level_filter_valid(food_data):
    """Test nutrition level filter with valid inputs."""
    nutrient_input = 'Fat'
    nutrient_level = 'High'
    result = nutrition_level_filter(nutrient_input, nutrient_level, food_data)
    assert isinstance(result, list), "Expected the result to be a list"
    result = food_data[result]
    assert result.shape[0] == 40, "Expected the result list to match the length of the data"

def test_nutrition_level_filter_invalid_nutrient(food_data):
    """Test nutrition level filter with invalid nutrient name."""
    nutrient_input = 'InvalidNutrient'
    nutrient_level = 'low'
    result = nutrition_level_filter(nutrient_input, nutrient_level, food_data)
    assert all(not val for val in result), "Expected all False values when nutrient is invalid"

def test_nutrition_level_filter_invalid_level(food_data):
    """Test nutrition level filter with invalid level input."""
    nutrient_input = 'Calories'
    nutrient_level = 'invalid_level'
    result = nutrition_level_filter(nutrient_input, nutrient_level, food_data)
    assert all(not val for val in result), "Expected all False values when level is invalid"

def test_nutrition_level_filter_invalid_data():
    """Test nutrition level filter with invalid data input."""
    with pytest.raises(TypeError):
        nutrition_level_filter('Calories', 'low', 'invalid_data')

def test_nutrition_level_filter_empty_nutrient_input(food_data):
    """Test nutrition level filter with empty nutrient input."""
    nutrient_input = ''
    nutrient_level = 'low'
    with pytest.raises(ValueError, match="The nutrient must be a non-empty string."):
        nutrition_level_filter(nutrient_input, nutrient_level, food_data)

def test_nutrition_level_filter_empty_level_input(food_data):
    """Test nutrition level filter with empty level input."""
    nutrient_input = 'Calories'
    nutrient_level = ''
    with pytest.raises(ValueError, match="The nutrient level must be a non-empty string."):
        nutrition_level_filter(nutrient_input, nutrient_level, food_data)

def test_nutrition_level_filter_empty_column():
    """Test nutrition range filter with empty min/max inputs."""
    nutrient_input = 'Fat'
    nutrient_level = 'low'
    data = {'Fat': []}
    result = nutrition_level_filter(nutrient_input, nutrient_level, pd.DataFrame(data))
    assert len(result) == 0, "Expected an empty Series for invalid nutrients"
