
""" This script counts the number of lines in stadard input
Input: strings form the system's standarrd input
Output: a string with the total number of lines

"""


import sys

count = 0
for line in sys.stdin: 
	count += 1

print(count, 'lines in standard input')

