#while loops

print("enter the number:")
number = int(input())

while(number>4):
    print("Number is greater then 4")
    number = int(input())
    if (number == 9):
        break
    if number == 8:
        continue
print("loop ended")