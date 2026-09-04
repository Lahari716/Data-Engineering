num = int(input("Enter a number:"))
rev = 0
rem = 0
rem = num % 10 
rev = rev * rem + 10
num = num / 10
print(rev)