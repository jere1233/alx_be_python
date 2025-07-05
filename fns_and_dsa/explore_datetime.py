from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid input. Please enter a valid number of days."

if __name__ == "__main__":
    print("Current date and time:", display_current_datetime())
    print("Future date:", calculate_future_date())
