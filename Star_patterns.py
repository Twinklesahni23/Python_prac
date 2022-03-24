#Program to write star patterns
#In each star pattern, we use i and j variables to iterate between rows and columns
#I have broken down the complex patterns into simpler triangle ones and combined the for loops as desried

#1 SQUARE STAR PATTERN
n = int(input("Enter the number: "))

for i in range(n): #This is the outer loop to iterate between rows
    for j in range(n): #This is the inner loop to iterate between columns and it depends on the outer loop
        print("*", end=" ")
    print()

#2 INCREASING TRIANGLE PATTERN
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i+1): 
        print("*", end=" ")
    print()

#3 DECREASING TRIANGLE PATTERN
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i,n): 
        print("*", end=" ")
    print()

#4 RIGHTWARD TRIANGLE PATTERN
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i,n): 
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

#5 RIGHTWARD DECREASING TRIANGLE
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n): 
        print("*", end=" ")
    
    print()

#6 HILL PATTERN
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i,n):
        print(" ", end=" ") 
    for j in range(i): #Here we changed the changed from i+1 to just i to get the peak of the hill. Having i+1 columns would give us equal columns in both star triangles 
        print("*", end=" ")
    for j in range(i+1): 
        print("*", end=" ")
    print()

#7REVERSE HILL PATTERN
n = int(input("Enter the number: "))

for i in range(n): 
    for j in range(i+1):
        print(" ", end=" ") 
    for j in range(i,n): 
        print("*", end=" ")
    for j in range(i,n-1): #Here we decrease the number of columns by 1 unit to get the peak of the hill
        print("*", end=" ")
    print()

#8 DIAMOND PATTERN

n = int(input("Enter the number: "))

for i in range(n-1): 
    for j in range(i,n):
        print(" ", end=" ") 
    for j in range(i): 
        print("*", end=" ")
    for j in range(i+1): 
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ") 
    for j in range(i,n-1): 
        print("*", end=" ")
    for j in range(i,n): 
        print("*", end=" ")
    print()

#9 HOURGLASS PATTERN
n = int(input("Enter the number: "))

for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

#10 PYRAMID
n = int(input("Enter the number: "))

for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
