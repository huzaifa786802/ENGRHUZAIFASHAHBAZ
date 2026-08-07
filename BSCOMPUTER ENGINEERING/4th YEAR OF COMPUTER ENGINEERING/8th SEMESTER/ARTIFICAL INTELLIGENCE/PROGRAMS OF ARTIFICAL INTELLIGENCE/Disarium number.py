def is_disarium_number(number):
    # Convert the number to a string to easily iterate through its digits
    num_str = str(number)
    # Calculate the sum of digits raised to their respective positions
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    # Check if the sum equals the original number
    return disarium_sum == number
# Test the function with some example numbers
def test_disarium_numbers():
    # Test cases
    test_numbers = [175, 89, 135, 518, 100, 200]
    for num in test_numbers:
        result = is_disarium_number(num)
        print(f"{num} is {'a' if result else 'not a'} Disarium number")
# Run the test function
test_disarium_numbers()