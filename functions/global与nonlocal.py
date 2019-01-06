x = 2

def f1():
	x = 666
	def f2():
		print(x)
	f2()
f1()



def tester(start):              # parameter 和argument 形参和实参
	state = start
	def nested(label):
		print(label,state)
		return 666
	return nested

f=tester(888)
f(999)



def tester2(start):
	state = start
	def nested2(label):
		nonlocal state         # nonlocal 嵌套引用时从当前层函数向外层函数查找
		print(label,state)
		state+=1
	return nested2


f =tester2(123)
f(12)


def calls(trys):
	print('from calls')
	return 666

calls(555)



option = 3

def global_w():
	global option
	option +=2
	print(option)

global_w()



def mm():
	x=12345
	def mmm():
		print('from mmm')
		print(x)
	return mmm

f =mm()
f()



class MixedNames:
	data = 'spam'
	name = 'total'
	def __init__(self,value):
		self.data = value

	def display(self):
		print(self.data,MixedNames.data)

y =MixedNames(1)
print(y)
x = MixedNames(3)
print(x)


x.display()
y.display()

print(x.name)
print(y.name)

def f1():
    x= 42
    def f2():
        def f3():
            print(x)
        f3()
    f2()


f1()


def fun():
	x= 42
	def wrapper():
		print(x)
	wrapper()

fun()


xx= [122]
m = 2

def find():
	mmm=[111,2222]
	# global xx ,可变类型在局部作用域操作时不必声明global,
	#操作可变类型是在原地址操作，不需要重新赋值，所以不需要global
	xx.append(1)
	print(xx)

find()


def find2():
	l=m**3
	str(m)
	print(m,l)


find2()

#全局变量只在函数内赋值时需要global，但是可以引用进行其他操作
#全局变量在函数内不需要声明就能被引用
q= 3
def find3():
	h =q*5
	print(h)

find3()
