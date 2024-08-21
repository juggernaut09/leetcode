class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def process(i):
            if i % 3 == 0 and i % 5 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)
        return [process(i) for i in range(1, n + 1)]