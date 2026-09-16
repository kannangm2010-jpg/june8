"""
Find Employees Present in Both Teams 
Two project teams are formed. Find employees working in both teams.
Input
team_a = {"John", "Mary", "Tom", "David"}
team_b = {"Tom", "David", "Sam", "Alex"}

Logic
1.	Convert both collections into sets. 
2.	Use intersection(). 
3.	Common employees will be returned. 

Program
"""
team_a = {"John", "Mary", "Tom", "David"}
team_b = {"Tom", "David", "Sam", "Alex"}

common = team_a.intersection(team_b)

print("Working in both teams:", common)
