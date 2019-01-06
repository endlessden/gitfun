def f(a):
	a = 99
	return a


b = 88
print(f(b))  # 函数的作用域关系在定义时就已经固定了 name space &scope


def deco(func):
	def wrapper():
		print('i\'am a deco function')
		res = func()
		print('decorator is over')

	return wrapper

#被装饰的函数作为参数传入
@deco
def normal():
	print('normal function')


normal()

a, b, *rest = range(5)
print(a, b, rest)

l = [1, [2], [3], 4, 5] * 3
l[1][0] = 0
print(l)


def factorial(n):
	""" return n!"""
	return 1 if n < 2 else n * factorial(n - 1)


f = factorial(10)

print(f)


def document_it(func):
	def new_func(*args, **kwargs):
		print('running function:', func.__name__)
		print('positional arguments:', args)
		print('keyword arguments:', kwargs)
		result = func(*args, **kwargs)
		print('result:', result)
		return result
	return new_func


def square_it(func):
	def new_function(*args, **kwargs):
		result = func(*args, **kwargs)
		print('square:', result * result)
		return result * result
	return new_function


@square_it
@document_it
def add_int(a, b):
	return a + b


add_int(3, 5)

import time

current_user = {'user': None}


# def auth(engine='file'):
# 	def deco(func):
# 		def wrapper(*args, **kwargs):
# 			if current_user['user']:
# 				# 已经登陆过
# 				res = func(*args, **kwargs)
# 				return res
# 			user = input('username>>: ').strip()
# 			pwd = input('password>>: ').strip()
# 			if engine == 'file':
# 				# 基于文件的认证
# 				if user == 'egon' and pwd == '123':
# 					print('login successful')
# 					# 记录用户登陆状态
# 					current_user['user'] = user
# 					res = func(*args, **kwargs)
# 					return res
# 				else:
# 					print('user or password error')
# 			elif engine == 'mysql':
# 				print('基于mysql的认证')
# 			elif engine == 'ldap':
# 				print('基于ldap的认证')
# 			else:
# 				print('无法识别认证来源')

# 		return wrapper

# 	return deco


# @auth(engine='mysql')  # @deco #index=deco(index) #index=wrapper
# def index():
# 	print('welcome to index page')
# 	time.sleep(1)


# @auth(engine='mysql')
# def home(name):
# 	print('welecome %s to home page' % name)
# 	time.sleep(0.5)


# index()
# home('egon')

"""装饰器使函数调用变慢了.一定要记住.

装饰器不能被取消(有些人把装饰器做成可以移除的但是没有人会用)
所以一旦一个函数被装饰了.所有的代码都会被装饰.

Python自身提供了几个装饰器,像property, staticmethod.

Django用装饰器管理缓存和视图的权限.

Twisted用来修改异步函数的调用."""


def decorator(**kwargs):
	def add(obj):
#执行顺序:1.运行Decorator函数，先打印外部的传入的参数，返回add函数名；
# 2.再执行School = add(School)
		for k, v in kwargs.items():
			setattr(obj, k, v)
		return obj
	return add



@decorator()
class School():
    def __init__(self,price):
        self.price =price

#price 装饰成为类属性
@decorator(addr = "湖北省",price =12000)
class School1():
    pass

middleschool = School1()
middleschool2 = School1()
print(School.__dict__)
print(School1.__dict__)
print(middleschool.price)
print(middleschool2.price)






class Myproperty():
    def __init__(self,fun):
        # print("执行Myproperty类的构造方法")   #调用Myproperty类时会首先运行它
        self.fun = fun
    def __get__(self, instance, owner):
        """
        :param instance: 代表school实例本身
        :param owner:  代表类School本身
        :return:
        """
        # print('调用Myproperty的属性时将执行此方法')
        return  self.fun(instance)



class School():
    """
    @name:学校名字
    @addr:学校地址
    @price:学费
    @num:招生人数
    """
    def __init__(self,name,addr,price,num):
        self.name =name
        self.addr =addr
        self.price =price
        self.num =num
    # @property
    @Myproperty    #等价于-->>total=Myproperty(total)
    def total(self):
        "求总的学费"
        return  self.price*self.num

school = School('浙江大学','浙江省杭州市',12000,6000)
print(school.total)



