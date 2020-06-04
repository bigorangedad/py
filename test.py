"""
a = 1
if a == 0:
    print("a=0")
else:
    print("a!=0")
"""
"""
计算出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
#
# computer_number = random.randint(1,13)
# while True:
#     person_number = int(input("请输入一个数"))
#
#     if person_number>computer_number:
#         print("小一点")
#     elif person_number<computer_number:
#         print("大一点")
#     elif person_number==computer_number:
#         print("猜对啦")
#         break
#
# def func(a):
#     print(a)
#     return 0
#
# print(func(1))

# def method(a,b):
#     """
#     :param a:
#     :return:
#     """
#     print(a)
#     print(b)
#
# print(method(1,3))

#
# def method(*a):
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#     print(a[4])
#
#
# method("a", "b", "c","d", "e")

a=(1,2,3,4)

#print(a[0])


# 函数传参
# #仅限关键字传参，在关键字前加 *,
# #例如：
# def method(*,a):
#     print(a)
#
#     """
#
#     :param a:
#     :return:
#     """
#     return 0
#
# print(method(a=1))这里只能使用 a=1传参，不能直接传参1



# #解包：
# 元组，列表解包
# print(list(range(3,6)))
#
# list_a = (3,6) 元组或列表都可以
# list(range(*list_a))
# 这里要加*解包才行

# #字典解包
# def method(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#
# dic1 = {"a":1,"b":2,"c":3}
# #字典对象
#
# method(**dic1)
# #经过**解包字典对象后，"a":1 -> a=1

##lambda表达式：
# 可以用来创建一个小的匿名函数，lambda主体是一个表达式，自带return功能，仅能封装简短的有限的逻辑进去
# y = lambda x:x*2
# 用法 lambda a:
# print(y(2))