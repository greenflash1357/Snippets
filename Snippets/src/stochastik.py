import random

c = 100;
n = 10000;

res = [0]*(c);

for _ in range(n):
    res[random.randint(0,c-1)] += 1;

mean = sum([res[i]*i for i in range(c)])/n;
var = sum([(res[i]-mean)**2 for i in range(c)])/n;
sigma = var**0.5;
    
print(mean, var, sigma)