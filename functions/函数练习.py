
import time
def index():
	print('welcome to timer')
	time.sleep(2)

def timer(*args,**kwargs):
	def wrapper():
		start = time.start()
		res = func(*args,**kwargs)
		stop = stop.stop()
		print('run time is %s'%(stop-start))
		return res

	return wrapper

index = timer(index)

x = 100
def main():
	global x            #UnboundLocalError: local variable 'x' referenced before assignment
	x+=1
	print(x)
main()

lax_coordinates= (33.945, -118.408056)
city,year,pop,chg,area= ('tokyo',2003,32450,0.66,8014)
traveler_ids = [('usa','31195855'),('bra','ce32567'), ('esp','xda205856')]
for passport in sorted (traveler_ids):
	print('%s/%s'%passport)
for country, _ in traveler_ids:
	print(country)

registry = []
def register(func):                        #装饰器
	print('running register%s'%func)
	registry.append(func)
	return func

@register
def f1():
	print('running f1()')

print('running main()')
print('registry>>',registry)


def doctest():
	"""
the docs of the function
	"""

print(doctest.__doc__)

def compare(x,y):
	min = x if x < y else y
	print(min)


compare(3,5)




# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass