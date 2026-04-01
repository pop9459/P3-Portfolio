from challenge import Challenge
from foodItem import FoodItem


class NutritionFactsChallenge(Challenge):
    menuName = "Nutrition Facts: Prepare a meal"
    needed_calories = 500
    food_items = [
        FoodItem("Apple", 95),
        FoodItem("Banana", 105),
        FoodItem("cookie", 150),
        FoodItem("sandwich", 300),
        FoodItem("water", 0)
    ]
    
    
    def playChallenge(self):
        super().playChallenge()
    
        print(f"You need to prepare a meal with {self.needed_calories} calories to proceed.")
        print("Available options: apple, banana, cookie, sandwich, water")

        total_calories = 0

        while total_calories < 500:
            user_input = input("Choose a food item to add to your meal: ").lower()

            matching_items = [item for item in self.food_items if item.name.lower() == user_input]

            if not matching_items:
                print("Invalid food item! Try again.")
                continue

            selected_item = matching_items[0]
            
            total_calories += selected_item.calories
            print(f"{selected_item.name.capitalize()} added! Total calories: {total_calories}")

        print("Congratulations! You  Your meal is complete, and you have enough energy.")
        self.completed = True
        return True