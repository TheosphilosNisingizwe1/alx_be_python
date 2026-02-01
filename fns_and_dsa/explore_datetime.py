from datetime import datetime, timedelta


def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    
    # Format and display the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    
    return current_date


def calculate_future_date(current_date):
    # Prompt user for number of days
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    
    # Format and display the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)


if __name__ == "__main__":
    main()
