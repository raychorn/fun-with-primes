# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

from math import sqrt
from itertools import ifilter

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True
    
def primes_up_to(n):
    """Generates all primes less than n."""
    if n <= 2: return
    yield 2
    F = [True] * n
    seq1 = xrange(3, int(sqrt(n)) + 1, 2)
    seq2 = xrange(seq1[-1] + 2, n, 2)
    for p in ifilter(F.__getitem__, seq1):
        yield p
        for q in xrange(p * p, n, 2 * p):
            F[q] = False
    for p in ifilter(F.__getitem__, seq2):
        yield p
        
if (__name__ == '__main__'):
    p = 10000
    p = primes_up_to(p)
    try:
        for i in xrange(0,10000):
            n = p.next()
            if (is_prime(n)):
                print n
            else:
                print 'ERROR: Failed to generate a valid prime number.'
                break
    except Exception, details:
        print 'Stopped due to exception: %s.' % (details)
        
    
