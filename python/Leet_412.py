from _ast import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        # Iterate through each number from 1 to n (inclusive)
        for number in range(1, n + 1):
            # Initialize an empty string to build the "FizzBuzz" result
            fizz_buzz_str = ""

            # Check if the current number is divisible by 3
            if number % 3 == 0:
                fizz_buzz_str += "Fizz"

            # Check if the current number is divisible by 5
            if number % 5 == 0:
                fizz_buzz_str += "Buzz"

            # If the number is not divisible by either 3 or 5, use the number itself
            if not fizz_buzz_str:
                fizz_buzz_str = str(number)

            # Append the result to the list
            result.append(fizz_buzz_str)

        # Return the final list containing the "FizzBuzz" results
        return result