
 
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Task '{task}' has an unknown priority"

if time_bound == "yes":
    message += " that requires immediate attention today!"

print(message)
task = input("Enter your task: ") 
priority = input("Priority (high/medium/low): ").lower() 
time_bound = input("Is it time-bound? (yes/no): ").lower() 
 
match priority: 
    case "high": 
        message = f"'{task}' is a high priority task" 
    case "medium": 
        message = f"'{task}' is a medium priority task" 
    case "low": 
        message = f"'{task}' is a low priority task" 
    case _: 
        message = f"'{task}' has an unspecified priority" 
 
if time_bound == "yes": 
    print(f"Reminder: {message} that requires immediate attention today!") 
else: 
    print(f"Note: {message}. Consider completing it when you have free time.") 

