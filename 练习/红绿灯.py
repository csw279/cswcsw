# _*_ coding:utf-8 _*_
# @time:2020/11/9 000921:18
# @Author:csw


# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print(' ')
import  random

def rad():
    a=[]
    for i in range(10):
        a.append(random.randint(0,100))
    return  a

def bubbom_insert():
    a=rad()
    print(a)
    le=len(a)
    for i in range(le):
        sum=0
        for j in range(le-1-i):
            if a[j] >a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                sum+=1
        if sum==0:
            break
    print(a)
    print('csw')

if __name__=='__main__':
    bubbom_insert()
