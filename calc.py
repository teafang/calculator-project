# Tip Calculator
    # Ask for meal price
    # Ask how the waitier was (give a few options)
    # Suggested tip: give 2 options
    # Choose tip percent
    # Calculate tip
# Extra 1: calculate total meal cost (food cost, tax, tip)
# Extra 2: ask for weekly budget and then subtract to give remaining amount in budget

# Welcome
print("Welcome to the X Tip Calculator!")
input("How was your meal?")
print("Wonderful! Now let's calculate how much your tip will be.")

# Tip Suggestion based on waiter rating
def suggestion(meal, service):
    # Service recommendation
    if service <  5:
        print("Sorry to hear that!")
        suggest = "10%" + " or 15%"
    elif 5 <= service < 8:
        print("Awesome")
        suggest = "15%" + " or 20%"
    else:
        print("Awesome!")
        suggest = "15%" + " or 20%"
    # while
    print(f"Based on your input, we suggest a tip of {suggest}")

# Tip Calculation
def tip_amount(meal, percent):
    if percent.isdigit() == True:
        tip = meal * (float(percent)/100)
    else:
        percent = percent[:-1]
        tip = round(meal * (float(percent)/100), 2)
    return tip

# Total Tip Amount and Meal Price
def meal_price(meal, percent):
    print(f"Your tip amount is: ${tip_amount(meal, percent)}")
    total = meal + tip_amount(meal, percent)
    print(f"Your total meal price is: ${total}")

# Inputs
meal = float(input("What was the total price of your meal (including tax)?"))
service = int(input("Great! How would you rate your service from 1 to 10? (10 being highest)"))
suggestion(meal, service)
percent = (input("What percent tip would you like to give? (Enter non-decimal number)"))
meal_price(meal, percent)
