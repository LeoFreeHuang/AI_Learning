import sympy 
from sympy import oo

x = sympy.Symbol('x')
f = sympy.sin(x) / x
result = sympy.limit(f, x, oo)
print(result)

x1 = sympy.Symbol('x')
f1 = (x1 ** 2 - 1)/(x1 - 1)
result1 = sympy.limit(f1, x1, 1)
print(result1) 

x2 = sympy.Symbol('x')
f2 = (x2**(1/3) - 2) / (x2 - 8)
f2_limit_res = sympy.limit(f2, x2, 8)
print(f2_limit_res)