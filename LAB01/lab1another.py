# Name : Danny Rai
# student id: 147986236


# Function 1
def wins_rock_scissors_paper(ch1, ch2):
    choices = ["rock", "paper", "scissors"]
    ch1 = ch1.lower()
    ch2 = ch2.lower()

    if ch1 not in choices or ch2 not in choices:
        return False

    if ch1 == ch2:
        return False

    elif (ch1 == "rock" and ch2 == "scissors") or \
         (ch1 == "paper" and ch2 == "rock") or \
         (ch1 == "scissors" and ch2 == "paper"):
        return True

    else:
        return False

# Fucniton 2
def factorial(n):
    product = 1
    for num in range(1, n + 1):
        product *= num
    return product

# Function 3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fn, fn_1 = 0, 1
    for _ in range(2, n+1):
        fn, fn_1 = fn_1, fn + fn_1
    return fn_1

# Function 4
def sum_to_goal(number, goal):
    sum = 0
    for num1 in number:
        for num2 in number:
            if (num1 + num2 == goal):return num1 * num2
    return 0


# up counter and Downcounter
class UpCounter:
    def __init__(self, step =1):
        self.counter = 0
        self.step = step

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.step

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.step
