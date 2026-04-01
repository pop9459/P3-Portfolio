import random
from challenge import Challenge


class mathInterpreterChallenge(Challenge):
    menuName = "Math Interpreter: Unlock the safe"

    def playChallenge(self):
        super().playChallenge()

        print("A safe unlocks only with the correct mathematical calculation.")
        
        user_input = input("Enter the mathematical expression (e.g., 2 + 3 * 4): ")

        try:
            result = eval(user_input)
        except Exception as e:
            print("Invalid expression! Try again.")
            return False
        
        print(f"The result is: {result}. The safe opens!")
        self.completed = True
        return True