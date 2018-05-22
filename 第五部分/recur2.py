from recur1 import X
from recur1 import Y

#原因很简单，因为recur2的导入是指定的，不会引发循环。而recur1的导入会导致内部架构逐步逐步运行句子，换句话说，会导入循环导入，而计算机其实是找不到的，自然就会报错
#而这时我又很疑惑，在命令行运行时两者结果截然不同。recur2会报错，而recur1不会报错

#   OK,我明白了。如果你在命令行执行的话，import是取出整个模块，模块的变量名在稍后使用点号运算，在获得值之前都不会读取。但是如果使用from来取出特定的变量名，必须记住，只能读取在模块中已经赋值的变量名，所以会报错
