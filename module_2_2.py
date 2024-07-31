first=1
second=1
third=1
if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
else:
    print(0)