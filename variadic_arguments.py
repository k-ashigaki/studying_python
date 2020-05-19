"""
Pythonの可変長引数（*args, **kwargs）の使い方
https://note.nkmk.me/python-args-kwargs-usage/
"""

# *args: 複数の引数をタプルとして受け取る

def my_sum(*args):
    return sum(args)

print('my_sum(1, 2, 3, 4): {}'.format(my_sum(1, 2, 3, 4)))
# my_sum(1, 2, 3, 4): 10

print('my_sum(1, 2, 3, 4, 5, 6, 7, 8): {}'.format(my_sum(1, 2, 3, 4, 5, 6, 7, 8)))
# my_sum(1, 2, 3, 4, 5, 6, 7, 8): 36

def my_sum2(*args):
    print('args: ', args)
    print('type: ', type(args))
    print('sum : ', sum(args))

my_sum2(1, 2, 3, 4)
"""
args:  (1, 2, 3, 4)
type:  <class 'tuple'>
sum :  10
"""

def func_args(arg1, arg2, *args):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('args: ', args)

print('func_args(0, 1, 2, 3, 4)')
func_args(0, 1, 2, 3, 4)
"""
func_args(0, 1, 2, 3, 4)
arg1:  0
arg2:  1
args:  (2, 3, 4)
"""

print('func_args(0,1)')
func_args(0,1)
"""
args:  (2, 3, 4)
func_args(0,1)
arg1:  0
arg2:  1
args:  ()
"""

def func_args2(arg1, *args, arg2):
    print('arg1: ', arg1)
    print('args: ', arg2)
    print('args: ', args)

# func_args2(0, 1, 2, 3, 4) # 不正解
"""
func_args2(0, 1, 2, 3, 4)
TypeError: func_args2() missing 1 required keyword-only argument: 'arg2'
最後の値が自動的に位置引数に渡されたりすることはなく、キーワード引数として指定しないとエラーTypeErrorとなる
"""

func_args2(0, 1, 2, 3, arg2=4) # 正解
"""
arg1:  0
args:  4
args:  (1, 2, 3)
"""

# キーワード専用引数 or キーワード限定引数
def func_args_kw_only(args1, *, args2):
    print('args1: ', args1)
    print('args2: ', args2)
# func_args_kw_only(100,200)
"""
func_args_kw_only(100,200)
TypeError: func_args_kw_only() takes 1 positional argument but 2 were given
"""

# kwargs: 複数のキーワード引数を辞書として受け取る
def func_kwargs(**kwargs):
    print('kwargs: ', kwargs)
    print('type: ', type(kwargs))

func_kwargs(key1=1, key2=2, key3=3)
"""
kwargs:  {'key1': 1, 'key2': 2, 'key3': 3}
type:  <class 'dict'>
kwargs**は辞書として引数を吸収する
"""

def func_kwargs_positional(arg1, arg2, **kwargs):
    print('arg1: ', arg1)
    print('arg2: ', arg2)
    print('kwargs: ',kwargs)

func_kwargs_positional(0, 1, key1=1)
"""
args1:  0
args2:  1
kwargs:  {'key1': 1}
"""

# 辞書オブジェクトを引数に指定すると展開し、それぞれを引数で渡せる
d = {'key1': 1, 'key2': 2, 'arg1': 100, 'arg2': 200}
func_kwargs_positional(**d)

"""
arg1:  100
arg2:  200
kwargs:  {'key1': 1, 'key2': 2}
"""

#**を付けた引数は引数の最後でのみ定義できる。**を付けた引数以降に別の引数を定義するとSyntaxerrorになる。
#def func_kwargs_error(**kwargs, arg):
#    print(kwargs)
"""
def func_kwargs_error(**kwargs, arg):
                                  ^
SyntaxError: invalid syntax
"""
