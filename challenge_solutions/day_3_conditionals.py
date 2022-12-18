#--- Challenge Solution ---#
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    #check to see if n is odd

    if N%2!=0:
        print("Weird")
    
    #check to see if n is even
    if N%2 == 0:
        #n falls within the range of 2 and 5. In this case it will check 2, 3, 4, and 5 but not 6
        if N in range (2,6):
            print("Not Weird")
        #n falls within range of 6 and 20. i.e.  n is from 6 to 20
        if N in range (6, 21):
            print("Weird")
        #n is greater than 20
        if N > 20:
            print("Not Weird")
        