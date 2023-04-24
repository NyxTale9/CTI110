a= int(input('Enter grade for Module 1:'))
b= int(input('Enter grade for Module 2:'))
c= int(input('Enter grade for Module 3:'))
d= int(input('Enter grade for Module 4:'))
e= int(input('Enter grade for Module 5:'))
f= int(input('Enter grade for Module 6:'))
Sum_of_Grades =  a + b + c + d + e + f
avg = sum([a, b, c, d, e, f])/len([a, b, c, d, e, f])
print("\n------------Result------------")
print("Lowest Grade:", min([a, b, c, d, e, f]))
print("Highest Grade:", max([a, b, c, d, e, f]))
print("Sum of Grades:", Sum_of_Grades)
print("Average:", round(avg))
print("\n------------------------------")

if avg >= 90:
print('Your grade is: A')
else:
if avg > 80:
print('Your grade is: B')
else:

else:
print('Your grade is: F')
