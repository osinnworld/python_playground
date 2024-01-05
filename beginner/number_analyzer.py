#!/usr/bin/python3

# Number analyzer program

numbers = []
count = 0
total = 0
minimum = float('inf')
maximum = float('-inf')

print("Program Start")

while True:
    # User input
    user_input = input(":) Enter a number (type '=' to display statistics, 'exit' to end): ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        break
    elif user_input == '=':
        # Display analysis for each entered number
        if count > 0:
            print("_" * 70)
            for num in numbers:
                result = ""

                if num > 0:
                    result += "(+)POSITIVE"
                elif num < 0:
                    result += "(-)NEGATIVE"
                else:
                    result += "ZERO"

                if num % 2 == 0:
                    result += ", EVEN, Number"
                else:
                    result += ", ODD, Number"

                print(f"{num}: {result}")
            print("_" * 70)

            # Calculate and print statistics
            average = total / count
            print("\nStatistics:")
            print(f"Count: {count}")
            print(f"Sum: {' + '.join(map(str, numbers))} = {total}")
            print(f"Average: {average:.2f}")
            print(f"Minimum: {minimum}")
            print(f"Maximum: {maximum}")
            print("_" * 70)
        else:
            print("\nNo valid numbers entered.")
    else:
        try:
            # Convert user input to a floating-point number
            n1 = float(user_input)
            n = round(n1)

            # Statistics
            numbers.append(n)
            count += 1
            total += n
            minimum = min(minimum, n)
            maximum = max(maximum, n)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Print final message
print("\nProgram Ended.")

