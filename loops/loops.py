x= 0
while True:
	print(x,end='')
	x+=1
	if x>10:
		break

respones = {}
polling_active = True

# while polling_active:
# 	name = input('your name')
# 	respone= input('which mountains do you like to climb today?')
# 	respones['name'] = respone   #name 代表key
# 	repeat = input('another poll ,yes/no')
# 	if repeat == 'no':
# 		break

print('---poll results')

for name, respone in respones.items():
	print(name +'would like to climb '+ respone)

numbers = [2,4,6,8]
product = 1
for number in numbers:
	product *= number
print(product)

for i in reversed(range(1, 10, 2)):
 	print(i)


combs = []
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:
			combs.append((x,y))
print(combs)

#等价上面 列表推导式
improved_combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(improved_combs)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
	print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

