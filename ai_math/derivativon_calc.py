from sympy import *
from sympy.abc import x,y

u = 3*(x**2) + y**2
v = 4*x + 2*y
f = u ** v

#(3*x**2 + y**2)**(4*x + 2*y)*(6*x*(4*x + 2*y)/(3*x**2 + y**2) + 4*log(3*x**2 + y**2))
fx = diff(f,x) 
fx_res = fx.evalf(subs={x:1, y:2})
print(fx_res) 
#(3*x**2 + y**2)**(4*x + 2*y)*(2*y*(4*x + 2*y)/(3*x**2 + y**2) + 2*log(3*x**2 + y**2))
fy = diff(f, y)
fy_res = fy.evalf(subs={x:1, y:2})
print(fy_res) 


g = x**4 - 2*x**3 + 5*sin(x) + log(3)
gx = diff(g, x)
print(gx)


#计算函数梯度
h = x**2 + y**2
h_gradient = [diff(h, var) for var in (x, y)]
print(h_gradient)
h_x = diff(h, x).evalf(subs={x: 1, y: 2})
h_y = diff(h, y).evalf(subs={x: 1, y: 2})
h_grand = sqrt(h_x**2 + h_y**2)
print(h_grand)
