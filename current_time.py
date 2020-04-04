"""
This script returns the current system time.
"""

# Firstly we import the datetime library which contains a range of useful
# utilities for working with dates
import datetime

# Using the datetime library, we can get the current datetime stamp, 
# and then call the time() function in order to retrieve the time
time = datetime.datetime.now().time()

#It prints the time if we try it in command line
if __name__=="__main__":
    print(time)

