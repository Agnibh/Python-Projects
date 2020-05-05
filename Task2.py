"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
callDict={}
for row in calls:
    callDict[row[0]]=callDict.get(row[0],0)+int(row[3])
    callDict[row[1]]=callDict.get(row[1],0)+int(row[3])

keys=list(callDict.keys())
values=list(callDict.values())
maxValue=max(values)
index=values.index(maxValue)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(keys[index],maxValue))
