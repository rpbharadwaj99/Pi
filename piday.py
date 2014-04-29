import math
from decimal import *
getcontext().prec = 30
denominator = 1
pi=0
iteration=1
while 1:
	if iteration % 2 == 1:
		pi += Decimal(4.0/denominator)
	else:
		pi -= Decimal(4.0/denominator)
	denominator += 2	
	if iteration % 1000 == 1:
		print Decimal(pi)
	iteration += 1
