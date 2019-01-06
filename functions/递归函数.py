def mysum(L):
	print(L)       # 递归叠加
	if not L:
		return 0
	else:
		return L[0] +mysum(L[1:])

s = mysum([1,2,3])
print(s)


L =[1,2,3]
x=0
for i in L:       # 等效for循环
	x +=i
print('is:',x)



g = (i**2 for i in L)

for x in g:
	print(x)

def fact(n):          #计算n的阶乘递归
	if n == 1:
		return 1
	return n*fact(n-1)

print(fact(100))



