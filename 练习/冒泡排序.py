
# _*_ coding:utf-8 _*_
# @time:2020/11/9 000921:18
# @Author:csw
# import  random
# def get_random(num):
#     a=[]
#     i=0
#     while i<num:
#         a.append(random.randint(0,100))
#         i+=1
#     print(a)
#
# if __name__=='__main__':
#     get_random(10)

# num_list=[3,7,6,11,8,1,10,2]
# lengh=len(num_list)
# # print(type(lengh))
# for i in range(lengh): #range有多少值就做多少循环操作、每次循环操作的值可以选择i、那么i的值就是随时变化的
#     count_swap=0
#     for j in range(lengh-i-1):
#         if num_list[j]>num_list[j+1]:
#             num_list[j],num_list[j+1]=num_list[j+1],num_list[j]
#             count_swap+=1
#     if count_swap==0:
#         break
# print(num_list)

import  random

def random_list(a):
    sum=0
    b=[]
    while sum<10:
        b.append(random.randint(0,a))
        sum+=1
    # print(b)
    return b   #此函数的值想被其他函数调用、需要return返回

def bubble_sort(a):
    li=random_list(a)
    for i in range(len(li)):
        c = 0
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                c+=1
        if c==0:
            break
    print(li)
#
if __name__=='__main__':
    # random_list(int(input('请输入第一个值；')))
    bubble_sort(int(input('请输入列表范围:')))


