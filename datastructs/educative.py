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

def main():
    k = 6
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    result = find_averages_of_subarrays(k, arr)
    print(f'Averages of subarrays of size {k} is {result}')
    
if __name__ == "__main__":
    main()
