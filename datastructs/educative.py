import random
import math

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
   
def main():
    # k = 6
    # arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # result = find_averages_of_subarrays(k, arr)
    # print(f'Averages of subarrays of size {k} is {result}')


    arr =  [2, 1, 5, 1, 3, 2]
    k = 3
    print(maxSubArraySize(k, arr))
   
    print()
    arr = [2, 3, 4, 1, 5]
    k = 2
    print(maxSubArraySize(k, arr))


    print()
    arr = [2, 1, 5, 2, 3, 2]
    s = 7
    print(smallestSubArrayLen(s, arr))

    print()
    arr =  [2, 1, 5, 2, 8]
    s = 7
    print(smallestSubArrayLen(s, arr))

if __name__ == "__main__":
    main()
