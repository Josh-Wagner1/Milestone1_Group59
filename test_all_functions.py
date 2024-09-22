import pytest
import pandas as pd
from all_functions import load_data, filter_food_by_name, filter_food_by_exact_name
from pathlib import Path

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
    empty_file =  tmp_path / "empty.csv"  # Create a Path object
    empty_file.touch()  # Create an empty file
    with pytest.raises(ValueError, match="No data found in the file."):
        load_data(str(empty_file))

@pytest.fixture
def food_data():
    file_path = './Food_Nutrition_Dataset.csv'
    return pd.read_csv(file_path)

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

def test_filter_food_by_name_empty_string(food_data):
    """Test error handling for empty string as a food name."""
    with pytest.raises(ValueError):
        filter_food_by_exact_name('', food_data)

def test_filter_food_by_name_non_string_input(food_data):
    """Test error handling for a non-string food name input."""
    with pytest.raises(ValueError, match="The food name must be a non-empty string."):
        filter_food_by_exact_name(123, food_data) 