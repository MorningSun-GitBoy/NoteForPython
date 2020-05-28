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
#We can find that different constants has different class.
#我们能发现，不同的常量有不同的类型
#type() is a function python provide to get the data type.
#type() 是python用来展示数据类型的函数
#we use type(object) can get the object's data tye,and it will return a string
#我们可以使用type(对象) 来获得数据的表现形式，返回一个字符串
print(type(-3+2J))
print(type(1.2+1j))
"""打印输出(print result)：
    <class 'complex'>
    <class 'complex'>"""
#There is complex data type in python,by using "J"or "j" instead of "i".However,we should make some numbers joint with the char.
#python中具有复数类型，用“J”“j”表示复数中的“i”，但是要求有数字和它相连
print(type(None))
"""打印输出(print result)：
    <class 'NoneType'>"""
#There is a 'NoneType' constant meaning that there isn't any value.
#None类型代表空
print(type(True))
print(type(False))
"""打印输出(print result)：
    <class 'bool'>
    <class 'bool'>"""
#bool constants are the special constants that represent true or false,only two value
#bool常量是一种特殊常量，用以标识真、假，只可取true和false两种值
#The constants in python are defined by themselves.As long as they fit the style,they will be the right type.
#python 的常量由常量自己定义，只要符合特定形式，就会成为那种常量
#You may find that we use a different way to print the data type.That we put type function in the print one means to print the value type() return.
#可能你已经发现，我们用了与前三个不同的方式打印数据类型。将type()放在print()的括号里，意味着打印type()的返回值
#The other finding is that we didn't use the first line comment in this file.This is because we can not assure that in different PC using the same python path.
#而且本文件中我们没写上个文件的首行注释。这是由于我们无法保证任何PC上的python路径都相同。
#When it runs,you can type "python filename.py".
#可以输入"python filename.py"来运行文件