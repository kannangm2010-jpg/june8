"""
Find All Numbers Appearing Exactly Once
Given an array of integers, some numbers may appear multiple times.
Write a program to find and return all numbers that appear exactly once in the array.
The output should preserve the order in which the numbers first appear.
________________________________________
Input
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
________________________________________
Output
[3, 4, 5, 6]

"""
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
u=[]
for i in numbers :
	if numbers.count(i)==1:
			u.append(i)
print(u)
----------------------------------------------------------------------------------
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
u=[]
for i in numbers :
	if numbers.count(i)>1:
			u.append(i)
print(set(u))
---------------------------------------------------------------------------------
numbers = [1, 2, 3, 2, 4, 5, 1, 6]

l = len(numbers)

i = 0

result = []

while i < l:

    count = 0

    j = 0

    while j < l:

        if numbers[i] == numbers[j]:
            count = count + 1

        j = j + 1

    if count == 1:
        result.append(numbers[i])

    i = i + 1

print(result)
----------------------------------------------------------------------------------