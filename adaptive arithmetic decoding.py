import sys
import random
import string
import decimal
from decimal import Decimal

decimal.getcontext().prec=100


def decode(encoded, strlen, every):
    decoded_str = ""

    count = dict.fromkeys(string.digits, 1)                                        # probability table
    cdf_range = dict.fromkeys(string.digits, 0)
    pdf = dict.fromkeys(string.digits, 0)

    low = 0
    high = Decimal(1)/Decimal(10)
    for key, value in sorted(cdf_range.items()):
        cdf_range[key] = [low, high]
        low = high
        high += Decimal(1)/Decimal(10)

    for key, value in sorted(pdf.items()):
        pdf[key] = Decimal(1)/Decimal(10)


    lower_bound = 0                                                                     # upper bound
    upper_bound = 1                                                                     # lower bound

    k = 0

    while (strlen != len(decoded_str)):
        
        for key, value in sorted(pdf.items()):

            curr_range = upper_bound - lower_bound                                      # current range
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])                 # upper_bound
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])                 # lower bound

            if (lower_cand <= encoded < upper_cand):
                k += 1
                decoded_str += key

                if (strlen == len(decoded_str)):
                    break

                upper_bound = upper_cand
                lower_bound = lower_cand

                count[key] += 1

                if (k == every):
                    k = 0
                    for key, value in sorted(pdf.items()):
                        pdf[key] = Decimal(count[key])/Decimal(10+len(decoded_str))

                    low = 0
                    for key, value in sorted(cdf_range.items()):
                        high = pdf[key] + low
                        cdf_range[key] = [low, high]
                        low = high
    return decoded_str
   

def main():
   
    with open('Encoded sentence written in bits.bin', 'r') as file:
        data = file.read()
    length=len(data)
    
    l=[]
    
    for i in range(0,length,1):
        if(data[i]!=" " and data[i]!="[" and data[i]!="," and data[i]!="]"):
            l.append(data[i])

    l=''.join(l)
    
    
    
    every = 19

    
    s="0."+l
    s1=(Decimal(s))
    strlen = len(s)
    
    
    decoded = decode(s1, strlen, every)
   
    with open('Resulting decoded sequence.txt', 'w') as f2:
        f2.write(decoded)

if __name__ == '__main__':
    main()