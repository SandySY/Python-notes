# from random import random
import random


# def generate_random(max):
#     for i in range(10):
#         ran=random.randint(1,max)
#         print(ran)
#
#
# print(generate_random)
# print(generate_random(8))
#
# print(type(generate_random))
# print(isinstance(generate_random, int))


# def fun(name,sec=10,*args):
#     print(args)
#     print(type(args))
#     print(len(args),'||')
#     for i in args:
#         print(i)
#
#
# fun(1,5,4,5,8,2)


# def func(**kwargs):  #key word arguments
#     print(kwargs)
#     print(type(kwargs))
#     print(isinstance(kwargs, dict))
#
# func(a=1, b=3, c=3)
#
# dict1 = {'a':1, 'b':2}
# func(**dict1)

def fun(a, *args):
    print(a,args)

fun(1,2,[4,5,6])