# Name : Danny Rai
# student id: 147986236


## Part 1

#Functino 1
def function1(number):
	total = 0                   # 1
 
	for i in range(number):     # n - 1
		x = i + 1               # 2n
		total += x * x          # 3n
	return total                # 1
"""
T(n) = Total number of operations = 1 + n + 2n + 3n = 6n + 1
T(n) = 6n + 1
After removing constants Time = O(n)
"""

#Function 2
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6 # 7

"""
T(n) = Total number of operations = 7
T(n) is constant so we get time = O(1)
"""

#Function 3
def function3(list):
	n = len(list)                       # O(1)
	for i in range(n - 1):              # n - 1 (0 ... n - 1 - 1 )
		for j in range(n - 1 - i):      # n - 1 - i
			if list[j] > list[j+1]:     # 1
				tmp = list[j]           
				list[j] = list[j+1]
				list[j + 1] = tmp
"""
Here T(n) = T(n - 1 - i) = n - 1 + n - 2 + ... + 1 = (n(n - 1))/ 2 (Triangular formula)
So, 
    T(n) = Total number of operations = (n(n - 1))/ 2
    T(n) = (n² - n) / 2 = O(n²)
"""


#Function 4
def function4(number):
	total = 1                   # 1
	for i in range(1, number):  # n - 1
		total *= i + 1          # 3(n - 1)
	return total                # 1

"""
T(n) = Total number of operations = 1 + 3(n - 1) + 1 = 2 + 3n - 3 = 3n - 1
T(n) = 3n - 1 = O(n)
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fn, fn_1 = 0, 1
    for _ in range(2, n+1):
        fn, fn_1 = fn_1, fn + fn_1
    return fn_1
    # if n <= 1:
    #     return n
    # return fibonacci(n-1) + fibonacci(n-2)


def sum_to_goal(number, goal):
    sum = 0
    for num1 in number:
        for num2 in number:
            if (num1 + num2 == goal):return num1 * num2
    return 0
