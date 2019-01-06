import turtle
# from turtles import turtles

def drawsnake(rad,angle,len,neckrad):
	for i in range(len):
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	turtle.fd(rad)
	turtle.circle(neckrad+1,180)
	turtle.fd(rad*2/3)

def main():
	turtle.setup(1300,800,0,0)
	pythonsize = 30
	turtle.pensize(pythonsize)
	turtle.pencolor('red')
	turtle.seth(-40)
	drawsnake(40,80,5,pythonsize/2)
	turtle.done()
if __name__ == '__main__':
	main()

"""
1、__name__这个系统变量显示了当前模块执行过程中的名称，
如果当前程序运行在这个模块中，__name__ 的名称就是__main__如果不是，则为这个模块的名称。
2、__main__一般作为函数的入口，类似于C语言，
尤其在大型工程中，常常有if __name__ == "__main__":来表明整个工程开始运行的入口。
"""
