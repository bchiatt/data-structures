from stack import *
from queue1 import *
from recursion import *

food = Stack()
food.push('hamburger')
food.push('fries')
food.push('cake')

print("1st off the Stack: {0}".format(food.pop()))


line = Queue()
line.enqueue('Bill')
line.enqueue('Sara')
line.enqueue('Beth')

print("1st off the Queue: {0}".format(line.dequeue()))
print("1st off the Queue: {0}".format(line.dequeue()))

print(fact(5))

print("fib num is", fib(8))

for x in range(20):
    print('fib({0}) = {1}'.format(x, fib(x)))

pass
