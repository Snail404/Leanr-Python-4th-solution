L = [1,2,3,4] ;                             #创建一个新的列表
L[4] ;                                      #当我们尝试进行超越边界时，会报错，如下所示
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     L[4]
# IndexError: list index out of range
L[-1000:100] ;                              #接着正常显示，我不知道这是不是3.6版本才有的
L[3:1] ;                                    #不显示任何东西
L[3:1] = ['?'] ;                            #[1, 2, 3, '?', 4]，显示在第三个，也许是Python自动认为修正边界了，后面那个被修改了，然后值就插入到第三个了，我是这么理解的
