lst=[1,2,3,5,7,8,-1]
maximum_lst=lambda x:max(x)
lst2=maximum_lst(lst)
print(lst2)


print('Hello git')
print('Hello git')
print('Hello git')

print('-======-')


print('-======-')
def alg(x,sign,y):
    if sign=='+':
        res=int(x)+int(y)
        return res
    elif sign=='/':
        res=int(x)/int(y)
        return res
    elif sign=='*':
        res=int(x)*int(y)
        return res
    elif sign=='-':
        res=int(x)-int(y)
        return res
x=input("введите первое число ")
sign=input("введите знак ")
y=input("введите второе число")
print(alg(x, sign, y))


