import math
n1,m1=map(int,input().split())
b1=n1*m1
root=math.sqrt(b1)
if root*root==b1:
    print("yes")
else:
    print("no")
