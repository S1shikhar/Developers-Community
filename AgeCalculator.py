from datetime import datetime

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Input: Birthdate from user
day = int(input("Enter your birth day (DD): "))
month = int(input("Enter your birth month (MM): "))
year = int(input("Enter your birth year (YYYY): "))

# Create a datetime object for the birthdate
birthdate = datetime(year, month, day)

# Calculate and display the age
age = calculate_age(birthdate)
print(f"You are {age} years old.")
