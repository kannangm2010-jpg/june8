"""Find Unique Visitors to a Website
A website logs visitor IDs. Some visitors visit multiple times. Find how many unique visitors visited the website.
Input
	visitors = [101, 102, 103, 101, 104, 102, 105]
Logic
1.	A set stores only unique values. 
2.	Convert the list into a set. 
3.	Count the elements in the set. 

Program
"""
visitors = [101, 102, 103, 101, 104, 102, 105]

unique_visitors = set(visitors)

print("Unique Visitors:", unique_visitors)
print("Count:", len(unique_visitors))