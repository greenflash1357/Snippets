import time 
import sys
import math
import random
from fractions import Fraction, gcd
from collections import Counter

sys.setrecursionlimit(5000)

# def power(base, exp):
#     if exp==0: 
#         return 1;
#     if base==0:
#         return 0;
#     if exp%2 == 0:
#         return (power(base*base, exp/2))%10**10;
#     else:
#         return (base*power(base*base, int(exp/2)))%10**10;
# 
# def pe97():                    
#     res = power(2,7830457)
#     return (res*28433+1)%10**10;
#         
# print(pe97());
# 
# 
# def pe79():
#         codes = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716];
#         key = list(map(int, str(codes[0])));
#         return key;
# 
# print(pe79());
# 
# 
# def pe63():
#     count = 0;
#     for e in range(1,101):
#         for b in range(1,101):
#             if len(str(b**e))==e:
#                 count += 1;
#                 #print('%d ^ %d = %d' %(b,e,b**e))
#     return count;
# 
# print(pe63()); 
# 
# def step(n):
#     res = 0;
#     while n:
#         res += (n%10) * (n%10);
#         n //= 10;
#     return res;
# 
# def chain(n):
#     while (n!=1) and (n!= 89):
#         n = step(n);
#     return n;
# 
# def pe92():
#     start = time.time()
#     count = 0;
#     d = {};
#     for n in range(1,568):
#         d[n]=chain(n);
#     for n in range(1,10000000):
#         tmp = step(n);
#         if d[tmp]==89:
#             count += 1;
#     print('Time: %f seconds' %(time.time()-start))
#     return count;
# 
# #print(pe92());

def keywithmaxval(d):
    v=list(d.values());
    k=list(d.keys());
    return k[v.index(max(v))];

