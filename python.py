# lets practice python and run code
# print("hello world");

# a=input("enter the value of a");
# b=input("enter the value of b");
# print("sum=",int(a)+int(b))

# a=int(input("enter the value of a"));
# b=int(input("enter the value of b"));
# c=int(input("enter the value of c"));
# if((a>b) and (a>c)):
#     print("a is largest");
# elif((b>a) and (b>c)):
#     print("b is largest");
# else:
#     print("c is largest");

# a=int(input("enter the value of a"));
# f=1;
# for b in range(1,a+1,1):
#     f=f*b;
# print("factorial=",f);

# a=str(input("enter the string"));
# for i in range(len(a)-1,-1,-1):
#     print(a[i],end="");

# a=int(input("enter the value of a"));
# a=str(a);
# a=a[::-1];
# print(a);

# a=int(input("enter the value of a"));
# b=int(input("enter the value of b"));
# print("before swapping a=",a,"b=",b);
# intc=a;
# a=b;
# b=intc;    
# print("after swapping a=",a,"b=",b);


# a=int(input("enter the value of a"));
# for b in range(1,a+1,1):
#     print("hello world");

# a=int(input("enter the value of a"));
# for b in range(1,a+1,1):
#     print(b);

# a=int(input("enter the value of a"));
# for b in range(a,-1,-1):
#     print(b);

# a=int(input("enter the value of a"));
# for b in range(1,11,1):
#     print(a*b);

# a=int(input("enter the value of a"));
# sum=0;
# for b in range(1,a+1,1):
#     sum=sum+b;
# print("sum=",sum);

# a=int(input("enter the value of a"));
# even=0;
# odd=0;
# for b in range(1,a+1,1):
#     if(b%2==0):
#         even=even+b;
#     else:
#         odd=odd+b;
# print("even sum=",even);
# print("odd sum=",odd);

# a=int(input("enter the value of a"));
# for b in range(1,a+1,1):
#     if(a%b==0):
#         print(b);

# a=int(input("enter the value of a")); # perfect num sum of facor=a
# sum=0
# for b in range(1,a):
#     if(a%b==0):
#         sum=sum+b;
# if(sum==a):
#     print("perfect num");
# else:
#     print("not perfect num");

# a=int(input("enter the value of a"));
# count=0;
# for b in range(1,a+1,1):
#     if(a%b==0):
#         count=count+1;
# if(count==2):
#     print("prime num");
# else:
#     print("not prime num");



# a=[12,89,88,66,65];
# even=0;
# odd=0;
# for i in range(0,5,1):
#     if a[i]%2==0:
#         even=even+1;
#     else:
#         odd=odd+1;
# print(even)
# print(odd)
              

# a=[];
# max=-9999;
# for i in range(0,5,1):
#     a.append(int(input("enter the value: ")));
# for i in range(0,5,1):
#     if(max<a[i]):
#         max=a[i];
# print(max);


# a=[];
# min=9999;
# for i in range(5):
#     a.append(int(input("enter the value of a")));
# for i in range(5):
#     if min>a[i]:
#         min=a[i];
# print(min);

# num=int(input("enter the value of num"));
# rev=0;
# n=num;
# while num>0:
#     rem=num%10;
#     rev=rev*10+rem;
#     num=num//10;
# if(rev==n):
#     print("palindrome");
# else:  
#     print("not palindrome");


# a=[int(input(f"enter the value of a{i}")) for i in range(5)];
# max=-9999;
# for i in range(len(a)):
#     if(max<a[i]):
#         max=a[i];
# print(max);


# a1=0;
# a2=1;
# c=int(input("enter the value of n"));
# for i in range(1,c+1,1):
#     a3=a1+a2;
#     print(a3);
#     a1=a2;
#     a2=a3;


# a=[int(input(f"enter the value of a{i}")) for i in range(5)];
# pos=0;
# nag=0;
# zero=0;
# for i in range(len(a)):
#     if a[i]>0:
#         pos=pos+1;
#     elif a[i]<0:
#         nag=nag+1;
#     else:
#         zero=zero+1;
# print("positive=",pos);
# print("negative=",nag);
# print("zero=",zero);


# a=[int(input(f"enter the value of a{i}")) for i in range(5)];
# even=0;
# odd=0;
# for i in range(len(a)):
#     if a[i]%2==0:
#         even=even+1;
#     else:
#         odd=odd+1;
# print("even=",even);
# print("odd=",odd);

# a=[]
# for i in range(5):
#     num=int(input(f"enter number"))
#     a.append(num)
# count=0;
# for i in range(5):
#     if(a[i]%2==0):
#         count=count+1;
# print(count);

# a=int(input("enter the number whose table you want to print"))
# for i in range(1,11,1):
#     print(f"{a}*{i}={a*i}");

