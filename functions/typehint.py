# type-hint，Provide a standard way of annotating a function’s parameters and return values.
 # type hints are just hints

def text22(a:str,b:int) ->str:   #对变量声明类型
	print(a,b)
	return 'hint'

text22('string',6)



x = 'abc' #type: str

class Student:
    def __init__(self):
        self.name=None # type: str

my_list=[] # type: list[Student]
my_map={} # type: dict[int,str]
my_list_2=None # type: Tuple[int,Tuple[int]]