# def pe59():
#     cipher = [79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68,4,7,5,23,27,1,21,79,85,78,79,85,71,38,10,71,27,12,2,79,6,2,8,13,9,1,13,9,8,68,19,7,1,71,56,11,21,11,68,6,3,22,2,14,0,30,79,1,31,6,23,19,10,0,73,79,44,2,79,19,6,28,68,16,6,16,15,79,35,8,11,72,71,14,10,3,79,12,2,79,19,6,28,68,32,0,0,73,79,86,71,39,1,71,24,5,20,79,13,9,79,16,15,10,68,5,10,3,14,1,10,14,1,3,71,24,13,19,7,68,32,0,0,73,79,87,71,39,1,71,12,22,2,14,16,2,11,68,2,25,1,21,22,16,15,6,10,0,79,16,15,10,22,2,79,13,20,65,68,41,0,16,15,6,10,0,79,1,31,6,23,19,28,68,19,7,5,19,79,12,2,79,0,14,11,10,64,27,68,10,14,15,2,65,68,83,79,40,14,9,1,71,6,16,20,10,8,1,79,19,6,28,68,14,1,68,15,6,9,75,79,5,9,11,68,19,7,13,20,79,8,14,9,1,71,8,13,17,10,23,71,3,13,0,7,16,71,27,11,71,10,18,2,29,29,8,1,1,73,79,81,71,59,12,2,79,8,14,8,12,19,79,23,15,6,10,2,28,68,19,7,22,8,26,3,15,79,16,15,10,68,3,14,22,12,1,1,20,28,72,71,14,10,3,79,16,15,10,68,3,14,22,12,1,1,20,28,68,4,14,10,71,1,1,17,10,22,71,10,28,19,6,10,0,26,13,20,7,68,14,27,74,71,89,68,32,0,0,71,28,1,9,27,68,45,0,12,9,79,16,15,10,68,37,14,20,19,6,23,19,79,83,71,27,11,71,27,1,11,3,68,2,25,1,21,22,11,9,10,68,6,13,11,18,27,68,19,7,1,71,3,13,0,7,16,71,28,11,71,27,12,6,27,68,2,25,1,21,22,11,9,10,68,10,6,3,15,27,68,5,10,8,14,10,18,2,79,6,2,12,5,18,28,1,71,0,2,71,7,13,20,79,16,2,28,16,14,2,11,9,22,74,71,87,68,45,0,12,9,79,12,14,2,23,2,3,2,71,24,5,20,79,10,8,27,68,19,7,1,71,3,13,0,7,16,92,79,12,2,79,19,6,28,68,8,1,8,30,79,5,71,24,13,19,1,1,20,28,68,19,0,68,19,7,1,71,3,13,0,7,16,73,79,93,71,59,12,2,79,11,9,10,68,16,7,11,71,6,23,71,27,12,2,79,16,21,26,1,71,3,13,0,7,16,75,79,19,15,0,68,0,6,18,2,28,68,11,6,3,15,27,68,19,0,68,2,25,1,21,22,11,9,10,72,71,24,5,20,79,3,8,6,10,0,79,16,8,79,7,8,2,1,71,6,10,19,0,68,19,7,1,71,24,11,21,3,0,73,79,85,87,79,38,18,27,68,6,3,16,15,0,17,0,7,68,19,7,1,71,24,11,21,3,0,71,24,5,20,79,9,6,11,1,71,27,12,21,0,17,0,7,68,15,6,9,75,79,16,15,10,68,16,0,22,11,11,68,3,6,0,9,72,16,71,29,1,4,0,3,9,6,30,2,79,12,14,2,68,16,7,1,9,79,12,2,79,7,6,2,1,73,79,85,86,79,33,17,10,10,71,6,10,71,7,13,20,79,11,16,1,68,11,14,10,3,79,5,9,11,68,6,2,11,9,8,68,15,6,23,71,0,19,9,79,20,2,0,20,11,10,72,71,7,1,71,24,5,20,79,10,8,27,68,6,12,7,2,31,16,2,11,74,71,94,86,71,45,17,19,79,16,8,79,5,11,3,68,16,7,11,71,13,1,11,6,1,17,10,0,71,7,13,10,79,5,9,11,68,6,12,7,2,31,16,2,11,68,15,6,9,75,79,12,2,79,3,6,25,1,71,27,12,2,79,22,14,8,12,19,79,16,8,79,6,2,12,11,10,10,68,4,7,13,11,11,22,2,1,68,8,9,68,32,0,0,73,79,85,84,79,48,15,10,29,71,14,22,2,79,22,2,13,11,21,1,69,71,59,12,14,28,68,14,28,68,9,0,16,71,14,68,23,7,29,20,6,7,6,3,68,5,6,22,19,7,68,21,10,23,18,3,16,14,1,3,71,9,22,8,2,68,15,26,9,6,1,68,23,14,23,20,6,11,9,79,11,21,79,20,11,14,10,75,79,16,15,6,23,71,29,1,5,6,22,19,7,68,4,0,9,2,28,68,1,29,11,10,79,35,8,11,74,86,91,68,52,0,68,19,7,1,71,56,11,21,11,68,5,10,7,6,2,1,71,7,17,10,14,10,71,14,10,3,79,8,14,25,1,3,79,12,2,29,1,71,0,10,71,10,5,21,27,12,71,14,9,8,1,3,71,26,23,73,79,44,2,79,19,6,28,68,1,26,8,11,79,11,1,79,17,9,9,5,14,3,13,9,8,68,11,0,18,2,79,5,9,11,68,1,14,13,19,7,2,18,3,10,2,28,23,73,79,37,9,11,68,16,10,68,15,14,18,2,79,23,2,10,10,71,7,13,20,79,3,11,0,22,30,67,68,19,7,1,71,8,8,8,29,29,71,0,2,71,27,12,2,79,11,9,3,29,71,60,11,9,79,11,1,79,16,15,10,68,33,14,16,15,10,22,73];
#     most_freq = [];
#     for key_idx in [0, 1, 2]:
#         distrib = {};
#         i = key_idx;
#         while i < len(cipher):
#             c = cipher[i];
#             if c in distrib.keys():
#                 distrib[c] += 1;
#             else:
#                 distrib[c] = 1;
#             i += 3;
#         most_freq.append(keywithmaxval(distrib));
#     key = [n ^ 32 for n in most_freq]; # XOR with whitespace
#     plain = [];
#     for i in range(0,len(cipher)):
#         if i%3==0:
#             plain.append(cipher[i] ^ key[0]);
#         if i%3==1:
#             plain.append(cipher[i] ^ key[1]);
#         if i%3==2:
#             plain.append(cipher[i] ^ key[2]);
#     print(''.join([chr(n) for n in plain]))
#     return sum(plain);
# 
# print(pe59());
# 
# 
# def pe57():
#     count = 0;
#     last = Fraction(3,2);
#     for n in range(2,1000):
#         f = 1+1/(1+last);
#         last = f;
#         if len(str(f.numerator)) > len(str(f.denominator)):
#             count += 1;
#     return count; 
# 
# 
# print(pe57());
# 

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

