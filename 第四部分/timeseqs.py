import sys, mytimer, math
reps = 1000
repslist = range(reps)

def sqrtX1():
    return math.sqrt(4)
def sqrtX2():
    return 4 ** .5
def sqrtX3():
    return pow(4, .5)

print(sys.version)
for tester in (mytimer.timer,):
    for test in (sqrtX1, sqrtX2, sqrtX3):
        elapsed, restlt = tester(test)
        print('-' * 35)
        print('%.5f' % elapsed)



#原谅我没用，这代码还是我从书上抄下来的，我真的很懒，我懒得再去做改进了，再说我也不会很多
#然后呢，第二个最快，也就是直接开平方这个，而不是用各种函数，多半是因为函数里面还有迭代吧
#答案里面说手动循环比列表解析快，我反正没理解。如果你看到了，还请给我解答，谢谢，么么哒    
