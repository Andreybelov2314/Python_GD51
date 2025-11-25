my_list=[]
while True:
    operation=int(input("введите операцию, для завершения введите 0"))
    if operation==0:
        break
    else:
        my_list.append(operation)
total_in=0
total_ex=0
for i in my_list:
    if i<0:
        total_ex-=i
    if i>0:
        total_in+=i
total=total_in-total_ex
print(f"{total_in}-{total_ex}={total}")










