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
    percentage_low, percentage_high = nutrition_filter_levels(user_nutrient_level)
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

