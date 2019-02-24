# Built in Types

import math

def assertEqual(result, expected):
    response = result == expected
    #if(response != True):
    print(str(response) + ' :: ' + str(result) + ' == ' + str(expected))

# numeric types
assertEqual(5 / 3, 1.6666666666666667)
assertEqual(5 // 3, 1)
assertEqual(5 % 3, 2)
assertEqual(math.floor(5.2), 5)

assertEqual(1 | 0, 1)
assertEqual(1 & 0, 0)
assertEqual(1 ^ 0, 1)
assertEqual(1 ^ 1, 0)
assertEqual(101 << 2, 404)
assertEqual(101 >> 2, 25)
assertEqual(~1, -2)

# sequence types
assertEqual(5 in [2,3,5,6], True)
assertEqual(2 not in [1,4,5,6], True)
assertEqual([1,2,3] * 2, [1,2,3,1,2,3])
assertEqual([1,2,3][1], 2)
assertEqual([1,2,3,4][1:3], [2,3])
assertEqual([1,2,3,4,5][1:4:2], [2,4])
assertEqual(max([2,3,4]), 4)
assertEqual([2,3,4,3].count(3), 2)

seq = [2,3,4]
seq[2] = 5
assertEqual(seq, [2,3,5])

seq = [2,3,4]
seq[1:3] = [2,2]
assertEqual(seq, [2,2,2])

seq = [2,3,4]
seq.append(1)
assertEqual(seq, [2,3,4,1])

seq = [2,3,4]
seq.extend([1,1])
assertEqual(seq, [2,3,4,1,1])

seq = [2,3,4]
seq.insert(1,5)
assertEqual(seq, [2,5,3,4])

seq = [2,3,4]
assertEqual(seq.pop(1), 3)
assertEqual(seq, [2,4])

seq = [2,2,4]
seq.remove(2)
assertEqual(seq, [2,4])

seq = [2,3,4]
seq.reverse()
assertEqual(seq, [4,3,2])

def byScore(x):
    return x[1]
seq = [['Bob', 50], ['Tim', 23], ['Mary', 98]]
seq.sort(key=byScore)
assertEqual(seq, [['Tim', 23],['Bob', 50],['Mary', 98]])


# string type
value = 'string'
assertEqual(value.capitalize(), 'String')

value = 'string'
assertEqual(value.endswith('ing'), True)

# finds index of first occurance
value = 'string'
assertEqual(value.find('ri'), 2)

value = ['1','2','3']
assertEqual(':'.join(value), '1:2:3')

value = '  string  '
assertEqual(value.strip(), 'string')

value = 'string'
assertEqual(value.partition('r'), ('st', 'r','ing'))

value = '1:2:3'
assertEqual(value.split(':'), ['1','2','3'])

# pads the string with zeros
value = '12'
assertEqual(value.zfill(4), '0012')


