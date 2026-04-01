def main():
    while True:
        try:
            input_fraction = input("Fraction: ")
            fuel_gauge = gauge(convert(input_fraction))
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    
    print(fuel_gauge)


def convert(fraction):
    if fraction.count("/") != 1:
        raise ValueError("Invalid input")

    fraction = fraction.split("/")
    X = int(fraction[0])
    Y = int(fraction[1])

    if Y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if X > Y:
        raise ValueError("Numerator cannot be greater than denominator")

    percentage = int((X/Y) * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
