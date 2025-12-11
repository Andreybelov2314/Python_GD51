lst=[1,2,3,5,7,8,-1]
maximum_lst=lambda x:max(x)
lst2=maximum_lst(lst)
print(lst2)


print('Hello git')
print('Hello git')
print('Hello git')

print('-======-')


print('-======-')
def arif(x):
    lst=[]
    signs='+-*/^'
    num=''
    for i in x:
        if i not in signs:
            num+=i
        elif i in signs:
            lst.append(num)
            num=i
    if num not in lst:
        lst.append(num)
    result=int(lst[0])
    for l in lst[1:]:
        if l[0]=='+':
            result+=int(l[1:])
        elif l[0]=='-':
            result-=int(l[1:])
        elif l[0]=='*':
            result*=int(l[1:])
        elif l[0]=='/':
            result/=int(l[1:])
        elif l[0]=='^':
            result**=int(l[1:])
    return result
alg=input("введите пример")
print(arif(alg))

class Temp:

