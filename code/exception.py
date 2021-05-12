# 抛出异常 raise

# 注册 用户名必须6位
def register():
    username = input('输入用户名:')
    if len(username) < 6:
        raise Exception('用户长度必须6位以上')
    else:
        print('输入的用户名是:', username)


try:
    register()
except Exception as err:
    print(err)
    print('注册失败！')
else:
    print('注册成功！')

'''
# 文件操作  stream = open(...)   stream.read()   stream.close()
# 数据库操作  close()
try；
   pass
except:
   pass
finally:
   pass

'''

def func():
    stream = None

    try:
        stream = open(r'c:\p1\aa1.txt')
        container = stream.read()
        print(container)
        stream.close()
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('------finally-----')
        if stream:
            stream.close()
        # return 3


x = func()
print(x)