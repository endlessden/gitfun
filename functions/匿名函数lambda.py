counters = [1,2,3,4]
l = list(map((lambda x:x+3),counters))     # lambda和map函数
print(l)


l = [{'name':'alex','age':85},{'name':'egon','age':18},{'name':'oldboy','age':73}]  #
l.sort(key=lambda items:items['age'])
print(l)


print(map((lambda x: x*2),counters))


def func(x,n):
    action = (lambda x:x**n)
    return action(x)

f=func(5,3)
print('the action res is:', f)

multi=lambda x,y:x*y #lambda关键字定义,以':'分割，左边为参数列表，右边为返回结果的表达式
print(multi(2,3))


def deco(func):
	def wrapper(*args,**kwargs):
		print('aaa')
		print('asss')
		func(*args,**kwargs)
	return wrapper

@deco
def trees(a,b='newbee'):
	print('i\'m the trees',a,b)

trees(1)



def testFun():
   temp = [lambda x : i*x for i in range(4)]
   return temp

for everyLambda in testFun():
   print (everyLambda(2))



try:
	x = 1
	x > 0
except Exception as e:
	print(e)
except KeyError as e:
	print(e)
except ValueError as e:
	print(e)
else:
	print('no error')

finally:
	print('over')


