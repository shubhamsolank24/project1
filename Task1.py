"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
    phonenum = set()

for numbers in  texts:
    phonenum.add(numbers[0])
    phonenum.add(numbers[1])
for numbers in calls:
    phonenum.add(numbers[0])
    phonenum.add(numbers[1])
    count =len (phonenum)
print(f'There are { count } different telephone numbers in the records')
    


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
