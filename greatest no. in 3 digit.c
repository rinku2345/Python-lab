a=int(input ())
b=int(input ())
c=int(input ())
if(a>=b)and(a>=c):
  largest=a
elif(b>=a)and(b>=c):
  greatest=b
else:
  greatest=c
  print("the greatest no. is", greatest)