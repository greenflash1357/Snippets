import string
import random

alphabet = list(string.ascii_lowercase)   
key = list(string.ascii_lowercase)
random.shuffle(key)  
keydict = {};
for c in range(0,len(alphabet)):
    keydict[alphabet[c]] = key[c]; 