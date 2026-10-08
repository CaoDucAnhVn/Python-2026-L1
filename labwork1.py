#ex1
import math
n = float(input("Enter circle radius? "))
print(f"Circle area = {math.pi * n**2 // 1}")

#ex2
n = int(input("Enter the temperature in Celsius? "))
print(f"{n} (C) = {float(32 + 1.8*n // 1)} (F)")

#ex3
n = int(input("Enter a number? "))

def IsPrime(n):
    if n > 0:
        if n == 1:
            print("1 is a NOT prime number")
        elif n == 2:
            print("2 is a prime number")
        else:
            for i in range (2,n):
                if n % i == 0:
                    print(f"{n} is a NOT prime number")
                    break
                else:
                    print(f"{n} is a prime number")
                    break
IsPrime(n)

#ex4
n = int(input("Enter a number? "))
def IsPerfect(n):
    sum = 0
    if n >= 0:
        if n == 0 | n == 1:
            print(f"{n} is NOT a perfect number")
        else:
            for i in range (1,n):
                if n % i == 0:
                    sum += i
            if n == sum:
                print(f"{n} is a perfect number")
            else:
                print(f"{n} is NOT a perfect number")
        
IsPerfect(n)

    
#ex5
n = str(input("What is your favorite color? "))
index_clr = ["Purple", "Blue","Red"]
e = 0
for i in index_clr:
    e += 1
    if n in i:
        print(f"Your color is at index {e} in my list")
        break
else:
    print("Sorry, I could not find your color")

#ex6
print("range1")
for i in range(7):
    print(f"{i}", end=" ")
print("\nrange2")
for i in range(1, 11,3):
    print(f"{i}", end=", ")
print("\nrange3")
for i in range(5, 0, -1):
    print(f"{i}", end=" ")
print("\nrange4")
for i in range(6, -4,-2):
    print(f"{i}", end=" ")

#ex7
s = str(input("Input a string: "))
def remove_dollar_sign(dollar):
    letter_list = []
    for i in dollar:
        letter_list.append(i)
        if "$" in letter_list:
            letter_list.remove(i)
    return ''.join(letter_list)


remove_dollar_sign(s)
print(remove_dollar_sign(s))

#ex8
l = input("Input a list of integer: ").split()
for i in range(len(l)):
    l[i] = int(l[i])


def extract_even(even):
    letter_list = []
    for i in even:
        letter_list.append(i)
        if i % 2 != 0:
            letter_list.remove(i)
    return letter_list

extract_even(l)
print(extract_even(l))

#ex9
n = int(input("Input a non-negative integer: "))

def factorial(num):
    if num > 0:
        if num == 1 or num == 0:
            return 1
        return num * factorial(num-1)
    
    else:
        print("Positive number only!")

    
factorial(n)
print(factorial(n))

#ex10
n = int(input("Input a number: "))

def divisors(num):
    if num > 0:
        for i in range(1,num + 1):
            if num % i == 0:
                print(f"{i}", end=" ")
    else:
        print("Positive number only!")

    
divisors(n)

#ex11
import math
x1 = float(int(input("Enter x1: ")))
y1 = float(int(input("Enter y1: ")))

x2 = float(int(input("Enter x2: ")))
y2 = float(int(input("Enter y2: ")))

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"Distance = {d}")



#ex12
m = int(input("Enter length: "))
n = int(input("Enter width: "))
def pattern(m, n):
    for i in range(m):#Row
        for k in range(n):#Column
            if i == 0 or i == m - 1 or k == 0 or k == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

pattern(m,n)

