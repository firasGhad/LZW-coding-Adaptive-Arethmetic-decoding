import random as rand
import math
import numpy as np
import binascii
import sys
import random
import string
import struct
import decimal
from decimal import Decimal

decimal.getcontext().prec=100

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(0,dict_size,1 ))#need to build the dictionary
    c=" "
    w=" "
    w1 = " "
    w2 = " "
    result = []
    newlist=[]
    length=len(uncompressed)
    for i in range(0,length,2):
        j=i+1
        newlist.append(uncompressed[i]+uncompressed[j])
    
   
    for i in range(0,len(newlist)):
        wc=w+newlist[i] 
     
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    


    return result
 
 


   
 
 
 
# How to use:
def main():
    
   
    with open('Initial sentence.txt', 'r') as file:
        data = file.read().replace('\n', '')
    
    
    compressed = compress(data)
     
    str1 = ''.join(str(compressed))
    bin =' '.join(format(ord(x), 'b') for x in str1)
    every=9
  
    with open('Encoded sentence written in bits.bin', 'wb') as f1:
        f1.write(bytes(str1,encoding='utf8'))
    with open('Encoded sentence (bits written as text).txt', 'w') as f2:
        f2.write(bin)
    
   
    
if __name__ == '__main__':
    main()




    


    