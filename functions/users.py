# 每个函数只执行单一而清晰的任务，函数是一等公民
import json
def get_stored_username():
	try:
		with open('username.json') as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input('input your username:')
	with open('username.json','w')as f:
		json.dump(username,f)
	return  username


def greet_user(f):
	username = f()
	if username:
		print(f'welcome back {username}')
	else:
		username = get_new_username()
		print(f'we will remember you when you back {username}')

greet_user(get_stored_username)
