# Palindrome is a string that reads the same forward as it does backwards. e.g., "racecar", "level", "madam".
# This code uses rolling hashes to efficiently check if a given string can be rearranged to form
# a palindrome by comparing the hash of the string with the hash of its reverse.
# Hash: f("radar") = 17
# Rollimg hash: f("radars") = f("radar" + "s") = f("radar")~"s"

import random

def naive(str):
    str_rev = str[::-1] # Reverse the string
    n = len(str) # Get length of string     
    p = 31 # A prime number as base for polynomial rolling hash
    for i in range(n, -1, -1):
        if str_rev[i:] == str[i-1::-1]:
            return str + str_rev[i:]
        
def rolling_hash(str):
    p = 23
    p = 666013
    str_rev = str[::-1] # Reverse the string
    f_forward = 0 # Hash for the original string
    f_backward = 0 # Hash for the reversed string
    p_power = 1 # p^i
    max_suffix_palindrome = 0 # Length ofvariable to store the longest palindromic suffix
    # iterate over the reverse string
    for i, c in enumerate(str_rev):
        # ompute the index of the current char in the english alphabet
        c_idx = ord(c) - ord('a') # ord gives ASCII value of the input character
        # we assume thet the input is made of lowercase english letters only.
        # compute f_forward and f_backward
        f_forward = (f_forward + c_idx * p_power) % p # Rolling hash for original string
        f_backward = (f_backward * p + c_idx) % p # Rolling hash for reversed string
        p_power = (p_power * p) % p # Update p^i for next iteration
        # %p to avoid overflow
        # If the hashes match, we found a palindromic suffix
        if f_forward == f_backward:
            max_suffix_palindrome = i # Update length of longest palindromic suffix
    # Construct and return the palindrome
    return str + str_rev[max_suffix_palindrome+1:]


str = 'loaded'
print('niave str: ', naive(str))
print(rolling_hash(str))