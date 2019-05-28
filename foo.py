# foo.py.
# understanding __name__ == '__main__'
print("before import")
import math # math = __import__("math")

print("before functionA")
def functionA():

    print("Function A")
print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")