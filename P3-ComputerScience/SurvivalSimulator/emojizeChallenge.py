from challenge import Challenge


class EmojizeChallenge(Challenge):
    menuName = "Emojize: Guess the clue"


    def playChallenge(self):
        super().playChallenge()

        print("You find a clue in emojis: 🍎 🍌 🍪")
        
        user_input = input("What do these emojis mean? (Hint: food): ").lower().strip()
        
        if user_input == "apple banana cookie":
            print("Correct! You receive a key.")
            self.completed = True
            return True
        else:
            print("That's not correct. Try again!")
            return False