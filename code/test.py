# var = '全局作用域'
# glo = 0
#
# def fun(a, *args, **kwargs):
#     global glo
#     abs = '''局部   作用域'''
#
#     print(args)
#     print(kwargs)
#
#     #访问全局变量
#     print(var)
#     #修改全局变量
#     glo += 1
#     print(glo)
#
#     def inner_fun():
#         nonlocal abs
#         print(abs)
#         abs = '修改外层局部变量'
#         print('修改后{}'.format(abs))
#
#         def inner():
#             print('*'*10)
#
#         return inner
#
#     return inner_fun
#
#
# # fun(1,[4,5],key=1)()
# flag = fun(1,[4,5],key=1)
# flag()()

# 闭包
#
# def decorate(fun):
#     abs = 'dsfgew'
#     print('decorate')
#     def wrapper(*args,**kwargs):
#         print('wrapper',abs, args, kwargs)
#         return fun(*args, **kwargs)
#     return wrapper
#
# # decorate()()
#
# def decorate1(fun):
#     abs = 'dsfgew111'
#     print('decorate1')
#     def wrapper(*args,**kwargs):
#         print('wrapper1',abs, args, kwargs)
#         return fun(*args, **kwargs)
#     return wrapper
#
# @decorate
# @decorate1
# def fun(a=3):
#     print('fun执行了%d' %a)
#
# fun(1)

# def outer(page=1,num=10):
#     print(page,'||',num)
#     def decorate(fun):
#         abs = 'dsfgew'
#         print('decorate')
#         print(page,'||||',num)
#
#         def wrapper(*args, **kwargs):
#             print('wrapper', abs, args, kwargs)
#
#             print(page, '||||||', num)
#             return fun(*args, **kwargs)
#
#         return wrapper
#     return decorate
#
# # decorate()()
#
# def decorate1(fun):
#     abs = 'dsfgew111'
#     print('decorate1')
#     def wrapper(*args,**kwargs):
#         print('wrapper1',abs, args, kwargs)
#         return fun(*args, **kwargs)
#     return wrapper
#
# @decorate1
# @outer(2,15)
# def fun(a=3):
#     print('fun执行了%d' %a)
#
# fun(1)

# list = [1,2,5,8,4,6]
# fun = lambda a,b : a+b
# print(fun(2,3))
# print(max(list,key=lambda x:x*(3)))
import os
import sys

string = '''
学python、
学java
学nodejs
'''

# write(string, '11.text')


# # 推导式
# list = [4, 5, 7, 5, 2]
# print([a + 1 for a in list])
# print({a + 1 for a in list})
# print({k,v for k,v in tuple.items()})

#
# def fun():
#     value = 9
#
#
#     while value<11:
#         o = yield value  # 有暂停功能 需要能暂停的循环函数体
#         print(o, '||', value - 9)
#         if value==10:
#             raise ZeroDivisionError('0000000')
#         value += 1
#     return '异常msg'
#
# f = fun()
# next(f)
# f.send('fefe')
# next(f)
# f.__next__()
# f.__next__()


# class Person:
#     # 构造方法
#     def __init__(self, name):
#         self.name = name
#
#     # 更多展示类的信息，默认只有内存地址
#     # 打印对象名的时候 触发； 一定要有return
#     def __str__(self):
#         return self.name
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#     def __del__(self):
#         pass
#
#     # 开辟空间
#     def __new__(cls, *args, **kwargs):
#         return super(Person, cls).__new__(cls)
#
#     # 类方法中只能访问类属性和类方法，不依赖于对象
#     @classmethod
#     def classfun(cls):
#         pass
#
#     # 使用类名访问类属性和类方法，不依赖于对象
#     @staticmethod
#     def staticfun():
#         pass
#
#     # 普通方法
#     def fun(self,page=1):
#         pass

# print(sys.path)
# print(sys.version)
# print(sys.argv)
# print(sys.argv)

import time
import datetime
# print(time.time())
# print(time.ctime()) #字符串
# print(time.localtime())  #元组 年月日。。。
# t = time.localtime()
# print(time.mktime(t))  #元组 转 时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S',t))  #元组 转 时间戳
# time.sleep(2)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))  #默认当前时间
#
# #回转 时间元组
# print(time.strptime('2019-10-12 16:05:15', '%Y-%m-%d %H:%M:%S'))


# print(datetime.time.hour)
# print(time.localtime().tm_hour)
#
# print(datetime.date.day)
# print(datetime.date(2019,9,9))
# print(datetime.date.today())
# print(datetime.timedelta(weeks=3))
# print(datetime.date.today() + datetime.timedelta(weeks=3))

# import random
#
# ran = random.random()
# print(ran)
# ran = random.randrange(0,10,1)  #不包含10
# print(ran)
#
# print(random.randint(0,10))  #包含10
#
# list= ['fe','ef','er','etew','aw']
# print( random.choice(list))  #随机抽
#
# # 洗牌
# pai= ['红桃A', '方块B', '梅花Q', '黑桃K']
# random.shuffle(pai)
# print(pai)


# # 加密 md5 sha1 sha256
# import hashlib
#
# msg='终于快要学完了，但是还没有项目实践'
# md5 = hashlib.md5(msg.encode('utf-8'))
# print(md5)
# print(md5.hexdigest())
# print(hashlib.sha1(msg.encode('utf-8')).hexdigest())
# print(hashlib.sha256(msg.encode('utf-8')).hexdigest())


# import pillow
#
# import requests
# request = requests.get('http://12306.cn/')
# print(request.text)

import re
# 支持[0-9a-zA-Z]
# msg = 'dfnew'
# pattern = re.compile('n[a-z]{2}$')
# print(pattern.match(msg))
# print(pattern.search(msg))
# print(pattern.search(msg).span())  #span 返回位置
# print(pattern.search(msg).group())  #提取到的内容
# print(pattern.search(msg).groups())
#
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-([0-9]{8})$', phone)
print(result)
print(result.group(1))
print(result.group(2))

msg = '<html>pagetitle</html>'
msg1 = '<h2>h2title</h2>'
print(re.match(r'<[0-9a-zA-Z]+>(\w*)</[0-9a-zA-Z]+>', msg))
print(re.match(r'<[0-9a-zA-Z]+>(\w*)</[0-9a-zA-Z]+>', msg).group(1))
print(re.match(r'<([0-9a-zA-Z]+)>(.*)</\1>$', msg1))
print(re.match(r'<([0-9a-zA-Z]+)>(.*)</\1>$', msg1).group(2))