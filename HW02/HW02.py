import os   # 載入模組

def main(): #定義main()
    print('Hello world!') #印出字串

    print("This is Alice's greeting.") #印出字串
    print('This is Bob\'s greeting') #印出字串

    foo(5,10) 
    #自訂函數foo(,)，會印出5 plus 10 is equal to 15 和foo

    print('='*10) #印出10個=
    print('Current working directory is ' + os.getcwd()) #印出現在工作路徑


    counter = 0    #令變數counter為0
    counter += 1   #counter = counter + 1

    food = ['apples', 'oranges', 'cats']  #令food為一個list

    for i in food:
        print('I like to eat' + i)
         #依序印出I like to eatapples、eatoranges、eatcats

    print('Count to ten:') #印出字串
    for i in range(10):    #印出0到9
        print(i)

def foo(param1, secondParam): #定義foo()
    res = param1 + secondParam #令res為param1 + secondParam

    print('%s plus %s is equal to %s' % (param1, secondParam, res))
    #印出param1 plus secondParam is equal to res

    if res < 50:
        print('foo')   #符合res < 50，印出foo

    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print('bar')   #符合res >= 50且(param1=42或secondParam=24)，印出bar

    else:
        print('moo')   #其他情況印出foo

    return res         #foo()的output為res


    if __name__ == '__main__':  #執行此檔時，執行main()
        main()
