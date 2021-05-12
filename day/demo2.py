#捕获异常
try:
    print('----test--1--')

    f = open('123.txt', 'r')

    print('-----test----2--')

except IOError:
    pass


try:
    print(num)
# except IOError:
#     print("产生错误了")
# except NameError:
#     print("未定义")
# except (IOError, NameError):
#     print("有多种可能异常发生")
# except NameError as result:
#     print("发生错误是：", result)
except Exception as result:
    print("捕获所有异常，任何异常都可以,错误信息是：", result)



import time

try:
    f=open("text.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)

    finally:
        f.close()
except Exception as result:
    print("发生异常")