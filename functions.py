# Built in Functions

def assertEqual(result, expected):
    response = result == expected
    #if(response != True):
    print(str(response) + ' :: ' + str(result) + ' == ' + str(expected))


# abs
# Returns the absolute value
assertEqual(abs(5), 5)
assertEqual(abs(-5), 5)

# all
# Returns True if all iterable elements are True
value = [True, True, True]
assertEqual(all(value), True)

value = [True, False, True]
assertEqual(all(value), False)

value = []
assertEqual(all(value), True)

value = [1, True, 'test']
assertEqual(all(value), True)

# any
# Returns True if any iterable element is True
value = [True, True, True]
assertEqual(any(value), True)

value = [True, False, True]
assertEqual(any(value), True)

value = []
assertEqual(any(value), False)

value = [1, True, 'test']
assertEqual(any(value), True)

# ascii
# Returns ascii escaped string
assertEqual(ascii('Te♥t'), ascii('Te\u2665t'))

# bin
# Converts number to binary
assertEqual(bin(5), '0b101')
assertEqual(format(5, '#b'), '0b101')
assertEqual(format(5, 'b'), '101')
assertEqual(bin(-5), '-0b101')

# bool
# Converts to a boolean
assertEqual(bool(1), True)
assertEqual(bool(False), False)
assertEqual(bool(''), False)
assertEqual(bool('Test'), True)
assertEqual(bool([]), False)
assertEqual(bool([1, 'Test', False]), True)

# bytearray
# Creates arrays of bytes for byte calculations
assertEqual(bytearray(5), bytearray(b'\x00\x00\x00\x00\x00')) #Initialized an array of 5 empty bytes
assertEqual(bytearray([5]), bytearray(b'\x05'))
assertEqual(bytearray('Test', 'UTF-8'), bytearray(b'Test'))

# bytes
# Same as bytearray but immutable (not changeable)
assertEqual(bytes(5), bytes(b'\x00\x00\x00\x00\x00')) #Initialized an array of 5 empty bytes
assertEqual(bytes([5]), bytes(b'\x05'))
assertEqual(bytes('Test', 'UTF-8'), bytes(b'Test'))

# callable
# Determines if you've given it a function or not
class Duck:
    name = 'Bill'
    def quack():
        return 'quack'

duck = Duck()
assertEqual(callable(duck.quack), True)
assertEqual(callable(duck), False)
assertEqual(callable(duck.name), False)

# chr
# Returns character from unicode
assertEqual(chr(97), 'a')
  
# @classmethod
# Defines a method as a class method
class Duck:
    @classmethod
    def quack(cls):
        return 'quack'

assertEqual(Duck.quack(), 'quack')
assertEqual(Duck().quack(), 'quack')

# compile
# Compiles text into an executable object
object = compile('print(\'Hello World!\')', '', 'eval')
assertEqual(eval(object), None)

object = compile('\'Hello World!\'', '', 'eval')
assertEqual(eval(object), 'Hello World!')

# complex
# Creates a complex number
assertEqual(complex(5, 2), (5+2j))
assertEqual(complex('5+2j'), (5+2j))
assertEqual(complex('5'), (5+0j))

# delattr
# Deletes an attribute on the object
class Duck:
    name = 'Bill'

assertEqual(Duck.__dict__.get('name', None), 'Bill')
delattr(Duck, 'name')
assertEqual(Duck.__dict__.get('name', None), None)

# dict
# Creates a dictionary (map)
value = dict({'key':'value'})
assertEqual(value, {'key':'value'})

# dir
# Returns list of all available methods of object including inherited.
class Duck:
    def quack():
        return "quack"

assertEqual(dir(Duck), ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'quack'])

# divmod
# Returns a tuple with the quotiont (num of times it was divisiable) and remainder
assertEqual(divmod(10, 5), (2,0))
assertEqual(divmod(5, 3), (1,2))
assertEqual(divmod(7.5, 3.2), (2.0, 1.0999999999999996))

# enumerate
# Adds an index to a iterable object
assertEqual(list(enumerate(['Zero', 'One', 'Two'])), [(0, 'Zero'), (1, 'One'), (2, 'Two')])

# eval
# Evaluates a string as python code and returns a value
assertEqual(eval('1+2'), 3)

# exec
# Executes a code object as python code and doesn't return a value
object = compile('x=2\nprint(x+3)', '', 'exec')
assertEqual(exec(object), None)

# filter
# Filters an iterable list with the use of the function
assertEqual(list(filter(None, [True, False, True])), [True, True])

def greaterThanTwo(x):
    return x > 2

assertEqual(list(filter(greaterThanTwo, [1, 2, 3, 4])), [3, 4])

# float
# Returns a floating point number
assertEqual(float('1.23'), 1.23)

# format
# Formats a value by the formatspec into a string
assertEqual('{:,}'.format(1234567), '1,234,567')
assertEqual('{1}, {0}'.format('a', 'b'), 'b, a')

