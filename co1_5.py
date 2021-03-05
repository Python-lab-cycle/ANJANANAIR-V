list=[10,200,30,40,150,60]
result=[]
for i in list:
    if i>100:
       result.append('over')
    else:
        result.append(i)
print(result)
