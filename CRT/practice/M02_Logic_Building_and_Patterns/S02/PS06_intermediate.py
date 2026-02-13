# n = int(input("Output: "))
# for i in range(n):
#    for j in range(n):
#         print("*", end=" ")
#     print() 

# n = int(input("Output: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print() 


# n = int(input("Output  : "))
# for i in range(1, n + 1):
#     for j in range(n - i+1):
#         print("*", end=" ") 
#     print()  



# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     ch = 65
#     for j in range(i):
#         print(chr(ch + j), end=" ")
#     print()

# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(n, end=" ")
#     print()
    

# 11 = [1,2,3,4,5]
# res = []
# for ele in li:
#     res.append(ele*2)
# print(res)    

# li = ['a', 'b', 'c']
# res = " "
# for ch in li:
#     res = res + ch + " "
# print(res)    

# n = int(input("Enter number of rows: "))

# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i) 

# for i in range(n-1,0,-1):
#     print(" " * (n - i) + "* " * i)
    
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    for k in range(2, i + 1):
        print(k, end="")
    
    print()
