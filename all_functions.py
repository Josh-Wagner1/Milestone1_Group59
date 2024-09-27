import pandas as pd
import numpy as np

def load_data(file_path: str):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("No data found in the file.")

    return df

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

# Search for food in the database by exact name
def filter_food_by_exact_name(food_name: str, data: pd.DataFrame):
    
        if not isinstance(data, pd.DataFrame):
            raise TypeError("The provided data is not a pandas DataFrame.")
        
        if not isinstance(food_name, str) or not food_name.strip():
            raise ValueError("The food name must be a non-empty string.")
    
        filtered_data = data[data['food'].str.lower() == food_name.lower()]
    
        if filtered_data.empty:
            raise ValueError(f"No food item found for '{food_name}' in the database.")
        
        if len(filtered_data) > 1:
            raise ValueError(f"Multiple entries found for '{food_name}'. Please provide a unique food name.")

        return filtered_data

#function for retrieving the nutrient values for a specific food item
def nutrition_breakdown(food_name: str, data: pd.DataFrame, nutrients: list = None):
    if not isinstance(food_name, str) or not food_name.strip():
        raise ValueError("The food name must be a non-empty string.")

    if not isinstance(data, pd.DataFrame):
        raise TypeError("The provided data is not a pandas DataFrame.")

    try: 
        selected_food = filter_food_by_exact_name(food_name, data)
        if nutrients is None:
            return selected_food.iloc[0]
        else:
            invalid_nutrients = []
            for nutrient in nutrients:
                if nutrient not in selected_food.columns:
                    invalid_nutrients.append(nutrient)
            if invalid_nutrients:
                raise ValueError(f"The following nutrients are not valid: {', '.join(invalid_nutrients)}")
            return selected_food[nutrients].iloc[0]
    except ValueError as e:
        print(f"ValueError: {e}")
        return pd.Series()
    except TypeError as e:
        print(f"TypeError: {e}")
        return pd.Series()

#function for calculating the nutrient values for a given weight of the selected food with an exact match.
def calculate_nutrients(food_name: str, data: pd.DataFrame, weight_input: str, nutrients: list = None):
    try:
        weight = float(weight_input)
        if weight <= 0:
            raise ValueError("Weight must be a positive number greater than zero.")
        nutrient_values = nutrition_breakdown(food_name, data, nutrients)
        if nutrient_values.empty:
            raise ValueError("No valid nutrient data found for the specified food.")

        nutrient_values = pd.to_numeric(nutrient_values, errors='coerce')
        nutrient_values_per_weight = (nutrient_values * weight) / 100
        return nutrient_values_per_weight

    except ValueError as e:
        print(f"ValueError: {e}")
        return pd.Series()
    except TypeError as e:
        print(f"TypeError: {e}")
        return pd.Series()    
    
#function for filtering the results based on a high and low value for a nutrient
def nutrition_range_filter(nutrient_input: str, nutrient_min_input: str, nutrient_max_input: str, data: pd.DataFrame):
    if not isinstance(nutrient_input, str) or nutrient_input == '':
        raise ValueError("The nutrient name must be a non-empty string.")
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The provided data is not a pandas DataFrame.")

    food_arr = []

    try:
        nutrient_min = float(nutrient_min_input)
        nutrient_max = float(nutrient_max_input)
        nutrient = nutrient_input.lower().title()
        column = data[nutrient]
        for entry in column:
            try:
                if nutrient_min <= float(entry) <= nutrient_max:
                    food_arr.append(True)
                else:
                    food_arr.append(False)
            except ValueError:
                food_arr.append(False)

        if len(food_arr) == 0:
            raise ValueError("No valid foods match the specified inputs.")

        return food_arr

    except KeyError as e:
        print(f"ValueError: {e}")
        return food_arr
    except ValueError as e:
        print(f"ValueError: {e}")
        return food_arr
    except TypeError as e:
        print(f"TypeError: {e}")
        return food_arr

# Function that gives the high and low values for the levels for the nutrition level filter
def nutrition_filter_min_max(level: str):
    p_low = 0
    p_high = 0

    try:
        if level == "low":
            p_low = 0
            p_high = 33
        elif level == "medium":
            p_low = 33
            p_high = 66
        elif level == "high":
            p_low = 66
            p_high = 100
        else:
            raise ValueError("Invalid filter level.")

        return p_low, p_high

    except ValueError as e:
        print(f"ValueError: {e}")
        return p_low, p_high
    except TypeError as e:
        print(f"TypeError: {e}")
        return p_low, p_high


# function for filtering the results based the weight of a specific nutrient in 100g of the food.
def nutrition_level_filter(nutrient_input: str, nutrient_level: str, data: pd.DataFrame):
    if not isinstance(nutrient_input, str) or nutrient_input == '':
        raise ValueError("The nutrient must be a non-empty string.")
    if not isinstance(nutrient_level, str) or nutrient_level == '':
        raise ValueError("The nutrient level must be a non-empty string.")
    if not isinstance(data, pd.DataFrame):
        raise TypeError("The provided data is not a pandas DataFrame.")

    food_arr = []

    try:
        p_low, p_high = nutrition_filter_min_max(nutrient_level.lower())

        nutrient = nutrient_input.lower().title()

        if nutrient not in data.columns:
            raise KeyError(f"Nutrient '{nutrient}' not found in the table")

        column = data[nutrient]

        for entry in column:
            try:
                if p_low <= float(entry) < p_high:
                    food_arr.append(True)
                else:
                    food_arr.append(False)
            except ValueError:
                food_arr.append(False)

        if len(food_arr) == 0:
            raise ValueError("No valid foods match the specified inputs.")

        return food_arr

    except KeyError as e:
        print(f"ValueError: {e}")
        return food_arr
    except ValueError as e:
        print(f"ValueError: {e}")
        return food_arr
    except TypeError as e:
        print(f"TypeError: {e}")
        return food_arr
