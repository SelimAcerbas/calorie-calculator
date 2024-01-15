import random

# FoodItem class
class FoodItem:
    def __init__(self, name, protein_per_100g, carbs_per_100g, fats_per_100g, serving_size):
        self.name = name
        self.protein_per_100g = protein_per_100g
        self.carbs_per_100g = carbs_per_100g
        self.fats_per_100g = fats_per_100g
        self.serving_size = serving_size  # in grams

    def get_macros_for_serving(self):
        # Calculate macros for the defined serving size
        protein = (self.protein_per_100g / 100) * self.serving_size
        carbs = (self.carbs_per_100g / 100) * self.serving_size
        fats = (self.fats_per_100g / 100) * self.serving_size
        calories = (protein + carbs) * 4 + fats * 9
        return protein, carbs, fats, calories

# Meal class
class Meal:
    def __init__(self, name):
        self.name = name
        self.food_items = []
        self.quantities = []  # Number of servings of each food item

    def add_food_item(self, food_item, quantity):
        self.food_items.append(food_item)
        self.quantities.append(quantity)

    def get_total_macros(self):
        total_protein = sum(item.get_macros_for_serving()[0] * qty for item, qty in zip(self.food_items, self.quantities))
        total_carbs = sum(item.get_macros_for_serving()[1] * qty for item, qty in zip(self.food_items, self.quantities))
        total_fats = sum(item.get_macros_for_serving()[2] * qty for item, qty in zip(self.food_items, self.quantities))
        total_calories = sum(item.get_macros_for_serving()[3] * qty for item, qty in zip(self.food_items, self.quantities))
        return total_protein, total_carbs, total_fats, total_calories


class MealPlan:
    def __init__(self, target_macros):
        self.target_protein, self.target_carbs, self.target_fats, self.target_calories = target_macros
        self.meals = {'Breakfast': Meal('Breakfast'), 'Lunch': Meal('Lunch'), 'Dinner': Meal('Dinner')}

    def add_meal(self, meal_name, food_item, quantity):
        if meal_name in self.meals:
            self.meals[meal_name].add_food_item(food_item, quantity)

    def get_daily_totals(self):
        total_protein = sum(meal.get_total_macros()[0] for meal in self.meals.values())
        total_carbs = sum(meal.get_total_macros()[1] for meal in self.meals.values())
        total_fats = sum(meal.get_total_macros()[2] for meal in self.meals.values())
        total_calories = sum(meal.get_total_macros()[3] for meal in self.meals.values())
        return total_protein, total_carbs, total_fats, total_calories

    def generate_meal_plan(self):
        # This is a simplified approach and would need a more complex algorithm in a real application
        # Randomly select food items and adjust quantities to meet macro targets
        # For demonstration purposes, we'll distribute macros evenly across meals
        target_per_meal = (self.target_protein / 3, self.target_carbs / 3, self.target_fats / 3, self.target_calories / 3)

        # For each meal, add random food items and adjust quantities to meet approximately one-third of the daily targets
        for meal_name in self.meals:
            while True:
                # Randomly select a food item and a quantity
                food_item = random.choice(food_database)
                quantity = random.uniform(0.5, 2)  # Random quantity between 0.5 and 2 servings

                # Add the food item to the meal
                self.add_meal(meal_name, food_item, quantity)

                # Check if the meal meets the target for this meal
                if all(meal >= target for meal, target in zip(self.meals[meal_name].get_total_macros(), target_per_meal)):
                    break

    def display_meal_plan(self):
        for meal_name, meal in self.meals.items():
            print(f"{meal_name}:")
            for food_item, quantity in zip(meal.food_items, meal.quantities):
                print(f"  - {food_item.name} (x{quantity:.2f} servings)")
            total_protein, total_carbs, total_fats, total_calories = meal.get_total_macros()
            print(f"    Total Macros: {total_protein:.1f}g Protein, {total_carbs:.1f}g Carbs, {total_fats:.1f}g Fats, {total_calories:.1f} Calories\n")


# Define a sample food database
food_database = [
    FoodItem("Chicken Breast", 31, 0, 3.6, 100),
    FoodItem("Brown Rice", 2.6, 23, 0.4, 100),
    FoodItem("Broccoli", 2.8, 6.6, 0.3, 100),
    # ... Add more food items here
]

# Example usage
target_macros = (150, 250, 70, 2300)  # Example target macros
meal_plan = MealPlan(target_macros)
meal_plan.generate_meal_plan()
meal_plan.display_meal_plan()

           
