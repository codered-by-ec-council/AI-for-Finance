'''loop_function.py'''

'''
We are creating a simple python custom function to test the capability
'''

import numpy as np
import pandas as pd

def isPhoneN(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 100-200-0000 tomorrow. 415-555-6666 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneN(chunk):
        print('Phone number found: ' + chunk)
print('Done')

def add_number(a:int, b:int)->int:
    '''
    Add two numbers together

    Returns
    -------
    the_sum : type of arguments
    '''

    return a + b


print('100-200-4242 is a phone number:')
print(isPhoneN('100-200-4242'))
print(isPhoneN('Hello World of Python'))
print('Addition of two numbers:', add_number(5,10))
