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



