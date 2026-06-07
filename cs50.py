# Aks users for their name and plus one
age = input("how old are you?")
age = int(age)
print(age+1)

# Ask users for their name and square
age = int(input("how old are you?"))
def square(number):
    return number * number
print(square(age))

# Hello name
def greet(friend):
    print("hello, " + name)
name = "Steve"
greet(name)

#compare(same result)
age = input("how old are you? ")
print("I am " + age)
print("I am", age)

#escape conequences(\+character)
print('hello, "friend"')
print("hello, \"friend\"")

#f-string (say hello to the user)
name=input("what's your name? ")
print(f"hello, {name}")

#ask user for their name #remove whitespace from str，Capitalize each word in the user's name, slip user's name into fiirst name and last name
name = input("what's your name? ").strip().title().split(" ")[0]
#say hello to user
print(f"hello, {name}")

#it is equal to：
name = input("what's your name? ")
name = name.strip()
print("hello,", name.title())

def main():
    name=input("what's your name")
    hello(name)
def hello(to="world"):
    print(f"hello, {to}")
main()

x=int(input("what's x? "))
y=int(input("what's y? "))
print(x+y)

x=float(input("what's x? "))
y=float(input("what's y? "))
z=round(x+y)
print(f"{z:,}")

x=float(input("what's x? "))
y=float(input("what's y? "))
z=x/y
print(f"{z:.2f}")

def main():
    x=int(input("what's x? "))
    print("x squared is", square(x))
def square(n):
    return n*n
main()