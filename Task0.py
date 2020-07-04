"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    incoming, answering, timestamp = list(reader)[0]
    print(f'First record of texts, {incoming} texts {answering} at time {timestamp}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    incoming, answering, timestamp, seconds = list(reader)[-1]
    print(f'Last record of calls, {incoming} calls {answering} at time {timestamp}, lasting {seconds} seconds')
    

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

