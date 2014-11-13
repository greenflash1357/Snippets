import sys
import random
import datetime

sys.setrecursionlimit(50000)

def power(b, e):
    if e:
        return b*power(b,e-1)
    else:
        return 1

def qsum(n):
    if n:
        return n%10+qsum(n//10)
    else:
        return 0

def selfpower(n):
    return power(n,n)

def even(n):
    return n % 2 == 0

def divisors(n):
    return [x for x in range(1,n) if n % x == 0]

def isprime(n):
    if divisors(n) == [1]:
        return True
    else:
        return False

def primes(n):
    return [x for x in range(1,n+1) if isprime(x)]

def check(phone):
    if phone[0] == "+":
        if all(s in "123456789 0" for s in phone[1:]):
            return True 
    return False


def random_option():
    seq = [1, 2, 3];
    a = random.choice(seq);
    seq.remove(a);
    b = random.choice(seq);
    seq.remove(b);
    c = random.choice(seq);
    return [a,b,c];
        
def test():
    target = [1,2,3];
    success=[];
    for x in range(0,100000):
        comb = random_option();
        success.append(comb == target);
    return sum(success);



