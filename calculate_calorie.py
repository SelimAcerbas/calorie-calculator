def main():

    # Example Usage
    example_input = {
    'gender': 'female',
    'weight': 59,  # kg
    'height': 162,  # cm
    'age': 27,
    'activity_level': 'lightly active',
    'goal': 'deficit'
}
    
    result = calculate_macros(**example_input)
    print(result)


def calculate_macros(gender, weight, height, age, activity_level, goal):
    # BMR Calculation
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Activity Level Multiplier
    activity_multipliers = {
        'sedentary': 1.2,
        'lightly active': 1.375,
        'moderately active': 1.55,
        'very active': 1.725,
        'extra active': 1.9
    }
    tdee = round(bmr * activity_multipliers[activity_level.lower()])

    # Adjust for goal
    if goal.lower() == 'deficit':
        calorie_goal = tdee - 500  # Example: 500 calorie deficit for weight loss
    elif goal.lower() == 'surplus':
        calorie_goal = tdee + 500  # Example: 500 calorie surplus for muscle gain
    else:  # maintenance
        calorie_goal = tdee

    # Protein Intake Calculation (in grams)
    protein_intake = round(weight * 2.2)  # Using 2.2 as a general guideline

    # Calculating Fat and Carbohydrate Intake
    # Assuming 30% of calorie intake from fats, and the rest from carbohydrates
    fat_calories = calorie_goal * 0.30
    carb_calories = calorie_goal - (protein_intake * 4) - fat_calories  # 4 calories per gram of protein

    # Convert calories to grams (9 calories/gram for fat, 4 calories/gram for carbs)
    fat_grams = round(fat_calories / 9)
    carb_grams = round(carb_calories / 4)

    return {
        'Daily Calorie Goal': calorie_goal, 
        'Recommended Protein Intake (grams)': protein_intake,
        'Recommended Fat Intake (grams)': fat_grams,
        'Recommended Carbohydrate Intake (grams)': carb_grams
    }


if __name__ == "__main__":
    main()