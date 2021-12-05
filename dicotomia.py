a= float(input("inicio: "))
b= float(input("Fim"))

preci=4
def funcao (x):

    f= (x**2)+(1.95*x)-2.09
    return f
fc=1
count=1
#ficar a tento ao numero de zeros
while fc!=0.0000:

    c= ((a+b)/2)
    fa=round(funcao(a), preci)
    fb=round(funcao(b), preci)
    fc=round(funcao(c), preci)
    print(count,a,fa,b,fb,c,fc)
    if fc<0:
        a=c
    else:
        b=c
    count=count+1

    if count>50:
        break