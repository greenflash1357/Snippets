import timeit
from timeit import timeit as timer
import random
import math


# def cond1():
#     a = random.randint(0,9);
#     b = False;
#     if a < 1:
#         b = True;
#     else:
#         for i in range(1000):
#             b = True;
#     return b;
# 
# def cond2():
#     a = random.randint(0,9);
#     b = False;
#     if a >= 1:
#         b = True;
#     else:
#         for i in range(1000):
#             b = True;        
#     return b;
# 
# 
# def cond3():
#     b = False;
#     if (5**400)**(1/380) > 1:
#         if False:
#             b = True;
#     else:
#             b = True;        
#     return b;
# 
# def cond4():
#     b = False;
#     if False:
#         if (5**400)**(1/380) > 1:
#             b = True;
#     else:
#         b = True;        
#     return b;
# 
# 
# 
# def cond5():
#     b = False;
#     if (5**400)**(1/380) > 1 and False:
#         b = True;
#     else:
#         b = True;        
#     return b;
# 
# def cond6():
#     b = False;
#     if False and (5**400)**(1/380) > 1:
#         b = True;
#     else:
#         b = True;        
#     return b;
# 
# print(timer('cond1()', setup='from __main__ import cond1', number=100000));
# print(timer('cond2()', setup='from __main__ import cond2', number=100000));
# 
# print(timer('cond3()', setup='from __main__ import cond3', number=100000));
# print(timer('cond4()', setup='from __main__ import cond4', number=100000));
# 
# print(timer('cond5()', setup='from __main__ import cond5', number=100000));
# print(timer('cond6()', setup='from __main__ import cond6', number=100000));
# 
# 
# print(timer('256**0.5', setup='from __main__ import math', number=100000));
# print(timer('math.sqrt(256)', setup='from __main__ import math', number=100000));


def _sign(x):
    if x > 0 or (x == 0 and math.atan2(x, -1.) > 0.):
        return 1;
    else:
        return -1;

def sign(x):
    a = str(x)[0];
    return  a == '-' and '-' or '';

#candidates = [1.1,0.0,-0.0,-1.2,2.4,5.6,-8.2,74.1,-23.4,7945.481];
candidates = list(range(-500,500));

print(timer('[_sign(c) for c in candidates]', setup='from __main__ import _sign, candidates', number=1000));
print(timer('[sign(c) for c in candidates]', setup='from __main__ import sign, candidates', number=1000));