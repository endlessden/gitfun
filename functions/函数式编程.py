from functools import reduce, partial


x = -1

print(10 / 5)

"""
filter:将sequence中的每个元素，依次传进function函数
（可以自定义，返回的结果是True或者False）筛选，
返回符合条件的元素，重组成一个String,List,Tuple等（跟sequence一样）
map 和filter 用生成器表达式替代，reduce用sum函数替代
"""


def func(x):
	return x % 2 == 0 and x % 3 == 0


res = list(filter(func, (3, 6, 8, 12, 15, 21)))
print(res)

"""
map:将sequence中的每个元素，
依次传进function函数（可以自定义，返回的结果是数值）计算，
无论sequence是什么类型，都返回List
map支持多个sequence输入，但是function也要有相同数量的参数
"""


def func(x):
	return x * 2


print(list(map(func, (3, 6, 8, 12, 15, 21))))


def func(x, y):
	return x + y


seq1 = [3, 6, 4, 8]
seq2 = [6, 4, 3, 7]
print(list(map(func, seq1, seq2)))

"""
 reduce将sequence中的item顺序迭代调用function，例如可以用来对List求和：
"""

def add(x, y):
	return x + y

print('the reduce function.....')
print(reduce(add, [3, 6, 4, 8]))
print(reduce(lambda x, y: x + y, [1, 3, 4, 6, 8]))


def subtract(x, y):
	return x - y


print(reduce(subtract, [3, 6, 4], 20))

print(reduce(lambda x, y: x + y, [3, 6, 4, 8]))

nums = [5, 3, 7, 6, 9]
nums = iter(nums)
print(next(nums))

L = [
	{"name": "python", "age": 12},
	{"name": "ghj", "age": 10},
	{"name": "java", "age": 17}
]
L = sorted(L, key=lambda x: x["age"])
print(L)

sortList = ["4", "3", "5", "2", "1"]
curList = [{"id": "1", "province": "河南"},
           {"id": "2", "province": "河北"},
           {"id": "3", "province": "湖南"},
           {"id": "4", "province": "湖北"},
           {"id": "5", "province": "江西"}]
curList = sorted(curList, key=lambda item: sortList.index(item["id"]),reverse=False)
print(curList)

"""functools.partial可以把一个参数多的函数变成一个参数少的新函数，
少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。"""


def add(a, b):
	return a + b


plus3 = partial(add, 3)
plus5 = partial(add, 5)

print(plus3(4))

print(plus3(7))

print(plus5(10))


def say(name, age):
	print(name, age)


func = partial(say, age=5)
func('the 5 fire')


def get(self, request, *args, **kwargs):
	context = {
		'ua_filter': partial(get_useragent, **{"request": request})
	}
	self.render('index.html', context)


# 先将每个iter内部第一个值和init进行func处理
# 处理的结果再与iter第二个值进行func处理，直到结束。
result = reduce(lambda x, y: x + y, [2, 3, 4, 5, 6], 1)
print(result)




# user-agent: {% ua_filter %}


