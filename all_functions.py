import pandas as pd
import numpy as np


# Search for food in the database

def filter_food_by_name(food_name: str, data: pd.DataFrame):

    if not isinstance(data, pd.DataFrame):
        raise TypeError("The provided data is not a pandas DataFrame.")
    
    if not isinstance(food_name, str) or not food_name.strip():
        raise ValueError("The food name must be a non-empty string.")

    food_column = data['food']
    filtered_data = data[food_column.str.contains(food_name, case=False, na=False)]

    if filtered_data.empty:
        raise ValueError(f"No food item found for '{food_name}' in the database.")
    
    return filtered_data


