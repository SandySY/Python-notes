'''
def printOneLine():
  print("-"*30)

def printNumLine(num):
  i = 0
  while i<num:
    printOneLine()
    i+=1

printNumLine(3)
'''

# f = open("text.txt", "w")
# f=open("text.txt") #默认访问模式 r

# f.write('hello world')

'''
content = f.readlines()

i=1
for temp in content:
    print('%d:%s'%(i,temp))
    i+=1
'''
# print(f.readline())
# print(f.readline())
#
#
# f.close()

import sys
# print(sys.path)
# ['C:\\Work\\my-project\\Python相关的学习和模板项目\\Python\\day',
#  'C:\\Work\\my-project\\Python相关的学习和模板项目\\Python',
#  'C:\\Program Files\\JetBrains\\PyCharm 2020.3.3\\plugins\\python\\helpers\\pycharm_display',
#  'C:\\Software\\Python 3.7.4\\python37.zip', 'C:\\Software\\Python 3.7.4\\DLLs',
#  'C:\\Software\\Python 3.7.4\\lib', 'C:\\Software\\Python 3.7.4',
#  'C:\\Users\\lshfy\\PycharmProjects\\pythonProject\\venv',
#  'C:\\Users\\lshfy\\PycharmProjects\\pythonProject\\venv\\lib\\site-packages',
#  'C:\\Program Files\\JetBrains\\PyCharm 2020.3.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

import datetime
d = datetime.datetime.now()
print(d)
print(d.date())
print(d.time())
print(d+ datetime.timedelta(5))
print(d.replace(year=2120, month=8))

import string
import random
#随机生成字符串密码
a = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))
print(a)
#洗牌
list = [0,1,2,3,45,5,6,7,8,9]
random.shuffle(list)
print(list)