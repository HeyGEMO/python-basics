#loops

print("How many times do you want to execute?")
no = int(input())
for i in range(0,no):
    print(i)

list1 =['item1','item2','item3']
for item in list1:
    print(item)
list2=[[1,2,3],[4,5,6],[7,8,9]]
for item in list2:
    for i in item:
        print(i)