# def pe58():
#     e = 3;
#     n = 5;
#     primes = [3, 5, 7];
#     ratio = len(primes)/n;
#     while ratio >= 0.1:
#         e += 2;
#         t = e**2;
#         next_step = [t-3*(e-1), t-2*(e-1), t-(e-1), t];
#         n += 4;
#         primes += [n for n in next_step if is_prime(n)];
#         ratio = len(primes)/n;
#         # print('Edge: %d    Ratio: %f' %(e,ratio));
#     return e;
# 
# print(pe58());
# 
# 
# def pe52():
#     n = 1;
#     res = Counter(str(n)) == Counter(str(2*n)) == Counter(str(3*n)) == Counter(str(4*n)) == Counter(str(5*n)) == Counter(str(6*n));
#     while res == False:
#         n += 1;
#         res = Counter(str(n)) == Counter(str(2*n)) == Counter(str(3*n)) == Counter(str(4*n)) == Counter(str(5*n)) == Counter(str(6*n));
#     return n;
# 
# print(pe52());


def bino(n, k):
    if k == 0:
        return 1;
    res = n-k+1;
    for i in range(2,k+1):
        res *= (n-k+i);
        res //= i;
    return res;
 
# def pe53():
#     res = 4;
#     k = 10;
#     for n in range(24,101):
#         tmp = bino(n,k);
#         while tmp > 1000000:
#             k -= 1;
#             tmp = bino(n,k);
#             
#         t = n+1-(k+1)*2;
#         res += t;
#     return res;
# 
# print (pe53());
# 
# def pe56():
#     res = 0;
#     for a in range(1,100):
#         for b in range(1,100):
#             tmp = a**b
#             tmp = sum([int(c) for c in str(tmp)]);
#             if tmp > res:
#                 res = tmp;
#     return res;
# 
# print(pe56());    
# 
# 
# def brent(N):
#     if N%2==0:
#         return 2
#     y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
#     g,r,q = 1,1,1
#     while g==1:            
#         x = y
#         for i in range(r):
#             y = ((y*y)%N+c)%N
#         k = 0
#         while (k<r and g==1):
#             ys = y
#             for i in range(min(m,r-k)):
#                 y = ((y*y)%N+c)%N
#                 q = q*(abs(x-y))%N
#             g = gcd(q,N)
#             k = k + m
#         r = r*2
#     if g==N:
#         while True:
#             ys = ((ys*ys)%N+c)%N
#             g = gcd(abs(x-ys),N)
#             if g>1:
#                 break
#          
#     return g;
# 
# 
# def primefac(N):
#     d = {};
#     tmp = N;
#     while tmp != 1:
#         if is_prime(tmp):
#             if tmp in d.keys():
#                 d[tmp] += 1;
#             else:
#                 d[tmp] = 1;
#             tmp //= tmp;
#         else:
#             f = brent(tmp);
#             if f != tmp and is_prime(f):
#                 if f in d.keys():
#                     d[f] += 1;
#                 else:
#                     d[f] =  1;
#                 tmp //= f;
#     return d;
# 
# def totient(N):
#     d = primefac(N);
#     res = 1;
#     for fac in d.keys():
#         if d[fac] == 1:
#             tmp = fac-1;
#         else:
#             tmp = fac**d[fac]-fac**(d[fac]-1)
#         res *= tmp;
#     return res;
# 
# def pe69():
#     m = 0;
#     res = 0;
#     for n in range(500000,1000000):
#         phi = totient(n);
#         tmp = n/phi;
#         if tmp > m:
#             m = tmp;
#             res = n;
#     print(m);
#     return res;
# 
# pe = pe69();
# print(pe);
# print(primefac(pe), totient(pe))


