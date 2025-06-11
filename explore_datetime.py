from datetime import datetime, timedelta

def displaycurrentdatetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        return formatted_future
    except ValueError:
        return "Invalid input. Please enter a valid number of days."

if __name__ == "__main__":
    print("Current date and time:", displaycurrentdatetime())
    print("Future date:", calculate_future_date())
