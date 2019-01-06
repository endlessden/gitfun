# 在 Python 中，将其他函数作为参数或者返回一个函数的函数称为高阶函数

def deco():
	pass

def factorial(n):
	""" return n!"""
	return 1 if n<2 else n*factorial(n-1)


f =factorial(10)

print(f)

def f(x):
	""" scope the function """
	m= 999
	print(list(globals()))

f(5)

class Foo(object):
    def bar(self):
        print('Foo.bar')


def bar(self):
    print('Modified bar')

Foo().bar()

Foo.bar = bar

Foo().bar()


def a(func):
	def b(x):
		print('bb')
		res = func(x)
		# return res
	return b


@a
def c(d):
	print('c',d)

c('rr')



def calculate(x):
	return x+1

print(list(map(calculate, [1,3,5,7,9])))#被淘汰

print([i+1 for i in [1,3,5,7,9]])

mm = lambda x:x**2

print(mm(3))



