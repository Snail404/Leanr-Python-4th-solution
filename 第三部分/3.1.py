Q = 'avdsad'            #先搞个字符串再说
for S in Q :
    ord(S)              #题上说了，在交互模式下运行，就没打印出来

for S in Q :
    D += ord(S)         #计算循环哦，这里可跟C不一样，不用提前声明的，哇，感觉真爽

res = []
for S in Q :
    res.append(ord(C))  #这里很简单，返回新列表

list(map(ord,Q))        #这里超简单地说，还是一个列表哦
