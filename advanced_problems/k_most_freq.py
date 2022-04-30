# https://www.youtube.com/watch?v=EYFcQRwcqk0
class Solution:
    def __init__(self, array):
        self.array = array

    def find_k_most(self, k):
        freq_map = {}
        ranking = []
        result = []

        # Build a map of all the values in the array with a counter of how often they appear
        # Also initiating an empty array for the sorted ranking
        for item in self.array:
            if item in freq_map:
                freq_map[item] += 1
            else:
                freq_map[item] = 1
            ranking.append(None)

        # Run through the map you made and transform into a "sorted" array, using the index
        # to represent the frequency / counter
        for key in freq_map:
            if ranking[freq_map[key]]:
                ranking[freq_map[key]].append(key)
            else:
                ranking[freq_map[key]] = [key]
        
        # Loop through the ranking array in reverse to get the 2 most occuring
        # values. 
        for i in range(len(ranking) - 1, 0, -1):
            if len(result) < k and ranking[i]:
                result += ranking[i]

        print(result)

s = Solution([1,5,7,3,1,6,6,1])
s.find_k_most(2)

s = Solution([1,5,7,3,1,6,6,2,8,8,5,5,5])
s.find_k_most(1)