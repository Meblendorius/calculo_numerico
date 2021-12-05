# Método Iterativo de Gauss-Seidel para resolver Sistemas
#
# 
from numpy import round_, sqrt, around


def maxValue(a, b, c, eq1, eq2, eq3):
  delta = sqrt(
    ((eq1 - a)**2) + ((eq2 - b)**2) + ((eq3 - c)**2)
  )
  roundDelta = around(delta, prec+1)
  
  print(roundDelta)
  
  return roundDelta

deltaK = 1
i = 0
prec = 4
x = float(input("Insira o valor de X: "))
y = float(input("Insira o valor de Y: "))
z = float(input("Insira o valor de Z: "))

def functionOne(y, z):
  xf = (59-(2*y)-(3*z))/9
  
  return xf

def functionTwo(x, z):
  yf = (1-(2*x)+z)/4
  
  return yf

def functionThree(x, y):
  zf = (-(3*x)+(2*y)+67)/15
  
  return zf

while deltaK != 0:
  eq1 = around(functionOne(y, z), prec)
  eq2 = around(functionTwo(x, z), prec)
  eq3 = around(functionThree(x, y), prec)
  
  deltaK = maxValue(x, y, z, eq1, eq2, eq3)
  
  x = eq1
  y = eq2
  z = eq3
  
  i = i+1
  print("X={} | Y={} | Z={} | iterações(k)= {}".format(x, y, z, i))

print("Resultado: X={} | Y={} | Z={} | iterações(k)= {}".format(x, y, z, i))
