#ٍSaif Eldeen Soliman Abdeen Soliman 18102012
from py_expression_eval import Parser
import sympy as sp
import math
parser = Parser() #Parser is the main class of the library that contains the methods to parse, evaluate and simplify mathematical expressions

#pyexperssion eval is a Mathematical Expression Evaluator
#downloaded from github https://github.com/axiacore/py-expression-eval

flag = 0
eqn = input("Please enter the equation: ")

x0 = float(input("Please enter the value of Xo: "))
fOfX = float(parser.parse(eqn).evaluate({'x' : x0}))
fdash = str(sp.diff(eqn))
print("The derivative is ", fdash)
numOfIterations = float(input("Please enter the vnumber of iterations: "))
tol = float(input("Please enter the value of tolerance: "))
#numOfIterations = float(math.log((valOfB-x0)/tol))/float(math.log(2)) 
i=2 #first iteration already made

fOfxDash = float(parser.parse(fdash).evaluate({'x' : x0}))

print("i=1,     Xi=", x0,  "    f(Xi)=", fOfX, "    F(Xi dash)=", fOfxDash, "\n" )
while i <= numOfIterations:
    xNexti = x0 - (fOfX / fOfxDash)
    x0 = xNexti
    fOfX = float(parser.parse(eqn).evaluate({'x' : xNexti}))
    fOfxDash = float(parser.parse(fdash).evaluate({'x' : xNexti}))

    print("i=", i ,"    Xi=",xNexti, "  f(Xi)=", fOfX, "    F(Xi dash)=",fOfxDash, "\n")
    if abs(fOfX) < tol :
        print("The Root is found, Root = " , fOfX)
        break
    flag = 1
    i=i+1
if flag == 0:
    print("Root found , Root = " , fOfX)