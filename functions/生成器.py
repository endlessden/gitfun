#生成器可以产出值，也可以接收值
# 协程(生成器)也是iterable对象
# yield 一次就返回一个值，yield from 可以从iterable对象里取值,await 理解为yield from
# result = yield from expr
# 生成器表达式与列表推导式语法非常相似，但生成器表达式返回的不是一个列表类型对象，而是一个生成器对象，生成器是一个内存使用友好的结构。
# 如果在函数中使用生成器表达式作为参数时，我们可以忽略括号 “()”
import inspect

def gen_func():
	m = [1,2,3,4]
	letter = yield 'Δ'
	nums = yield 999
	print(letter)
	print(nums)
	yield 'a'
	yield 'b'

	yield from m   #yield from 取值

def gen2():
	li = ['we','are','the','generators']
	# yield from iterable
	yield from li


if __name__ == '__main__':
	gen = gen_func()
	alpha = next(gen) #启动生成器
	print('alpha:',alpha)
	letter = 'alphabet'
	nums = [4,5,6,7]
	#在send 一次non-None值之前，必须先启动一次生成器,方法 1：gen.send(None) ,2:next()
	gen.send(letter)  #向生成器传值
	gen.send(nums)
	gen.send('continue')
	print(next(gen))
	# gen.close() 结束生成器
	print(next(gen))
	print(next(gen))
	# gen.throw(Exception,'生成器抛出异常')

	print(next(gen2()))
	print(inspect.getgeneratorstate(gen))



# example
def max_lens(filename):
	f = open(filename, 'rt', encoding='utf-8')
	longest = max(len(x.strip()) for x in f) #生成器表达式作为参数
	f.close()
	print(longest)
	return longest

max_lens('example.txt')


def gensquares(N):
	for i in range(N):
		yield i**2

for i in gensquares(5):
	print(i,end=':')

# 与生成器等价
def buildsquares(n):
	res = []
	for i in range(n):
		res.append(i**2)
	return res

for x in buildsquares(5):
	print(x,end=':')


def gen3():
	for i in range(10):
		yield i

g =gen3()
# next(g)
for  i in range(9):
	print(next(g))

class Dog():
	def __init__(self,name):
		self.name = name
	def run(self):
		print('running')
	def barking(self):
		print(f'i am {self.name}')


gilly = Dog('gilly')
gilly.barking()


class Bird():
	def __init__(self,name):
		self.name = name

	def flying(self):
		print('flying now')

	def chow_chow(self):
		print('the bird sound is chow_chow')

nika = Bird('nika')

nika.name = gilly
nika.name.run()
nika.name.barking()

