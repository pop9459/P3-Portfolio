def is_valid(s):
    if(len(s) < 2 or len(s) > 6):
        # The length of the plate must be between 2 and 6 characters
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        # The first two characters must be letters
        return False
    if not check_number_position(s):
        # The numbers must be at the end of the plate and cannot start with 0
        return False
    if not s.isalnum():
        # The plate must only contain letters and numbers 
        return False
    
    # Return True if all conditions are satisfied
    return True

def check_number_position(s):
    numbers_started = False

    for char in s:
        if char.isdigit():
            if char == "0" and not numbers_started:
                return False
            numbers_started = True
            continue

        if char.isalpha() and numbers_started:
            return False

    return numbers_started
