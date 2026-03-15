'''n = int(input("enter n : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)'''    


'''num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")'''

'''arr = list(map(int,input("Enter array ele").split()))
inc = True
dec = True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        inc = False
    if arr[i]<arr[i+1]:
        dec = False 
if inc or dec:
    print("monotonic")
else:
    print("not monotonic")'''  



                             