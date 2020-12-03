'''
	1. list of 100 elements with 100 values
    2. check whether each element is a prime
    3. max zero count between 2 primes from the list
'''

lst=[]
firstNum = int(input('Enter a num:'))
for cnt in range(100):
    lst.append(firstNum+ cnt)
    
print(lst)

for cnt in range(100):
    for num in range(2, lst[cnt]):
        if lst[cnt]%num==0:
            lst[cnt]=0
            break
print(lst)

zeroCnt,maxCnt=0,0
first,last = 0,0
for cnt in range(100):
    if lst[cnt] == 0:
        zeroCnt+=1
    else:
        if maxCnt<zeroCnt:
            maxCnt=zeroCnt
            first,last=cnt-maxCnt-1,cnt
        zeroCnt=0
else:
    if maxCnt<zeroCnt:
        maxCnt=zeroCnt
        first,last=cnt-maxCnt,cnt

print(f'zeroCnt--> {maxCnt} between {lst[first]} and {lst[last]}')