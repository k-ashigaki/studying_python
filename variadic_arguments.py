"""
Pythonの可変長引数（*args, **kwargs）の使い方
https://note.nkmk.me/python-args-kwargs-usage/
"""

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

