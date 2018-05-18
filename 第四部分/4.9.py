import math


X = [2, 4, 9, 16, 25]
S = []
for i in X:
    S.append(math.sqrt(i))              #for循环
print(S)

print(list(map(math.sqrt,X)))           #map调用

print(list(math.sqrt(i) for i in X))    #列表解析



#我最喜欢map调用，列表解析也可以，我讨厌for循环，又臭又长，哈哈哈哈
