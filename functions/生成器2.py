def gensquares(n):
    i = 0
    while i<n:
        yield i*i
        i+=1


g = gensquares(5)

for i in g:
    print(i)


#等价实现
def run(N):
    for i in range(N):
        yield i*i

for item in run(5):
    print(item)



def gensquares2(n):
	for i in range(n):
		yield i*i


g2 = gensquares2(5)

for i in g2:
	print(i)