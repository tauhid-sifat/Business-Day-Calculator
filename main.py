import datetime

# Define the fixed year
fixed_year = 2024

# Define the list of national holidays
holidays = [
    "21/02/2024",
    "26/02/2024",
    "17/03/2024",
    "26/03/2024",
    "07/04/2024",
    "10/04/2024",
    "11/04/2024",
    "12/04/2024",
    "14/04/2024",
    "01/05/2024",
    "22/05/2024",
    "16/06/2024",
    "17/06/2024",
    "18/06/2024",
    "17/07/2024",
    "15/08/2024",
    "26/08/2024",
    "16/09/2024",
    "13/10/2024",
    "16/12/2024",
    "25/12/2024"
]

# Function to check if a date is a holiday
def is_holiday(date_str):
    return date_str in holidays

# Function to check if a date is a Friday or Saturday
def is_weekend(date_str):
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
    return date.weekday() in [4, 5]

# Function to calculate the final date
def calculate_final_date(start_date_str, num_days):
    if is_weekend(start_date_str):
        return "Error: Start date cannot be a Friday or Saturday."

    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y")
    current_date = start_date

    while num_days > 0:
        # Check if the current day is a holiday, Friday, or Saturday
        current_day = current_date.strftime("%d/%m/%Y")
        if not is_holiday(current_day) and current_date.weekday() not in [4, 5]:
            num_days -= 1
        current_date += datetime.timedelta(days=1)

    return current_date.strftime("%d/%m/%Y")

# Input start date (day and month) and number of working days
start_date_str = input("Enter the start date (DD/MM): ")
num_days = int(input("Enter the number of working days: "))

# Concatenate the fixed year to the input date
start_date_str = f"{start_date_str}/{fixed_year}"

# Calculate the final date
final_date = calculate_final_date(start_date_str, num_days)
print("Final date after", num_days, "working days:", final_date)