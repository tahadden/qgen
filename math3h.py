from probsol import *


x = symbols('x')

def rationalSimp():
    a, b, c = randint(-10,10), randint(-10,10), randint(-10,10)
    f = (x+a)*(x+b)
    g = (x+b)*(x+c)
    rat = expand(f)/expand(g)
    sol = f/g
    probsol = ProbSol(rat, sol, "Simplify the following: ")
    return(probsol)

def rationalAddSub():
    a,b,c,d = randint(-10,10),randint(-10,10),randint(-10,10),randint(-10,10)
    n1 = (x+a)*(x+b)
    d1 = (x+c)*(x+d)

q1 = rationalSimp()
print(q1.latex)
