def generator():
	yield 2,20         #yield 可以获取多个值，元祖形式
	yield 3
	yield 4
#迭代器对象可以用for循环遍历

# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。


print(generator)
f = generator()
print(f)
for i in f:
	print(i)


def _get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild

    result, candidates = [], [self]
    while candidates:
        node = candidates.pop()
        distance = node._get_dist(obj)
        if distance <= max_dist and distance >= min_dist:
            result.extend(node._values)
        candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
        return result


def f123():
    yield 1
    yield 2
    yield 3


ite = f123()
print(f123)
print(ite)

for item in f123(): #for 循环生成器
    print(item,end='')


def my_range(first= 0,last= 10,step=1):
	number = first
	while number < last:
		yield number
		number +=step



ranger = my_range(1,10)
print(ranger)

for i in ranger:
	print(i,end='')


def func(x,y=3):        #有多种等效调用方式
	yield x+y
	yield x-y
	yield x*y
	yield x/y



res = func(x=8,y=6)
print(func)
print(res)

for num in res:
	print(num)


def f1():
    g = (i for i in range(10))


def f2():
    g = [(yield i) for i in range(10)]

def f3():
    g = [(yield from range(10))]




def dog(name):
    food_list=[]
    print('狗哥 %s 准备开吃' %name)
    while True:
        food=yield food_list#暂停 food=yield='一桶泔水'
        print('狗哥[%s]吃了<%s>' %(name,food))
        food_list.append(food)


alex_dog=dog('alex')

res1=next(alex_dog) # 初始化，即让狗准备好
print(res1)
# next(alex_dog) # 等同于alex_dog.send(None)
#
# next(alex_dog)

res2=alex_dog.send(('一泡翔','咖啡伴侣'))
print(res2)

res3=alex_dog.send('一桶泔水')
print(res3)

lists=[1,2,3,4]
it = iter(lists)    # iter() 创建迭代器对象,注意区分可迭代对象和迭代器对象
print(next(it))
print(next(it))


def tent_map(mu, x0):   #帐篷映射
    x = x0
    while True:
        yield x
        x = mu * min(x, 1.0 - x)


t = tent_map(2.0, 0.1)
for __ in range(30):
    print(next(t))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))