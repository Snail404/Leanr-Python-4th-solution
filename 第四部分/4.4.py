def adder(**good):
    S = []
    V = list(dict.keys(good))
    for i in V :
        S += i
    print(S)


adder(a=1,s=2)

#接受三个参数的，懒得再写了。
#前三个参数都没问题，我输入的是数字，输入第四个会报错，人家只要三个，你给了四个
#可以，关键词参数可以，人家本来就是关键词
#最后一问，自己看代码，懒得跟你BB那么多
