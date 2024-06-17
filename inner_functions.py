import  sys

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)

decorator(say_whee)
'''
#@decorator
def parent(say_whee):
    print("Printing from parent()")

    def first_child():
        print("Hi, I'm Elias")

    def second_child():
        print("Hi, I'm Esther")
    if num == 1:
        return first_child
    else:
        return second_child

#first_child()
#second_child()

first = parent(say whee)
first()
second = parent(say_whee)
second()
'''
