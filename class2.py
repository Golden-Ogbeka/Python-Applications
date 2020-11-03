def cal(z):
    up =0
    down=0
    sum=0
    for i in range(0,len(z)):
        divide=a[i]/(a[i]-1)
        sum=sum+divide
        
    return sum
a=[2,4,5,6,7,8]
print("The value is ",cal(a))
