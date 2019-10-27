import Arithmetic;
from Arithmetic import *
print("Enter the first number");
x = int(input());
print("Enter the second number");
y = int(input());
print("Sum is",end =" ");
Arithmetic.Add(x,y);
print("Difference is",end =" ");
Arithmetic.Sub(x,y);
print("Product is",end =" ");
Arithmetic.Mult(x,y);
print("Quotient is",end =" ");
Arithmetic.Div(x,y);