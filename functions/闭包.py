# encoding:utf-8
import math
def func(a,b):
	def deco(func):
		def test(x):
			print((a+b)*x)
			res = func()
			return res
		return test
	return deco


@func(3,5)
def func2():
	print('sada')

#定义： 如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包

#func2需要和闭包传相同的参数
func2(8)

def test1(a):
	print(a)
	def test2(b):
		print(a,b)
	return test2


test1('closure')('function')


#无参装饰器，被装饰的函数作为装饰器的参数传入，有参装饰器需要在包一层(func中间层传入)
def decorator(a,b):
	def deco(func):
		def wrapper(*arg,**kwargs): #如果被装饰的函数有参数，就通过wrapper闭包传入
			print(111)
			print(222)
			res =func(*arg,**kwargs)
			print(444)
			print(a*b)
			return res
		return wrapper
	return deco


@decorator(2,3)
def count(x,y):
	print(x,y)

count(333,'jumbo')

"""
python装饰器经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计，有了装饰器，
我们就可以从大量函数中抽离出与函数功能本身无关的雷同代码并继续重用。概括的讲，
装饰器的作用就是为已经存在的对象添加额外的功能。AOP 面向切面编程
"""

class Circle:
	def __init__(self,radius):
		self.__radius = radius
		self.parameter = 2*(math.pi*radius)
		self.square = math.pi*(radius**2)


round1 = Circle(3)
print(round1.square)






def decos(func):
	def wrapper(*args,**kwargs):
		print('i am the wrapper')
		res = func(*args,**kwargs)
		print('wrapper done')
		return res
	return wrapper

@decos
def wrapped(a,b):
	print(a,b)
	print('the lindenburg')


wrapped(34, b='qq')





def test1(a,b):
	print(a,b)


test1(1,b=5)


accounts = {'rate':999}

accounts.setdefault('rate',5)
print(accounts.get('rate'))
print(accounts.get('name','default'))


import requests
def outter(url):
	def get():
		res = requests.get(url)
		return res.text
	return get


new_get = outter('https://baidu.com')

print(new_get()) #固定住了url



def outside(a):
	def get():
		print(a)
	return get


outside(5)()

try:
	print(f'the functions is multiple ranges {10}')
except EOFError:
	raise AttributeError('the function is there is not right')
except AssertionError as e:
	print(e)
else:
	print('run this code if there is no error')
finally:
	print('try/catch is over')


m = ['asd','jackson',[123]]
print(m[2][-1])

mm = [('first',2),('two',4),('three',6)]
dict_mm = dict(mm)
keys= dict_mm.keys() #返回key的迭代形式
print(keys)
for key in keys:
	print(key)


print('it\'s my life')

