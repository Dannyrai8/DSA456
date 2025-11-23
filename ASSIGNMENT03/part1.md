# Name : Danny Rai
# student id: 147986236
Part A - Function Analysis for SortedTable

# 1 insert(self, key value)
this funciton checks if the key already exists and if it doesn't then it will add a new key-value pair, and expands the entire list when it's full. It uses bubble sort to sort the list which means it still has the same disabvantages of a bubble sort which is extremely slow for large lists. 
time complexity = Search O(n) + copy O(n) + sort O(n)
worst case = O(n²)

# 2 modify(self, key, value)
It loops through the list from the start untill it finds teh matching key which will then update the value. Although it scans the whole list it is not fast as the list is already sorted and if used binary search it could be done faster.
the time complexity for it is 
O(n)

# 3 remove(self, key)
This function will first search for the key and when its found it shifts all the element to the right of the list to a step left and set the last element to none, which is very inefficient as the shifting one after the other is very slow and a linked list or a has table would have solved it easily
The time complexity is = O(n)(Search = O(n) + move = O(n))

# 4 search(self, key)
this function looks through the list untill the key is found which is slow compared to binary search becuase the list is already sorted

# 5 capacity(self)
this function returns the value of the capacity

# 6 __len__(self)
this function loops through the list and counts al the non-None items on the list after counting them it simply returns the value. One way to make it shorter would be to simply have a size variable instead of counting everytime.

