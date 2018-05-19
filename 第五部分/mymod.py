def countlines(names):  #这个版本是我自己写的，错误的，严重错误！！！
    len(for line in open(names).readlines)

def correct_countline(names):    #这个版本是看答案的，这个才是正确的
    return len(open(names).readlines())

def countChars(names):  #这个版本也是错误的，也是我自己写的，好丢脸...
    len(for chars in open(names).read)

def correct_countChars(names):  #书上提供的正确答案哦
    return len(open(names).read())

def test(Q,W):  #这个是我自己写的，我还以为是随便调用两个计算的函数呢，晕
    A = len(Q)
    B = ord(Q)

def test(names):    #这个是书中提供的正确答案写法
    return correct_countline(names), correct_countChars(names)
    
