def fibonacci(n):
	a, b, counter = 0, 1, 0
	while True:
		if (counter >n):
			return
		yield a
		a, b = b, a + b
		counter += 1
f = fibonacci(10)

print(f)
# print(next(f))     # next 方法获取下一个值

for num in f:                # for循环生成器取值
	print(num, end='')




from collections.abc import Iterable  # 导入抽象类


class Fibonacci(Iterable):  # 自定义可迭代类
	"""docstrings for Fibonacci"""

	def __init__(self):
		self.a, self.b = 0, 1
		self.total = 0

	def __iter__(self):  # 迭代器对象都有__iter__ 和 __next__两种方法
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		self.total += self.a
		return self.a

	def running_sum(self):
		return self.total


fib = Fibonacci()
print(fib.running_sum)  # 绑定方法
print(fib.running_sum())

for _, i in zip(range(10), fib):
	print(i, end='')

print(fib.running_sum())
print(next(fib))



#

class Access(object):

	def __getattr__(self, name):
		print('__getattr__')
		return super(Access, self).__getattr__(name)

	def __setattr__(self, name, value):
		print('__setattr__')
		return super(Access, self).__setattr__(name, value)

	def __delattr__(self, name):
		print('__delattr__')
		return super(Access, self).__delattr__(name)

	def __getattribute__(self, name):
		print('__getattribute__')
		return super(Access, self).__getattribute__(name)


access = Access()
access.attr1 = True  # __setattr__调用，动态赋值时调用
access.attr1  # 属性存在,只有__getattribute__调用
try:
	access.attr2  # 属性不存在, 先调用__getattribute__, 后调用__getattr__
except AttributeError:
	pass
del access.attr1  # __delattr__调用

import sys


def fibonacci2(n):
	a, b, counter = 0, 1, 0
	while True:
		if (counter > n):
			return
		yield a
		a, b = b, a + b
		counter += 1


f = fibonacci2(10)

while True:
	try:
		print(next(f), end='', sep='%')
	except StopIteration:
		sys.exit()



