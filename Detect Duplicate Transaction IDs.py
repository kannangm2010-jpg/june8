Detect Duplicate Transaction IDs
A bank receives transaction IDs. Detect and print all duplicate transaction IDs.
Input
	transactions = [1001, 1002, 1003, 1002, 1004, 1005, 1001]
Logic
1.	Maintain one set for seen transactions. 
2.	Maintain another set for duplicates. 
3.	If transaction already exists in seen set, add to duplicate set. 
 
Program
transactions = [1001, 1002, 1003, 1002, 1004, 1005, 1001]

seen = set()
duplicates = set()

for txn in transactions:
    if txn in seen:
        duplicates.add(txn)
    else:
        seen.add(txn)

print("Duplicate Transactions:", duplicates)