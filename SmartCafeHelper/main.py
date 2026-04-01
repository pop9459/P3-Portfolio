def welcome_message():
    welcome_message = "Welcome to Smart Cafe!"
    print(welcome_message)

    user_input = input("Would you like to customize the welcome message? (yes/no): ").lower()
    if user_input == "yes":
        welcome_message = input("Enter your custom message: ")

    print(transform_message(welcome_message))

def transform_message(input_message):
    new_message = ""
    for char in input_message:
        new_message = new_message + char + "..."
    
    new_message = new_message.removesuffix("...")

    return new_message

def process_orders():
    total_order_price = 0

    # do while loop
    while True:
        # Get order item
        user_input = input("Please enter your order or type 'done' to finish: ").lower()
        order_output = get_item_type(user_input)
        if(order_output == False):
            break
        else:
            energy_coeficient = order_output

        # Calculate energy
        user_input = input("Would you like to calculate energy? (yes/no): ").lower()
        if(user_input == "yes"):
            print(f"Energy: {calculate_energy(energy_coeficient)} Joules")

        # Increment price
        total_order_price += get_item_price()

    print(f"Your total is ${total_order_price}.")

    price_after_tip = process_tip(total_order_price)
    print(f"With tip, your total is: ${price_after_tip}")

def process_tip(price_before_tip):
    while True:
        user_input = float(input("How much tip would you like to add? (10, 15, 20): "))
        price_after_tip = price_before_tip + price_before_tip * (user_input / 100)

        return price_after_tip

def get_item_type(user_input):
        match user_input:
            case "done":
                #finish ordering
                return False
            case "coffe":
                order_item = "☕"
                energy_coeficient = 1
            case "tea":
                order_item = "🫖"
                energy_coeficient = 2
            case "cake":
                order_item = "🍰"
                energy_coeficient = 3
            case "cookie":
                order_item = "🍪"
                energy_coeficient = 4
            case "cheese":
                order_item = "🧀"
                energy_coeficient = 5
            case _:
                order_item = user_input.lower()
                energy_coeficient = 0.5
                pass

        print("Okay, I will prepare " + order_item)
        return energy_coeficient

def get_item_price():
    user_input = input("Please enter the price of this item: ")
    item_price = float(user_input.removeprefix("$"))
    return item_price
    

def calculate_energy(energy_coeficient):
    item_weight = float(input("Enter the weight in grams: "))
    item_energy = item_weight * pow(energy_coeficient, 2)
    return item_energy


if __name__ == "__main__":
    welcome_message()
    process_orders()
    print("Thank you for visiting Smart Cafe!")