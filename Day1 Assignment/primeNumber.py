# Python program to display all the prime numbers within an interval

prime= int(input("Enter Number To Prime Number: "))
for num in range(prime, prime +100):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=" ")