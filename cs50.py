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

#string methods
name = input("what's your name? ")
name = name.strip()

#f-string
name=input("what's your name? ")
print(f"hello, {name}")


