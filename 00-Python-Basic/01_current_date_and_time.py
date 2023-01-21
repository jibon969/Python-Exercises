
# Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print (now.strftime("%Y-%m-%d %H:%M:%S"))

                                 
"""
date.strftime(format) returns a string representing the date, controlled by an explicit format string.
Format codes referring to hours, minutes or seconds will see 0 values.
"""
