L = [0,1,2,3] ;                               #创建一个新列表
L[2] = [] ;                                   #会替换原本2的位置，变成一个空列表，谁让列表是可变的
L[2:3] =[] ;                                  #就会删除它们之间的信息
del L[0] ;                                    #第1个位置被删除了，很简单
del L[1:] ;                                   #这个删除了第2个以后的所有东西，所以第1个保留了下来
L[1:2] = 1 ;                                  #会报错，不给这样做，要可以迭代的才可以放进去
#Traceback (most recent call last):
#  File "<pyshell#16>", line 1, in <module>
#    L[1:2] = 1
#TypeError: can only assign an iterable
