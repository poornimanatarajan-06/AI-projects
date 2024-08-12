n=int(input("enter the number for size of the list :"))
list=[]
md_list=[]
for i in range(n):
    new=int(input ("enter the elements to be entered in a list="))
    list.append(new)
print(list)
for i in list:
    if(i>=0):
        md_list.append(i)
print(md_list)
        
    
