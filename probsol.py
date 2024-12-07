from sympy import *
from random import *
from math import *


class ProbSol:
    def __init__(self, prob, sol,prompt=""):
        self.prompt = prompt
        self.prob = prob
        self.sol = sol
        self.latex = "\\begin{question}\n" + str(prompt) + "\n" + mathDisp(self.prob) +"\n\\end{question}\n\\begin{solution}\n" + mathDisp(self.sol) + "\n\\end{solution}"
    


def mathDisp(mathExp):
    texExp = latex(mathExp)
    return("\\[\n\t" +texExp + "\n\\]")

def randArray(size, lower = -5, upper = 5):
    rArray = []
    for i in range(size):
        rArray.append(randint(lower, upper))
    return(rArray)

