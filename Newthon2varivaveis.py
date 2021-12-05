
precisao = 0.01


def F(x, y):
    f=  (3*(x**2))-5-y
    return f


def G(x, y):
    g = (2*(x**3))+8-y
    return g


def Fx(x, y):
    fx = 6*x
    return fx


def Gx(x, y):
    gx = (6*(x**2))
    return gx


def Fy(x, y):
    fy = -1
    return fy


def Gy(x, y):
    gy = -1
    return gy


x = float(input("Digite o valor inicial de (x0): "))
y = float(input("Digite o valor inicial de (y0): "))

x_anterior = x + 2 * precisao
y_anterior = y + 2 * precisao

while ((abs(x - x_anterior) > precisao) or (abs(y - y_anterior) > precisao)):
    x_anterior = x
    y_anterior = y

    x = x_anterior - (F(x, y) * Gy(x, y) - Fy(x, y) * G(x, y)) / (Fx(x, y) * Gy(x, y) -
                                                                  Fy(x, y) * Gx(x, y))
    y = y_anterior - (Fx(x, y) * G(x, y) - F(x, y) * Gx(x, y)) / (Fx(x, y) * Gy(x, y) -
                                                                  Fy(x, y) * Gx(x, y))

    print("x = ", x, "\ty= ", y)