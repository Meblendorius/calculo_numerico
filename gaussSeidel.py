# Método Iterativo de Gauss-Seidel para resolver Sistemas
#verificar onde o delta fica maluco
# 
from numpy import round_, sqrt, around


def maxValue(a, b, c, eq1, eq2, eq3):
  delta = sqrt(
    ((eq1 - a)**2) + ((eq2 - b)**2) + ((eq3 - c)**2)
  )
  roundDelta = round(delta,5)
  
  #print(roundDelta)
  
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

while deltaK != 0.0000:
  eq1 = round(functionOne(y, z),5)
  eq2 = round((functionTwo(x, z)),5)
  eq3 = round((functionThree(x, y)),5)
  
  deltaK = maxValue(x, y, z, eq1, eq2, eq3)
  print("{}|X={} | Y={} | Z={} | x1={} | y1={}| z1={} | delta={}".format(i, x, y, z, eq1, eq2, eq3, deltaK))

  x = eq1
  y = eq2
  z = eq3
  i = i + 1

