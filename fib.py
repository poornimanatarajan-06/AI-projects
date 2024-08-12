n = int(input("enter the nmber for series=" ))
num1 = 0
num2 = 1
new= num2  
count = 1
 
while count <= n:
    print(new, end=" ")
    count=count+1
    num1, num2 = num2, new
    new= num1 + num2
print()
