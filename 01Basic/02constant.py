a = type(1)
b = type(1.5)
c = type("this is a string")
d = type('a')
print(a)
print(b)
print(c)
print(d)
"""打印输出(print result)：
    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'str'>"""
#Last str is a comment using the way we mentioned last time,and it show the console print
#以上的字符串就是我们上次说的“多行注释”，提供了以上代码的输出
#We can find that different constants has different type.
#我们能发现，不同的常量有不同的类型
#type() is a function python provide to get the data type.
#type() 是python用来展示数据类型的函数
#we use type(object) can get the object's data tye,and it will return a string
#我们可以使用type(对象) 来获得数据的表现形式，返回一个字符串