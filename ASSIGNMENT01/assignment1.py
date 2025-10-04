# Name : Danny Rai
# student id: 147986236

import random
import time

#funciton 1
def bubble_sort(my_list):
    steps = 0
    arrayOf = my_list[:]
    n = len(arrayOf)        
    for i in range(n - 1):
        for j in range(n - 1 - i):
            steps += 1 
            if arrayOf[j] > arrayOf[j + 1]:
                arrayOf[j], arrayOf[j + 1] = arrayOf[j + 1], arrayOf[j]
                steps += 3 
    return arrayOf, steps

#function 2
def selection_sort(my_list):
    steps = 0
    arrayOf = my_list[:]
    n = len(arrayOf)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            steps += 1
            if arrayOf[j] < arrayOf[minIndex]:
                minIndex = j
        if minIndex != i:
            arrayOf[i], arrayOf[minIndex] = arrayOf[minIndex], arrayOf[i]
            steps += 3 
    return arrayOf, steps


#function 3
def insertion_sort(my_list):
    steps = 0
    arrayOf = my_list[:]
    for i in range(1, len(arrayOf)):
        key = arrayOf[i]
        j = i - 1
        steps += 1 
        while j >= 0 and arrayOf[j] > key:
            arrayOf[j + 1] = arrayOf[j]
            j -= 1
            steps += 2
        arrayOf[j + 1] = key
        steps += 1
    return arrayOf, steps

#function 4
def quick_sort(my_list):
    arrayOf = my_list[:]
    steps = [0]
    def partition(low, high):
        pivotKey = arrayOf[high]
        i = low - 1
        for j in range(low, high):
            steps[0] += 1
            if arrayOf[j] <= pivotKey:
                i += 1
                arrayOf[i], arrayOf[j] = arrayOf[j], arrayOf[i]
                steps[0] += 3
        arrayOf[i + 1], arrayOf[high] = arrayOf[high], arrayOf[i + 1]
        steps[0] += 3
        return i + 1

    def qsort(low, high):
        if low < high:
            pi = partition(low, high)
            qsort(low, pi - 1)
            qsort(pi + 1, high)

    qsort(0, len(arrayOf) - 1)
    return arrayOf, steps[0]


#functino 5
def insertion_sort_range(my_list, left, right):
    steps = 0
    arrayOf = my_list[:]
    for i in range(left + 1, right + 1):
        key = arrayOf[i]
        j = i - 1
        steps += 1
        while j >= left and arrayOf[j] > key:
            arrayOf[j + 1] = arrayOf[j]
            j -= 1
            steps += 2
        arrayOf[j + 1] = key
        steps += 1
    return arrayOf, steps

# Step 2 Testing Best/Worst/Average
def test_cases():
    sizes = [10]
    for n in sizes:
        bestCase = list(range(n))
        worstCase = list(range(n, 0, -1))
        averageCase = [random.randint(0, 100) for _ in range(n)]

        print("\nTesting Bubble Sort with n =", n)
        print("Best case steps:", bubble_sort(bestCase)[1])
        print("Worst case steps:", bubble_sort(worstCase)[1])
        print("Average case steps:", bubble_sort(averageCase)[1])

# Step 3
def benchmark(sorting_func, sizes, name):
    stepList = []
    timeList = []

    for n in sizes:
        arrayOf = list(range(n, 0, -1)) # worst case: reverse sorted

        # Measure T(n) / steps or operaitons and Time
        _, steps = sorting_func(arrayOf)
        stepList.append(steps)

        start = time.time()
        sorting_func(arrayOf)
        end = time.time()
        timeList.append(end - start)
    
    for i in range(len(stepList)):
        print(name, " steps/T(n) = ", stepList[i], " time = ", timeList[i] )



def main():
    # Step 1 test
    arrayOf = [random.randint(0, 100) for _ in range(100)]
    print("Original list:", arrayOf[:10], "...\n")

    print("Bubble Sort:", bubble_sort(arrayOf)[0][:10])
    print("Selection Sort:", selection_sort(arrayOf)[0][:10])
    print("Insertion Sort:", insertion_sort(arrayOf)[0][:10])
    print("Quick Sort:", quick_sort(arrayOf)[0][:10])
    print("Insertion Sort Range:", insertion_sort_range(arrayOf, 0, len(arrayOf)-1)[0][:10])

    # Step 2 test
    test_cases()

    sizes = [10, 50, 100, 500, 1000]
    benchmark(bubble_sort, sizes, "Bubble Sort")
    benchmark(selection_sort, sizes, "Selection Sort")
    benchmark(insertion_sort, sizes, "Insertion Sort")


if __name__ == "__main__":
    main()
