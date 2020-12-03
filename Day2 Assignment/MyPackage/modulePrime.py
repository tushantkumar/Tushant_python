'''
	Intro to modules
'''
def getPrime():
    __name__
my_primes = []
number= int(input("Enter Number To Prime Number: "))
for pr in range(number, number+100):
    isPrime = True
    for i in range(2, pr):
          if pr % i == 0:
              isPrime = False
    if isPrime:
        my_primes.append(pr)
print(my_primes)

if __name__ == '__main__':
    getPrime()
    

    
    
   