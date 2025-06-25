
 
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

from datetime import datetime, timedelta

def displaycurrentdatetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date


def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)

        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()

        formatted_future = future_date.strftime("%Y-%m-%d")
        return formatted_future
    except ValueError:
        return "Invalid input. Please enter a valid number of days."

if __name__ == "__main__":
    print("Current date and time:", displaycurrentdatetime())
    print("Future date:", calculate_future_date())
