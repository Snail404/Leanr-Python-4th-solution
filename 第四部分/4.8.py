def isthereprime(y):
    x = y // 2
    while x > 1:
        if y % x == 0:
            print(y, 'has factor', x)
            break
        x -= 1
    else:
        print(y, 'is prime')

isthereprime(13)
isthereprime(13.0)
isthereprime(15)
isthereprime(15.0)




#原本我是写不出来的，但是我发觉照抄书上的就好了。唉，从某种意义上来说，我这是在作弊，我的数学素养低到一种让人震惊的地步，这着实让我感到羞愧万分
