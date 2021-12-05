from sympy import diff, var
x0= float(input("x0: "))
x,y,z= var('x y z')

#arre=3
def funcao(x):
    func=((x-3)**3)-((x+2)**2)
    return func

def derivada():
    func=((x-3)**3)-((x+2)**2)
    deri=diff(func,(x))
    return deri
count=0
while 0==0:
    f=funcao(x0)
    fderi=derivada()
    fd= fderi.subs({
        x: x0
    })
    fdr=fd
    x1= x0-(f/fdr)

    print(count,x0, f, fdr, x1)
    if x1==x0:
        break
    x0=x1
    count=count+1
    if count>50:
        break





