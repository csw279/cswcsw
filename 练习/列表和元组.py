# _*_ coding:utf-8 _*_
# @time:2020/11/9 000923:12
# @Author:csw
list []
a=[1,2]
列表的特点；
1、有序的、有索引、正倒序
2、可变的、能对列表进行增删改查操作

增；a.append[3]   给列表最后面添加一个值
   a.insert(0索引值,'cc')  将数据添加到指定的索引位置
   a.extend('a')   不会生成新的列表、在原来列表上增加

删；a.remove('csw')   从左到右删除第一个'csw' 元素====如果删除的值不存在就会报错、value error
   a.pop()  直接删除最后一个元素
   a.pop(0索引值)  删除索引值对应的元素
   a.clear()      清空a里所有的元素
   del a[0]       删除索引指定元素
   del a[:3]      切片删除一连串数值

改；a[0]=1   先索引找到该值、再去赋新值
   a[:3]=1,2,3  切片结合索引、再赋值
查；
   a.index('csw')  获取'csw' 的下标
   a.count('csw')  获取'csw' 出现的个数

print(a.reverse())   将列表倒序排列


a=()   tuple  空元组
a=(1,)    如果元组只带一个元素、那么需要带个逗号，否则认定为 int 整数
特点；
1、有序
2、不可变、元素无法改变            其他操作、函数均同列表===当然不能对元组的元素进行操作










