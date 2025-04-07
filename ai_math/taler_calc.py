import sympy as sy

x = sy.Symbol('x')
f = (sy.sin(x)-x*sy.cos(x))/pow(sy.sin(x), 3)
limit_res = sy.limit(f, x, 0)
print(limit_res)