# frozenset
# Returns an immutable (not changeable) set
assertEqual(frozenset([1,2]), {1,2})

# getattr
# Gets the value of an attribute
class Duck:
    name = 'Bill'

assertEqual(getattr(Duck, 'name'), 'Bill')

# hasattr
# Checks if attribute exists
class Duck:
    name = 'Bill'

assertEqual(hasattr(Duck, 'name'), True)
assertEqual(hasattr(Duck, 'height'), False)

# hash
# Gets hash value
assertEqual(hash(1), 1)

# hex
# Gets a hex value
assertEqual(hex(10), '0xa')
assertEqual(hex(-2), '-0x2')

# id
# Gets an identity value of an object
class Duck:
    name = 'Bill'

duck1 = Duck()
duck2 = Duck()
assertEqual(id(duck1) != id(duck2), True)

# int
# Gets an int
assertEqual(int('1'), 1)
assertEqual(int(1.23), 1)

# isinstance
# Checks if the object is an instance of the class
class Duck:
    name = 'Bill'

duck = Duck()
assertEqual(isinstance(duck, Duck), True)

# issubclass
# Checks if the class inherits from another class
class Duck:
    name = 'Bill'

class Mallard(Duck):
    name = 'Bob'

assertEqual(issubclass(Mallard, Duck), True)
assertEqual(issubclass(Duck, Mallard), False)

# iter
# Creates an iterable object of the sequence
value = iter([1,2,3])
assertEqual(next(value), 1)
assertEqual(next(value), 2)

# len
# Returns length of sequence or object in case of string
assertEqual(len([1,2,3]), 3)
assertEqual(len('Test'), 4)

# map
# Apply a function to each item in the iterable
def multipy(x):
    return x * 2

assertEqual(list(map(multipy, [1,2,3])), [2,4,6])

# max
# Returns max element in iterable
assertEqual(max([1,3,2]), 3)

# min
# Returns min element in terable
assertEqual(min([1,3,2]), 1)

# next
# Returns next item from an iterable
value = iter([1,2,3])
assertEqual(next(value), 1)
assertEqual(next(value), 2)

# oct
# Returns an octal base 8
assertEqual(oct(5), '0o5')
assertEqual(oct(9), '0o11')

# open
# Opens a file for reading

# ord
# Returns a unicode code
assertEqual(ord('a'), 97)

# pow
# Computes power
assertEqual(pow(2, 5), 32)

# property
# Define custom getter, setter, deleter
class Duck:
    def __init__(self):
        self._name = None
    def getname(self):
        return 'Mr {0}'.format(self._name)
    def setname(self, value):
        self._name = value
    name = property(getname, setname, None, 'Set his name')

duck = Duck()
duck.name = 'Bill'

assertEqual(duck.name, 'Mr Bill')

# range
# Returns a sequence
assertEqual(list(range(2)), [0,1])

# repr
# Creates a string representation of an object
class Duck:
    name = 'Bill'
    def __repr__(self):
        return 'Duck.name={0}'.format(self.name)

duck = Duck()
assertEqual(repr(duck), 'Duck.name=Bill')

# reversed
# Reverses a sequence
assertEqual(list(reversed([1,2,3])), [3,2,1])

# round
# Rounds a number (Doesn't round up at hundres place)
assertEqual(round(1.25), 1)
assertEqual(round(1.27, 1), 1.3)

# set
# Returns a set (removes duplicates)
assertEqual(set([1,2,3,1]), {1,2,3})

# setattr
# Sets a value to the attribute
class Duck:
    name = None
duck = Duck()

setattr(duck, 'name', 'Bob')
assertEqual(duck.name, 'Bob')

# slice
# Creats a slice function that can be applied to sequences / strings
value = slice(1,3)
assertEqual([1,2,3,4,5][value], [2,3])
assertEqual('Test'[value], 'es')

# sorted
assertEqual(sorted([3,1,2]), [1,2,3])
assertEqual(sorted([3,1,2], reverse=True), [3,2,1])

# staticmethod
# Creats a static method on the class
class Duck:
    @staticmethod
    def quack():
        return 'Quack'

assertEqual(Duck.quack(), 'Quack')

# str
# Converts to string
assertEqual(str(1), '1')

# sum
# Calculates sum
assertEqual(sum([1,2,3]), 6)

# super
# Allows access to parent methods that were hidden
class Duck:
    def speak(self):
        return 'Quack' 

class Mallard(Duck):
    def speak(self):
        return super().speak() + ' Quack'

duck = Mallard()
assertEqual(duck.speak(), 'Quack Quack')

# tuple
# Creates an immutable sequence
assertEqual(tuple([1,2,3]), (1,2,3))

# type
# Returns object type
assertEqual(type(1), int)

# zip
# Merges two sequences into a sequence of tuples
assertEqual(list(zip([1,2,3], [4,5,6])), [(1,4),(2,5),(3,6)])












