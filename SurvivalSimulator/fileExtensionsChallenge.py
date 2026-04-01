from challenge import Challenge


class FileExtensionsChallenge(Challenge):
    menuName = "File Extensions: What's in this file?"
    
    def playChallenge(self):
        super().playChallenge()

        file_name = "recipe.pdf"

        print(f"You find a file named '{file_name}'.")
        user_input = input("Type the name of the file to check its extension: ")

        success = user_input == file_name

        if success:
            print(f"This is a {file_name.split(".")[1].upper()} file containing a {file_name.split(".")[0]}!")
            self.completed = True
        else:
            print("That's not the correct file name. Try again!")

        return success