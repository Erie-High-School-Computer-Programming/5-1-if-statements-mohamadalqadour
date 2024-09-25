def check_age_21(age: int) -> bool:
    """
    Check if the age is 21 or older
    """
    return age >= 21


def check_grade_level(grade: str) -> bool:
    """
    Check if the grade level is valid (9-12) and print the corresponding grade name.
    """
    grade_levels = {'9': 'freshman', '10': 'sophomore', '11': 'junior', '12': 'senior'}
    grade_str = str(grade)  # Ensure the grade is treated as a string
    if grade_str in grade_levels:
        print(grade_levels[grade_str])
        return True
    return False


def check_date_of_birth(date_of_birth: str) -> bool:
    """
    Check if the date of birth is between 1900 and the current year.
    """
    from datetime import datetime
    current_year = datetime.now().year
    
    try:
        year_of_birth = int(date_of_birth)
    except ValueError:
        return False

    if 1900 <= year_of_birth <= current_year:
        print(current_year)
        return True
    return False


def check_the_list_of_cars(car_list: list) -> bool:
    """
    Check if the car list contains at least 3 unique cars and return the count of unique cars.
    """
    unique_cars = set(car_list)
    if len(unique_cars) >= 3:
        print(len(unique_cars))
        return True
    return False


def check_if_you_can_drive(can_you_drive: str) -> bool:
    """
    Check if the driving eligibility is valid (either 'yes' or 'no').
    """
    if can_you_drive.lower() == 'yes':
        print('You can drive')
        return True
    elif can_you_drive.lower() == 'no':
        return False
    return False


def check_weather(weather: str) -> bool:
    """
    Check if the weather condition is valid.
    """
    valid_weather = ['sunny', 'rainy', 'snowy', 'wind']
    if weather.lower() in valid_weather:
        print(weather)
        return True
    return False


import random
def check_if_you_can_play_game() -> bool:
    """
    Randomly generates a boolean value and returns a message if the result is True.
    """
    import random
    can_play = random.choice([True, False])
    if can_play:
        return 'You can play game'
    return False



def check_study_time_or_play_time(study_time_or_play_time: str) -> bool:
    """
    Check if the input is either 'study' or 'play'.
    """
    valid_choices = ['study', 'play']
    if study_time_or_play_time.lower() in valid_choices:
        print(study_time_or_play_time)
        return True
    return False


def make_the_input_store_in_variable(input_string: str) -> str:
    """
    Store the input in a variable and convert it to the appropriate type (int, float, or str).
    """
    user_input = input_string
    try:
        if '.' in input_string:
            user_input = float(input_string)
        else:
            user_input = int(input_string)
    except ValueError:
        user_input = input_string  # Keep it as a string if it's not a number
    return user_input


def check_if_the_number_is_even(number: int) -> bool:
    """
    Check if the given number is even.
    """
    return number % 2 == 0
