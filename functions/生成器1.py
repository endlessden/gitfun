"""
1.什么是生成器？
            生成器（generator）是一种特殊的迭代器，比迭代器更优雅，编写更简单，
        2.生成器的两中创建方式：
            1.简单的生成器实现：
                把列表推倒式[]改为()
            2.使用yield创建生成器：
                1.假如函数中有yield，则不在是函数，而是一个生成器
                2.yield会产生一个断点，暂停函数，挂起函数，保存当前状态
                3.假如yield后紧跟一个数据，就会把数据返回，作为next函数或for..in ..迭代出下一个值
                4.可以通过next()唤醒生成器，让生成器从断点处继续执行

        3.yield实现生成器的执行过程：
            1.生成器默认是沉睡的，可以通过next()唤醒生成器
            2.第一次唤醒生成器是从函数的起始位置开始的，直到遇见下一个yield，就会暂停函数，挂起函数
            3.第二次唤醒生成器是从断点开始，直到又遇见yield
            4.当生成器没有了yield，再使用next，则会抛出异常StopIteration

        4.send与next唤醒生成器的不同
            1.generator.send()与next()都可以唤醒生成器，但send可以传值给断点处
            2.使用的方式不同：
                next（generator）：next是内置的函数
                generator.send()：是生成器中的方法
            3.generator.send(None)等价于next(generator)
            4.第一次唤醒生成器时，假如使用send，则只能传Nonem,因为刚开始执行生产器时是没有断点的
"""

def generator():
    while True:
        m = yield 'you'
        yield m


g= generator()
print(next(g))
print(g.send('hello'))
print(g.send('world'))
print(g.send('next time'))
print(g.send('generator'))
print(g.send('world'))
print(next(g))



def generator3(n=0):
    while True:
        yield n*3
        n += 1

g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))




def gen2():
    li = ['we','are','the','unique','generators']
    # yield from iterable object
    yield from li


g2 = gen2()
for i in g2:
    print(i)



import asyncio
import requests
import time


async def download(url): # 通过async def定义的函数是原生的协程对象
    print("get %s" % url)
    response = requests.get(url)
    print(response.status_code)


async def wait_download(url):
    await download(url) # 这里download(url)就是一个原生的协程对象
    print("get {} data complete.".format(url))


async def main():
    start = time.time()
    await asyncio.wait([
        wait_download("http://www.163.com"),
        wait_download("http://www.mi.com"),
        wait_download("http://www.baidu.com")])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

