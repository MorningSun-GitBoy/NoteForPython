#If
#if is the judge key
#if是判断语句关键字
a = 7
b = 15.2
if a < b:
    print(a+b)
#There should be a judge expression behind the key,and using ":" to complete the instruction
#关键字后跟着判断表达式并用“:”结尾，来完成这个语句
#the code block behind if instruction do or not is up to the judge expression return what
#后续代码块是否执行取决于表达式返回什么
if True :
    print(True)
if False :
    print(a)
else :
    print(False)
#else is a key too
#else也是一个关键字
#it must write after an if instruction,meaning that when judge expression return False,the code block behind will run
#else关键字必须在一个if语句后，意味着当判断表达式返回False时else后面的代码开始执行
if a>b:
    print(a)
elif a == 7 :
    print(a)
else :
    print(b)
#elif is another key, using in if judge key
#elif也是if判断关键字中的一个关键字
#Switch