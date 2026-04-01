from challenge import Challenge


class CamelCaseDecoderChallenge(Challenge):
    menuName = "CamelCase Decoder: Decode the message"
    message = "EscapeNowThroughDoor"

    def playChallenge(self):
        super().playChallenge()

        print(f"You find a message in camelCase: '{self.message}'")

        user_input = input("Type the CamelCase message to decode it: ")

        decoded_message = ""
        for ch in user_input:
            if ch.isupper() and decoded_message:
                decoded_message += " "
            decoded_message += ch
        
        decoded_message = decoded_message.strip()

        print("Decoded message: " + decoded_message)
        self.completed = True
        return True