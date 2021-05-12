# -*- coding = utf-8 -*-
# @Time : 2021/4/12 10:13
# @Author : Sandy
# @File : magic.py
# @software : PyCharm


# __init__: 类实例化会触发
# __str__: 打印对象会触发
# __call__: 对象()触发, 类也是对象  类(), 类实例化过程中辉调用元类的__call__
# __new__: 在类实例化会触发,它比__init__早
# __del__: del对象,对象回收的时候触发
# __setattr__, __getattr__: 拦截方法,当对象.属性 -->赋值会调用setattr,取值会调用getattr
# __getitem__, __setitem__: ([]拦截)
# __enter__和__exit__ 上下文管理器

class Person:
    def __init__(self, name):
        self.name = name
    def __setitem__(self, key, value):
        setattr(self,key,value)  #反射
    def __getitem__(self, item):
        getattr(self,item)  #反射取值

p = Person('zhangsan')
p.name = 'lisi'
p['name']= 'wangwu'  #不能直接使用需要魔法方法修改
print(p['name'])

dic = {'name': 'zhangsan', 'age':19}
class Mydic(dict):
    pass
