from fractions import Fraction
import numpy as np

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def solution(rr):
    NO_OF_ITERATIONS = 500
    MAX_FRACTION_DENOMINATOR = 1000
    
    isTerminal = []
    lcm = 1
    out = []

    for rindex,r in enumerate(rr):
        s = sum(r)
        if s != 0:
            isTerminal.append(0)
            for i in range(len(r)):
                r[i] = float(r[i])/s
        else:
            r[rindex] = 1
            isTerminal.append(1)

    A = np.array(rr[0])
    B = np.array(rr)

    for i in range(NO_OF_ITERATIONS):
        A = A.dot(B)

    for i,ele in enumerate(A):
        frac = Fraction(A[i]).limit_denominator(MAX_FRACTION_DENOMINATOR)
        lcm = compute_lcm(lcm,frac.denominator)
        A[i] = frac

    for i,terminal in enumerate(isTerminal):
        if terminal:
            out.append(int(round(float(A[i]*lcm))))
    
    out.append(lcm)
    return out

# print(solution([[0, 2, 1, 0, 0],[0, 0, 0, 3, 4],[0, 0, 0, 0, 0],[0, 0, 0, 0,0],[0, 0, 0, 0, 0]]))