def cardvalue(c):
    char_value = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    if c.isdigit():
        return int(c);
    else:
        return char_value[c];

def p1wins(hand1result, hand2result):
    result_value = {
        'high': 0,
        'pair': 1,
        '2pair': 2,
        'three': 3,
        'straight': 4,
        'flush': 5,
        'full_house': 6,
        'four': 7,
        'straigt_flush': 8,
        'royal_flush': 9,
    }
    result1 = result_value[hand1result[0][0]];
    result2 = result_value[hand2result[0][0]];    
    if result1 > result2:
        return True;
    elif result1 == result2 and hand1result[0][1] > hand2result[0][1]:
        return True;
    elif result2 > result1:
        return False;
    elif result1 == result2 and hand2result[0][1] > hand1result[0][1]:
        return False;
    else:        
        high1 = high2 = 0;
        i = 0;
        while high1 == high2:
            high1 = hand1result[1][i];
            high2 = hand2result[1][i];
            if high1 > high2:
                return True;
            if high2 > high1:
                return False;
            i += 1;

def get_result(hand):
    vals = [cardvalue(c[0]) for c in hand];
    colors = [c[1] for c in hand];
    val_dict = {i: vals.count(i) for i in set(vals)}
    order = sorted(vals, reverse=True);
    max_key = keywithmaxval(val_dict);
    
    
    straight = len(val_dict) == 5 and (max(vals)-min(vals) == 4 or set(vals) == set([14,2,3,4,5]));
    flush = len(set(colors)) == 1;
    max_val = val_dict[max_key];
    tmp = val_dict;
    tmp.pop(max_key);
    max_key2 = keywithmaxval(tmp);
    max_val2 = tmp[max_key2];
    
    # straight/royal flush
    if straight and flush:
        return (('straight_flush',max(vals)), order);
    # four of a kind
    if max_val == 4:
        return (('four', max_key), order);
    
    # full house 
    if max_val == 3:
        if max_val2 == 2:
            return (('full_house', max_key), order);
    
    if flush:
        return (('flush', max(vals)), order);
    
    if straight:
        return (('straight', max(vals)), order);
    
    # three of a kind
    if max_val == 3:
        return (('three', max_key), order);
    
    # two pair / pair
    if max_val == 2:
        if max_val2 == 2:
            v = max(max_key, max_key2) * 10 + min(max_key, max_key2);
            return (('2pair', v), order);
        else:
            return (('pair', max_key), order);
        
    return (('high', max(vals)), order);
    
    
    
            
def pe54():
    f = open('C:\\Users\\Gesteb-Keller\\Downloads\\poker.txt');
    lines = [hand.split() for hand in [line.strip() for line in f]];
    f.close();
    wins = 0;
    for line in lines:
        h1 = line[0:5];
        h2 = line[5:10];
        r1 = get_result(h1);
        r2 = get_result(h2);
        win = p1wins(r1,r2);
        if win:
            wins += 1;
            
#         # DEBUG
#         r = 'straight';
#         if r1[0][0] == r or r2[0][0] == r:
#             s = win and 'Won:' or 'Lost:';
#             print(h1, h2);
#             print('%s %s with %d vs. %s with %d' % (s, r1[0][0], r1[0][1], r2[0][0], r2[0][1]))

    return wins;

print(pe54());


def pe99():
    f = open('C:\\Users\\Gesteb-Keller\\Downloads\\base_exp.txt');
    lines = [l.split(',') for l in [line.strip() for line in f]];
    l = [math.log(int(l[0]), 10)*int(l[1]) for l in lines];
    return l.index(max(l));

print(pe99());


# def pe62():
#     d_list = [];
#     for b in range(0,10000):
#         cube = b**3;
#         l = [c for c in str(cube)];
#         key_d = {i: l.count(i) for i in set(l)};
#         d_list.append(key_d);
#         if d_list.count(key_d) == 5:
#             return d_list.index(key_d);
# 
# print(pe62());


def pe76():
    for i in reversed(range(1,100)):
        100 - i;
    return 0;
        
        
        
        
        
        
        
        
        

