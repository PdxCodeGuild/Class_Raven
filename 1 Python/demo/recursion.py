import time

def countdown(number):
    print(number)
    time.sleep(1) # pause for 1 second

    # base case (will end the loop)
    if number == 0:
        return

    countdown(number - 1)


# countdown(10)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

# print([fibonacci(n) for n in range(6)])