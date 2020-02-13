import random
import math
import sys

def find_averages_of_subarrays(k, arr):
    # use the sliding window method -> windowSum, windowStart, result
    result = []
    windowStart, windowSum = 0, 0.0
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1
        
    return result

def maxSubArraySize(k, arr):
    windowStart, maxSubArrSum = 0, 0
    windowSum = 0
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        if windowEnd >= k - 1:
            maxSubArrSum = max(maxSubArrSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSubArrSum
  
def smallestSubArrayLen(s, arr):
    #use sliding window
    # set up sliding window variables
    minSubArrLen = math.inf
    windowStart, windowSum = 0, 0
    
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        
        # iterate through the right end
        # check if the current window is greater than target
        while windowSum >= s:
            minSubArrLen = min(minSubArrLen, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
        # if greater
        # check if len is smaller
        # remove the left end element
        # shift the left end
    return minSubArrLen
  
def longestSubstringKDistinct(k, str):
    #use sliding window,
    #setup sliding window var -> left_char, unique_char-dict, right_char,  maxlen
    maxLen = - math.inf + 1
    windowStart = 0
    char_frequency = dict()
    
    for windowEnd in range(len(str)):
        right_char = str[windowEnd]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        while len(char_frequency) > k:
            left_char = str[windowStart]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            windowStart += 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen

def maxFruitsInBasket(arr):
    #setup sliding window
    # stat moving the right end of the window
    window_start, maxLen = 0, -sys.maxsize + 1
    fruit_frequency = {}
    
    for window_end in range(len(arr)):
       # update the unique fruit counter
        right_fruit = arr[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1
        
        while len(fruit_frequency) > 2:
            left_fruit = arr[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1
            
        maxLen = max(maxLen, window_end - window_start + 1)
    return maxLen
        
    # check if new window exceeds 2 unique fruits
        # if exceeds, remove the firts till only 2 fruits
    #  update the maxlength of the tree
    
    pass

def main():
    fruits = ['A', 'B', 'C', 'A', 'C']
    fruits2 = ['A', 'B', 'C', 'B','B', 'C']
    print(maxFruitsInBasket(fruits))
    print(maxFruitsInBasket(fruits2))

if __name__ == "__main__":
    main()
