'''
通过列表生成式(列表推导式)，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

得到生成器方式：
1.通过列表推导式得到生成器


'''

# [x for x in range(10000000000)]

# [0,3,6,9,12,15,18,21,...27]

# newlist = [x*3 for x in range(20)]
# print(type(newlist))

# 得到生成器
g = (x*3 for x in range(10))
print(type(g))  # generator
print(g)

# 方式1：通过调用__next__() 方式得到元素
print(g.__next__())  # 0
print(g.__next__())  # 3
print(g.__next__())  # 6
print(g.__next__())  # 9

# 方式2： next(生成器对象)  builtins 系统内置函数
# 每调用一次next则会产生一个元素
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # StopIteration  生成器本来就可以产生10个，得到了10个。在调用next(g) 抛出异常



# g = (x * 3 for x in range(10))
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('没有更多元素啦！')
#         break


# 定义生成器的方式二:借助函数完成
# 只要函数中出现了yield关键字，说明函数就不是函数啦，变成生成器啦
# 菲波那切数列
'''
步骤：
1. 定义一个函数，函数中使用yield关键字
2. 调用函数，接收调用的结果
3. 得到的结果就是生成器
4. 借助于next() ,__next__()得到元素

'''


# def func():
#     n = 0
#     while True:
#         n += 1
#         # print(n)
#         yield n  # return n  + 暂停
#
#
# g = func()
# print(g)


# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 0,1,1,2,3,5,8
def fib(length):
    a, b = 0, 1
    n = 0

    while n < length:
        # print(b)
        yield b  # return b + 暂停
        a, b = b, a + b
        n += 1

    return '没有更多元素！！！'  # return就是在得到StopIteration后提示信息


g = fib(8)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
