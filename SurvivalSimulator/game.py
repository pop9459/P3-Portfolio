from challenge import Challenge
from fileExtensionsChallenge import FileExtensionsChallenge
from mathInterpreterChallenge import mathInterpreterChallenge
from nutritionFactsChallenge import NutritionFactsChallenge
from camelCaseDecoderChallenge import CamelCaseDecoderChallenge
from emojizeChallenge import EmojizeChallenge
from guessingGameChallenge import GuessingGameChallenge

class SurvivalSimulator:
    challenges = []
    
    def __init__(self):
        # Initialize the game and add challenges
        self.challenges.append(FileExtensionsChallenge())
        self.challenges.append(mathInterpreterChallenge())
        self.challenges.append(NutritionFactsChallenge())
        self.challenges.append(CamelCaseDecoderChallenge())
        self.challenges.append(EmojizeChallenge())
        self.challenges.append(GuessingGameChallenge())


    def exitGame(self):
        print("Thanks for playing! See you next time.")
        exit()


    def showWelcomeMessage(self):
        print("Welcome to the Survival Simulator!")
        print("You are in an abandoned supermarket and must solve puzzles to escape!")


    def menu(self):

        num_challenges = len(self.challenges)

        # Display the menu options
        print("\nChoose an option:")        
        for index, challenge in enumerate(self.challenges):
            print(f"{index + 1}. {challenge.menuName}")
        print(num_challenges + 1, ". Exit")

        user_input = int(input(f"Make a choice (1-{num_challenges + 1}): "))

        if(user_input <= num_challenges):
            self.challenges[int(user_input) - 1].playChallenge()
        elif(user_input == num_challenges + 1):
            self.exitGame()
        else:
            print("Invalid choice. Please try again.")


    def gameComplete(self):
        return all(challenge.completed for challenge in self.challenges)


    def start(self):
        self.showWelcomeMessage()

        while self.gameComplete() == False:
            self.menu()

        self.exitGame()