# a=int(input("enter the number"))
# c=0
# while(a>0):
#     digit=a%10;
#     c=c*10+digit;
#     a=a//10;
# print(c);

# a=[]
# for i in range(5):
#     num=int(input("enter the number"))
#     a.append(num)
# max=a[0]
# smax=a[0]
# for i in range(1,5,1):
#     if(max<a[i]):
#         smax=max
#         max=a[i]
#     elif(smax<a[i] and max!=a[i]):
#         smax=a[i]
# print(smax)

# a=int(input("enter the number"))
# count=0;
# for i in range(2,a):
#     if(a%i==0):
#         count=count+1;
# if(count==1):
#     print("prime")
# else:
#     print("not prime")

# a=int(input("enter the number"))
# c=1;
# for i in range(1,a+1):
#     c=c*i
# print(c)

# a=input("enter the string");
# vowel=0
# for i in range(len(a)):
#     if(a[i] in "aeiouAEIOU"):
#         vowel=vowel+1;
# print("number of vowels=",vowel);

# a=[]
# for i in range(5):
#     num=int(input("enter the number"))
#     a.append(num)
# sum=0;
# b=6;
# for i in range(5):
#     sum=sum+a[i];
# total=b*(b+1)/2;
# missing=total-sum;
# print("missing number=",missing);

# a=int(input("enter the number"))
# rev=0;
# while a>0:
#     digit=a%10;
#     rev=rev*10+digit;
#     a=a//10;
# print("reversed number=",rev);


# a=[]
# count=0
# for i in range(5):
#     num=int(input("enter the number"))
#     a.append(num)
# search=int(input("enter the number to search"))
# for i in range(5):
#         if a[i]==search:
#             count=count+1;
# print(count)

# a=[]
# new=[]
# for i in range(5):
#     num=int(input("enter the number"))
#     a.append(num)
# for i in range(len(a)):
#         if a[i] not in new:
#                new.append(a[i])
# print(new)
 
# a=[]
# for i in range(5):
#     c=int(input("enter the number"))
#     a.append(c)
# first=a.pop(0)
# a.append(first)
# print(a)

# a=[]
# for i in range(5):
#     c=int(input("enter the value"))
#     a.append(c)
# lar=a[0];
# sma=a[0];
# for i in range(5):
#     if a[i]>lar:
#         lar=a[i]
#     if a[i]<sma:
#         sma=a[i]
# print(lar)
# print(sma)

# a=[];
# for i in range(8):
#     num=int(input("enter the value of number"))
#     a.append(num)
# pos=0
# nag=0
# zero=0
# for i in range(8):
#     if(a[i]>0):
#         pos=pos+1
#     elif(a[i]<0):
#         nag=nag+1
#     else:
#         zero=zero+1

# print(f"positive numbers are={pos}")
# print(f"nagatives numbers are={nag}")
# print(f"zeros are={zero}")

# a=[]
# for i in range(7):
#     num=int(input("enter the numbers"))
#     a.append(num)
# lar=a[0]
# slar=a[0]
# for i in range(7):
#     if(lar<a[i]):
#         slar=lar
#         lar=a[i]
#     elif(slar<a[i] and lar!=a[i]):
#         slar=a[i];

# print(slar)


# a=[]
# for i in range(7):
#     num=int(input("enter the numbers"))
#     a.append(num)
# temp=a[0]
# for i in range(6):
#     a[i]=a[i+1]
# a[6]=temp
# print(a)


# a=[]
# for i in range(5):
#     num=int(input("enter the numbers"))
#     a.append(num)
# for i in range(5):
#     temp=a[i]
#     a[i]=a[4-i]
#     a[4-i]=temp
# print(a)

# #
a=[]
for i in range(5):
    num=int(input("enter the numbers"))
    a.append(num)
print(a)

a=[]
for i in range(5):
    num=int(input("enter the numbers"))
    a.append(num)
sum=0
for i in range(5):
    sum=sum+a[i];
print(sum)

a=[]
for i in range(5):
    num=int(input("enter the numbers"))
    a.append(num)
count=0
for i in range(5):
    if(a[i]%2==0):
        count=count+1;
print(count)

a=[]
for i in range(5):
    num=int(input("enter the numbers"))
    a.append(num)
max=a[0]
for i in range(5):
    if(max<a[i]):
        max=a[i]
print(max)

a=[]
for i in range(5):
    num=int(input("enter the numbers"))
    a.append(num)
max=a[0]
smax=-99999
for i in range(5):
    if(max<a[i]):
        smax=max
        max=a[i]
    elif(smax<a[i] and max!=a[i]):
        smax=a[i]
print(smax)



















































































