
def recur(num):
    if num<=10:
        print(f'{num} ', end=' ')
        recur(num+1)
        #print(f'{num} ', end=' ')
        
n = int(input('Enter a number: '))
print("The factorial of", n, "is")
recur(n)