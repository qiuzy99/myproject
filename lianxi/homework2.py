'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
　　
'''

s = input('请输入字符串')
l =len(s)

def out_put(s,l):
    if l == 0:
        return
    print(s[l-1],end='')
    out_put(s,l-1)

out_put(s,l)