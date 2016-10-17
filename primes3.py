from sympy.ntheory import factorint

import time
import random

from primes1 import is_prime

from primes1 import primes_up_to

prime_digits = [n for n in primes_up_to(10) if (len(str(n)) == 1)]

random.seed(int(time.time()))
num = 0
while (num < 1000):
    n = int(''.join(['%d'%(random.choice(prime_digits)) for n in xrange(5)]))
    
    f = factorint(n)
    
    print f
    
    __not__ = False
    for k,v in f.iteritems():
        __is__ = is_prime(k)
        if (not __is__):
            print 'WARNING: %s is not prime.' % (k)
            __not__ = True
            break

    if (__not__):
        print 'ERROR: Test failed.'
        break
    num += 1

if (__not__):
    print 'ERROR: Test failed.'
else:
    print 'INFO: Test successful.'
