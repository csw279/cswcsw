# _*_ coding:utf-8 _*_
# @time:2020/11/9 000923:42
# @Author:csw
####奇数之和
# a=0
# for i in range(10):
#     if i %2==0:
#         a+=i
#         print(a)
# print(a)
import  random
a=0
b=random.randint(0,100)
for i in range(b):
    if i % 2 == 0:
        a+=i
        print(i)
        print(a)
print(a)