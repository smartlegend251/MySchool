from django.test import TestCase
import random
import string
from datetime import datetime

def generate_roll_number(grade, sats_number, first_name):
    # Get the last 3 digits of sats_number
    sats_last_three = str(sats_number)[-5:]

    # Get the first letter of the first name and convert it to uppercase
    first_letter = first_name[0].upper()
    join_year = datetime.now().year % 100

    # Get the last two digits of the current year
    

    # Define the class/standard
    class_std = grade

    # Generate a random alphanumeric string of length 3
    random_chars = ''.join(random.choices(string.ascii_uppercase , k=2))
    print(random_chars)

    # Format the roll number based on the specified sequence
    roll_number = "{}-{} {}{} {}".format( first_letter, class_std, random_chars,join_year, sats_last_three)

    return roll_number

# Example usage:
grade = "10"
sats_number = "123456789"
first_name = "John"

generated_roll_number = generate_roll_number(grade, sats_number, first_name)
print(generated_roll_number)

