from random import randint 

correct = 0
qcnt=int(input('How many questions?'))

for i in range(qcnt):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    prod = n1 * n2
    
    ans = input("What's %d times %d? " % (n1, n2))
    if int(ans) == prod:
        print ("That's right -- well done.\n")
        correct = correct + 1
    else:
        print ("No, I'm afraid the answer is %d.\n" % prod)

print ("\nI asked you %d questions.  You got %d of them right." % (qcnt, correct))
print ("Well done!")