def value1(a,b,c):
    e=(b**2)-(4*a*c)
    f=e**(1/2)
    x=(-b)+f
    y=x/(2*a)
    print("x1 is", y)
def value2(a,b,c):
    e=(b**2)-(4*a*c)
    f=e**(1/2)
    x=(-b)-f
    y=x/(2*a)
    print("x2 is", y)
def result(a,c):
    a(1,-5,6)
    c(1,-5,6)
result(value1,value2)
