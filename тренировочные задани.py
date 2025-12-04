lst=[1,2,3,5,7,8,-1]
maximum_lst=lambda x:max(x)
lst2=maximum_lst(lst)
print(lst2)


print('Hello git')
print('Hello git')
print('Hello git')

print('-======-')


print('-======-')
def alg(x):
    first=''
    second=''
    sign=''
    flag=True
    for i in x:
        if i.isalnum() and flag==True:
            first+=i
        elif i.isalnum() and flag==False:
            second+=i
        else:
            sign+=i
            flag=False
    if sign=='+':
        res=int(first)+int(second)
        return res
    elif sign=='-':
        res=int(first)-int(second)
        return res
    elif sign=='*':
        res=int(first)*int(second)
        return res
    elif sign=='/':
        res=int(first)/int(second)
        return res


example=input('введите пример')
print(alg(example))


