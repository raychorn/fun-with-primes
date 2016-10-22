from sympy.ntheory import factorint

import time
import random

from primes1 import is_prime

from primes1 import primes_up_to

prime_digits0 = [n for n in primes_up_to(100) if (len(str(n)) == 2)]

prime_digits = prime_digits0 * 10

random.shuffle(prime_digits)

__dict__ = {}

random.seed(int(time.time()))
num = 0
while (num < 100):
    n = int(''.join(['%d'%(random.choice(prime_digits)) for n in xrange(4)]))
    
    if (__dict__.has_key(n)):
        num -= 1
        print '%s has repeated.' % (n)
        continue
    
    f = factorint(n)
    
    __dict__[n] = f
    
    print '%s ==> %s' % (n, f)
    
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
