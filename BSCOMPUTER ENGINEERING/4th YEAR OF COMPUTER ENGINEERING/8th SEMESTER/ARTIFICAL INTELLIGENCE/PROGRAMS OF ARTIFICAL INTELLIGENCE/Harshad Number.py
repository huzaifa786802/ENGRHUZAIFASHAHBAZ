def is_harshad_number(number):
    # Convert the number to a string to easily iterate through its digits
    num_str = str(number)
    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in num_str)
    # Check if the number is divisible by the sum of its digits
    return number % digit_sum == 0
def main():
    # Test the function with some examples
    test_numbers = [54, 120, 156, 18, 10, 22, 100, 63]
    print("Harshad Number Checker")
    print("-" * 25)
    
    for num in test_numbers:
        result = is_harshad_number(num)
        print(f"{num} is{' ' if result else ' not '}a Harshad Number")
        if result:
            print(f"  Digit Sum: {sum(int(digit) for digit in str(num))}")
        print()
# Allow the script to be run directly or imported as a module
if __name__ == "__main__":
    main()