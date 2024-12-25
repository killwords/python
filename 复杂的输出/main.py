# 主程序
import imports

a = input("Y/n")

if a == "Y":
    a = 'running'
elif a == "n":
    a = "don't running"
else:
    a = None
b = input("请输入内容：")
prints_ = imports.running(a, b)
print(prints_)
