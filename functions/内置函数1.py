import math


print(abs(-1))

print(dict(first='Mary',second='Jack'))

print(dict([('one', 1), ('two', 2), ('three', 3)]))

print(min([2,34,56,7,4]))


"""all() 函数用于判断给定的可迭代参数 iterable
中的所有元素是否都为 TRUE，
如果是返回 True，否则返回 False。
元素除了是 0、空、FALSE 外都算 TRUE。"""
print(all(['a', 'b', 'c', 0]))

print(dir(min))#dir([object])

print(divmod(9,5)) #同时获得商和余数

# print(globals()，locals())  #查找全局作用域,局部作用域

print(hex(555)) #转16进制

print(bin(2))  #转换2进制

print(oct(2))  #转换8进制

# any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True
print(any(['a', 'b', 'c', 'd']))

exec('print("hello world")')

print(callable(0))  # callable判断对象是否可调用

print(bytes('array',encoding='utf-8'))

# bytesarray()    字节列表，可以将元素拼接为字节串

print(math.pow(2,3)) #pow() 方法返回 xy（x的y次方） 的值。

print(type(str([1,2])))

print(bool(0),bool(1))

print(isinstance([1,2],list)) #判断实例

print(ord('a'))  #字符对应的ASCII值

class A:
    pass
class B(A):
    pass

b = B()
print(issubclass(B,A))  #判断子类

print(iter([1,2,3]))  # iter函数生成迭代器

print(tuple([4,5,6]))  #生成元祖

#返回对象object的属性和属性值的字典对象，如果没参数，就打印当前调用位置的属性和属性值 类似 locals()。
print(vars(A))

#冻结集合，不可变
print(frozenset(range(10)))

dicts = {'runoob': 'runoob.com', 'google': 'google.com','a':123}
print(repr(dicts)) # 函数将对象转化为供解释器读取的形式。


 # 函数可以应用于数字、字符串和对象，不能直接应用于 list、set、dictionary
print(hash('aaa'))


intern(string)


# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
arr = [1,2,3,4,5,6,7,8,810]
myslice = slice(1,8,2) # start ,end ,step
new_arr = arr[myslice]
print(new_arr)

names =['Cecilia','Lise','Marie']
lenght = [len(n) for n in names]
print(list(zip(names, lenght)))
longest_name = None
max_letters = 0

for name,count in zip(names,lenght):  #zip函数
	if count>max_letters:
		longest_name = name
		max_letters = count
		print(longest_name,max_letters)


class Test:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def __bool__(self):  # 自定义对象布尔值
		return False


a = Test('Jason', 12)
if a:
	print('up')
else:
	print('down')

scope = {}
exec("print('hello world')") #字符串做代码执行

