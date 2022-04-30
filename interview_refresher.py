# Basics to review before an interview

print("=========== PRINT ===========")

# Python3 wraps in parenthesis
print('hi')

# Comma separate for multiple printing 
print('hello', 'world', 5)

# Inverse boolean
print(not True)

print("=========== ITERATING ===========")

test = ['A', 'B', 'C']

# Simple for loop
for letter in test:
    print(letter)

# Simple for loop with index
for idx, letter in enumerate(test):
    print(idx, letter)

# Loop number of elements using range
for idx in range(len(test)):
    print(idx, test[idx])

map = {
    'a': 'test1',
    'b': 'test2',
}

# Only get keys
for key in map:
    print(key, map[key])

# Get key and values
for key, value in map.items():
    print(key, value)

# Only get values
for value in map.values():
    print(value)


print("=========== EXISTENCE ===========")

# Check key in map
if 'b' in map and 'a' in map:
    print('found')

# Check item in array
if 'B' in test or 'C' not in map:
    print('found')

print("=========== FUNCTION / CLASS ===========")

# Simple function return
def hello_world():
    return 'hello world'

result = hello_world()
print(result)

# function return tuple and deconstruct
def tuple_world():
    return 1, 2

x, y = tuple_world()
print(x, y)

# Static object
class Data:
    x = 1
    y = 2

print(Data.x)
Data.y = 'test'
print(Data.y)

# Instance object
# with sub functions
class SetData:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def overrideX(self, x):
        self.x = x

    def printer(x):
        print(x)

d = SetData(5, 6)
print(d.x)
d.overrideX(7)
print(d.x)

print("=========== STRING MANIPULATION ===========")

# Cast int to string
print('something ' + str(1))

test = "A B C"

# Split string
result = test.split(" ")
print(result)

print("=========== ARRAY MANIPULATION ===========")

a = [1, 2, 3]
b = [4, 5, 6]

# concats
print(a + b)

# last item
print(a[-1])

# subset of list at idx 1
print(a[1:])

# subset of list until idx 2 (non inclusive)
print(a[:2])

# adds to end
a.append(4)
print(a)

# removes from end
a.pop()
print(a)

# removes from begining
a.pop(0)
print(a)

print("=========== ERROR / TESTING ===========")

# Try Catch Finally
try: 
    print('hi')
    raise Exception('oh no')
except Exception as e:
    print(e)
finally:
    print('bye')

# Assertions
assert 1 == 1
assert 1 == 2, 'FAILED'
