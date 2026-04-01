from random import randint
from challenge import Challenge


class GuessingGameChallenge(Challenge):
    menuName = "Guessing Game: Guess the secret code"

    min_value = 1
    max_value = 10
    attempts = 3
    secret = None


    def playChallenge(self):
        super().playChallenge()

        secret = randint(self.min_value, self.max_value)

        print(f"A secret code (between {self.min_value} and {self.max_value}) must be guessed.")

        for attempt in range(self.attempts):
            user_input = int(input(f"Guess the code (attempts left: {self.attempts-attempt}): "))
            
            if user_input == secret:
                print("Correct! The door opens.")
                self.completed = True
                return True
            elif user_input < secret:
                print("Too low!")
            else:
                print("Too high!")
        
        print(f"Unfortunately! The code was {secret}.")
        return False