"""
Find Pair With Given Sum
Find whether two numbers exist whose sum equals a target value.
Input
numbers = [2, 7, 11, 15]
target = 9

-----------------------------------------------------------------------------------
"""


numbers = [2, 7, 11, 15]

target = 17

l = len(numbers)

i = 0
is_found=False

while i < l:

    j = 0

    while j < l:

        if i != j:

            if numbers[i] + numbers[j] == target:
                print("Answer Found:", numbers[i], numbers[j])
                is_found=True
                break
		

        j = j + 1

    i = i + 1
if is_found:
	print("targt found")
else:
	print(' target not found')         
			
"""
target	l	i	while i < l	 j	while j < l	i != j	 if numbers[i] + numbers[j] == target
17	4	0	yes		0	yes		no	
17	4	0	yes	 	1	yes   		yes	 2 +7==17   false
17	4	0	yes	 	2	yes`		yes	 2+11==17   false
17	4	0	yes		3	yes		yes	 2+15==17   true
17	4	0	yes		4	no
17	4	1	yes		0	yes		yes	7+2==17  	false
17	4	1	yes		1	yes		no

target	l	i	while i < l	 j	while j < l	i != j	 if numbers[i] + numbers[j] == target	
19	4	0	yes		
"""