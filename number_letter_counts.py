__author__ = 'jprout'
import datetime

start_time = datetime.datetime.now()

#No pattern to the units, so just sum them
units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
units_length = 0
for txt in units: units_length += len(txt)

#No pattern to the teens, so just sum them
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teens_length = 0
for txt in teens: teens_length += len(txt)

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#number letter counts for numbers from twenty to ninety nine
#pattern for each ten is:
#  len(ten txt) * 10  + units_length
twenty_to_ninety_nine_length = 0
for ten in tens:
    twenty_to_ninety_nine_length += len(ten) * 10 + units_length

#number letter count for 1 - 99
one_to_ninety_nine_length = units_length + teens_length + twenty_to_ninety_nine_length

#number letter count for 100 - 999
#English usage pattern is <unit> " hundred and " <tens number>, except for the first number which is <unit> hundred
total_length = 0
for unit in units:
    # a hundred times the number of hundreds
    total_length += len(unit) * 100
    # add the length of the text for a hundred numbers
    # and the previously calculated length of the 99 numbers
    # Remember to exclude spaces
    total_length += len("hundred") + len("hundredand") * 99 + one_to_ninety_nine_length

#Finally, add the length calculated for the numbers 1-99
total_length += one_to_ninety_nine_length
#and the length of "one thousand" (with no space)
total_length += len("onethousand")

elapsed = datetime.datetime.now() - start_time

#Expected result is from https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
assert total_length == 21124, "Incorrect number of letters"

print "Problem 17; Number of characters: " + str(total_length) + \
      " Execution time: " + str((datetime.datetime.now() - start_time).microseconds)
