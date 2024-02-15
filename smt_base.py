#https://ericpony.github.io/z3py-tutorial/guide-examples.htm
from z3 import *
#variable
x = Int('x')
y = Int('y')
#solveur
s = Solver()
solve(x > 0,y > 0)
#ajout de contraintes 
s.add(x > 0) 
s.add(y > 0) 
s.add(x+y == 10)  
if s.check() == sat :
    print (s.check())
    m = s.model()
    print(m)
    print("x =", m[x])
    print("y =", m[y])
else:
    print("Insatisfiable")