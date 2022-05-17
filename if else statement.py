print("enter your marks ?")
number = int(input())
print(number)

if (number>90 and number<100):
    grade = 'A'
elif (number>80 and number<90):
    grade = 'B'
else:
    grade = 'Dont know'

print("The grade is ",grade)