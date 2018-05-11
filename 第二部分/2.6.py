D = {'a':1,'b':2} ;                         #创造一个新字典
D['d'] ;                                    #报错了，原因很简单。它根本不存在
#Traceback (most recent call last):
#  File "<pyshell#3>", line 1, in <module>
#    D['d']
#KeyError: 'd'
D['d']='spam' ;                             #创建了一个新的键和值，这和超出边界类似，都是Python自动适应
#D
#{'a': 1, 'b': 2, 'd': 'spam'}
