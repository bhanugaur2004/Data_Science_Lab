a = 10
b = 3.14
c = "Hello, World!"
d = True
e = [1, 2, 3, 4, 5]
f = (1, 2, 3)
g = {"name": "Alice", "age": 30}
h = 5+4j

print(type(a))  
print(type(b))     
print(type(c))  
print(type(d))  
print(type(e))  
print(type(f))  
print(type(g))  
print(type(h))  

a = [10,20,30]
b = a

if a is b:
    print("a and b refer to the same object in memory.")
else:
    print("a and b refer to different objects in memory.")

print(id(a))
print(id(b))

a = [1, 2, 3]
b = [1, 2, 3]

print("Equality:", a == b)
print("Identity:", a is b)

print(id(a))
print(id(b))

a = "100"

b = int(a)
c = float(a)

print(b, type(b))
print(c, type(c))

#Reverse an integer

# n = int(input("Enter a number: "))
# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10

# print("Reverse =", reverse)

z = complex(3, 4)

print("Complex Number =", z)

a = True
b = False

print(a and b)
print(a or b)
print(not a)

text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Java" not in text)

numbers = [50, 10, 40, 20, 30]

print(sorted(numbers))
print(sorted(numbers, reverse=True))

text = "PYTHONPROGRAMMING"

print(text[0:6])
print(text[6:])
print(text[:6])
print(text[::2])
print(text[::-1])

#Palindrome

# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#count vowels and consonants

text = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in text:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)