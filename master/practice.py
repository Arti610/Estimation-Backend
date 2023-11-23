#-------- pallindrome string ------------
# def p(s):
#     temp=s[::-1]
#     if temp==s:
#         print('true')
#     else :
#         print('false')

# s='nitin1'
# p(s)


#------- pallindrome string ------------#
# def pallindrome(s):
#     n=len(s)
#     for i in range(n):
#         if s[i] != s[n-i-1]:
#             return False
#     return True

# input=input('enter name')
# print(pallindrome(input))

#-------- pallindrome number ---------
# def pallindromeNuber(num):
#     temp=num
#     rev_num=0
#     while(temp>0):
#         digit=temp%10
#         rev_num=rev_num*10 + digit
#         temp=temp//10
#     if num==rev_num:
#         return True
#     return False

# n=int(input('enter number : '))
# print(pallindromeNuber(n))
    
#----------- fizzbuzz -----------   
# for i in range(1,100+1):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#         continue
#     elif i%5==0:
#         print('Buzz')
#         continue
#     elif i%3==0:
#         print('Fizz')
#         continue
#     else :
#         print(i)

#------- fibonacci series -----------
# a=0
# b=1
# print(a)
# for i in range(10):
    # print(b)
    # n3=a+b
    # a=b
    # b=n3
    # or 
    # a,b=b,a+b
    # print(a)


#using recursion
# def fibbonacci(i):
#     if i<=1:
#         return 1
#     else:
#         return fibbonacci(i-1)+fibbonacci(i-2)

# num=int(input('Enter the number'))
# if num<=0:
#     print("Please enter a valid number")
# else :
#     for i in range(num):
#         print(fibbonacci(i),end=' ')

# using fuction

# def fibbonacci(n):
#     a,b=0,1
#     if n==1:
#         print(a)
#     else:
#         print(a,end=' ')
#         print(b,end=' ')
#         for i in range(2,n):
#             a,b=b,a+b
#             print(b,end=' ')
            
# fibbonacci(10)




# s='nidtin'
# temp=s[::-1]
# if s==temp:
#     print('yes')
# else:
#     print('no')



# s='niting'
# len=len(s)
# for i in range(len-1):
#     if s[i]!=s[len-i-1]:
#         print('no')
#         break
    
# else:
#     print('yes')
   
   
   
    
# num=1211
# temp=num
# sum=0
# while (temp>0):
#     digit=temp%10
#     sum=sum*10+digit
#     temp=temp//10
    
# if num==sum:
#     print('yes')
# else:
#     print('no')
   
   
   
   
# a=0
# b=1
# for i in range(10): 
#     print(a)
#     a,b=b,a+b



# l=[4,9,0,5]
# first=0
# second=0
# if l[0]>l[1]:
#     first=l[0]
#     second=l[1]
# else:
#     first=l[1]
#     second=l[0]
# for i in range(2,len(l)):
#     if first<l[i]:
#         second=first
#         first=l[i]
#     elif second<l[i] and first!=l[i]:
#         second=l[i]

# # print(first,second)



# s='aaaassssssssbbss'
# new=''
# counter=1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         counter+=1
#     else:
#         new=new+s[i]+str(counter)
#         counter=1
# new=new+s[len(s)-1]+str(counter)
    
# # print(new)
# for n in range(1,50):
#     if n>1:
#         for i in range(2,(n//2+1)):
#             if n%i==0:
#                 break
            
#         else:
#             # print(n)
#             # print('yes')
#     # else:
#     #     print('no')



# s='This_is_moer'
# temp=s.split('_')
# l=[]
# for i in temp:
#     l.append(i[0].lower()+i[1:].upper())
# s='.'.join(l)
# print(s)

# s='This_is_moer'
# temp=s.split('_')
# l=''
# for i in temp:
#     l=l+i[0].lower()+i[1:].upper()+'.'

# print(l)



# for n in range(1,1000):
    
#     temp=n
#     result=0
#     while(temp>0):
#         digit=temp%10
#         result=result+(digit**3)
#         temp=temp//10
        
#     if result==n:
#         print(n)


# s='agrrgffffg'
# ch={}
# for i in s:
#     if i in ch:
#         ch[i]+=1
#     else:
#         ch[i]=1
    
# print(max(ch,key=ch.get))


# def fact(n):
#     s=1
#     for i in range(1,n+1):
#         s=s*i
    
#     return s

# def facto():
#     start =int(input('Start '))
#     end =int(input('end '))
    
#     for n in range(start,end):
#         temp=n
#         sum=fact(n)
    
#         print(sum)


# facto(


