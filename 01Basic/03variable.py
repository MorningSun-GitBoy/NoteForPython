a = 21
#We difine a variable only use some str and equal.
#仅需一串字符和一个等号就可以定义一个变量
#In fact,the variables in python are composed by two parts,str and the contants or objects.
#其实，变量由两部分组成，即助记符（变量名）和常量或者说对象组成。
#The variables are the stamp of the contants and objects.
#变量其实就是对内存中常量或者说对象的标记
print(id(a))
"""控制台输出（console）：
    140732244590272
    it will change every time
    会在任何运行时候改变"""
#Function id() will return the vitrul memory addrass of the variable.
#函数 id() 会返回变量的虚拟内存地址
c = 21
#When I have two variable in the same value,python will store only one value,and their id will be the same.
#当两个变量拥有同一值时，python只会存储一个对象，这两个变量会拥有同一id
print(id(c))
print(id(a)==id(c))
"""控制台输出（console）：
    140732244590272
    140732244590272
    True"""
#But the object will has two references , and its reference number will be two.
#但是那个对象将会由两个引用，它的引用计数为2
#When two variables changed,the object whose value is 21 will change its reference number to 0.
#当这两个变量改变时，值为21的对象就会减少引用计数到0.
#Python Explainer will destroy objects whose reference number is 0.
#python解释器会销毁引用计数为0的对象
a = 1+3j
c = None
print(id(a))
print(id(c))
#Python's unique variabe realization make it a free mode to change the value.
#python独特的变量实现使更改变量十分的自由
#You can change variable to any value and any data types as long as you want.
#你可以将变量改编程任何你想要的值和类型
"""控制台输出（console）：
    2399791661872
    140732244133904"""
#It is called weakly typed variable.
#称为弱类型变量