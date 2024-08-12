x={10,20,30,40,0}
y={78,73,78,40,56}
q=x.union(y)
print("union of x and y is ",q)
c=y.difference(x)
print("difference of x and y is ",c)
l=x.intersection(y)
print("intersection of x and y is ",l)
t=y.symmetric_difference(x)
print("symmetric of x and y is ",t)
