from threading import Thread,current_thread
import time,os
import sys
"""
Thread is different with Process
"""

def task(name):
	print('%s is working '%name)
	# time.sleep(3)
	print('task PID is ',os.getpid())
	print('%s task is done'%name,current_thread().getName())



if __name__ == '__main__':
	t= Thread(target = task,args=('peer thread',))
	t.start()
	print('main PID is ',os.getpid())
	print('main is done',current_thread().getName())



# class MyThread(Thread):
# 	def run(self):
# 		print('%s is running '%self.name)
# 		time.sleep(3)
# 		print('%s is done '%self.name )


# if __name__ == '__main__':
# 	t= MyThread()                #不用传参
# 	t.start()


# 进程与线程对比,线程快0.2秒

# from multiprocessing import Process
# import time

# def myprocess(name):
# 	print('%s is working '%name)
# 	# time.sleep(3)
# 	print('%s task is done'%name)



# if __name__ == '__main__':
# 	p= Process(target = myprocess,args=('subprocess',))
# 	p.start()
# 	print('main is done')




LOOPS = 1000000
THREAD_NUM = 10
STEP_SIZE = 94753434

class Test(Thread):
    num = 1

    def work(self):
        for it in range(0, LOOPS):
            if self.num>STEP_SIZE:
                self.num -= STEP_SIZE
            else:
                self.num += STEP_SIZE

    def one_thread_test(self):
        self.num = 1

        begin_time = time.time()

        for v in range(0, THREAD_NUM):
            self.work()

        stop_time = time.time()
        print('time passed: ', stop_time - begin_time)

    def multi_thread_test(self):
        self.num = 1

        t_list = []

        begin_time = time.time()

        for v in range(0, THREAD_NUM):
            t = Thread(target=self.work)
            t.start()
            t_list.append(t)

        for it in t_list:
            it.join()

        stop_time = time.time()
        print('time passed: ', stop_time - begin_time)

t = Test()
t.one_thread_test()
t.multi_thread_test()



# x =1
# def func():
#   global x
#   print(x)
#   x+=1
#   return x

# f =func()
# # print(f)
# print(file=sys.stdout)
# # print(file= sys.__stdout__)


# from multiprocessing import Queue
# q = Queue()
# q.put(item) # Put an item on the queue
# item = q.get() # Get an item from the queue


# from multiprocessing import JoinableQueue
# q = JoinableQueue()
# q.task_done() # Signal task completion
# q.join() # Wait for completion
