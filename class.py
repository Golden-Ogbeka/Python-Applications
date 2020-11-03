def calc(z):#z is called parameter or argument
    calcValue=0
    Value1=0
    Value2=0
    for i in range(0,len(z)):
        Value1=Value1+z[i]
        Value2=Value2+(z[i]-2)
    calcValue=Value1/Value2

    return calcValue
a=[2,4,5,6,7,8]
print(calc(a))
