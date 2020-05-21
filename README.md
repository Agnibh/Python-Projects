# Python-Projects

***About the data***
The text and call data are provided in csv files.
The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:
Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

***Task0***-Read file into texts and calls.

***Task1***-How many different telephone numbers are there in the records?

***Task2***-Which telephone number spent the longest time on the phoneduring the period? Don't forget that time spent answering a call is
also time spent on the phone.

***Task3***-(080) is the area code for fixed line telephones in Bangalore.Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
   
***Task4***-The telephone company want to identify numbers that might be doing telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls
