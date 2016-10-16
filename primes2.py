from sympy.ntheory import factorint

from primes1 import is_prime

#print factorint(10**20+1)

n = 1313

f = factorint(n)

print f

__not__ = False
for k,v in f.iteritems():
    __is__ = is_prime(k)
    if (not __is__):
        print 'WARNING: %s is not prime.' % (k)
        __not__ = True

if (__not__):
    print 'ERROR: Test failed.'
else:
    print 'INFO: Test successful.'