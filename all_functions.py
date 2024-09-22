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
def calculate_nutrients(food_name: str, data: pd.DataFrame, weight: float, nutrients: list = None):
    try:
        if weight <= 0:
            raise ValueError("Weight must be a positive number greater than zero.")
        nutrient_values = nutrition_breakdown(food_name, data, nutrients)
        if nutrient_values.empty:
            raise ValueError("No valid nutrient data found for the specified food.")
        nutrient_values_per_weight = (nutrient_values * weight) / 100
        return nutrient_values_per_weight
    
    except ValueError as e:
        print(f"ValueError: {e}")
        return pd.Series()
    except TypeError as e:
        print(f"TypeError: {e}")
        return pd.Series()    
    
#function for filtering the results based on a high and low value for a nutrient
def nutrition_range_filter(user_nutrient_input, user_nutrient_min, user_nutrient_max, data: pd.DataFrame):

    nutrient_column = data[user_nutrient_input]
    user_nutrient_min = int(user_nutrient_min)
    user_nutrient_max = int(user_nutrient_max)
    food_arr = []
    for entry in nutrient_column:
        if entry < user_nutrient_max and entry > user_nutrient_min:
            food_arr.append(True)
        else:
            filter_food_by_name().append(False)

    return food_arr

#function that gives the high and low values for the levels for the nutrition level filter
def nutrition_filter_min_max(level):
    percentage_low = 0
    percentage_high = 0
    if level == 'high':
        percentage_low = 67
        percentage_high = 100
    if level == 'mid':
        percentage_low = 34
        percentage_high = 66
    if level == 'low':
        percentage_low = 0
        percentage_high = 33

    return percentage_low, percentage_high


def nutrition_level_filter(user_nutrient_input, user_nutrient_level, data: pd.DataFrame):
    percentage_low, percentage_high = nutrition_filter_min_max(user_nutrient_level)
    nutrient_column = data[user_nutrient_input]
    food_arr = []
    #finding the highest value of the nutrient
    highest_value = 0
    for entry in nutrient_column:
        if entry > highest_value:
            highest_value = float(entry)
        else:
            pass
    #calculating the percentage of each entry of the highest nutrient
    for entry in nutrient_column:
        nutrition_percentage = float(entry) / highest_value * 100
        #adding the entry to results if percentage in selected limits
        if nutrition_percentage > percentage_low and nutrition_percentage < percentage_high:
            food_arr.append(True)
        else:
            food_arr.append(False)
    return food_arr
