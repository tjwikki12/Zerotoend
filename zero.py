#input
n = int(input())
lst=[]   #empty list
non_zero=[]
for i in range(n):
    lst.append(int(input()))
zero_count=lst.count(0)
print(zero_count)
for i in lst:
    if i != 0:
        non_zero.append(i)
zero_lst=[]
for i in range(zero_count):
    zero_lst.append(0)
new_lst=non_zero+zero_lst
print(new_lst)

