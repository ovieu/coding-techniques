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
    # use sliding window
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
    # use sliding window,
    # setup sliding window var -> left_char, unique_char-dict, right_char,  maxlen
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
    # setup sliding window
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


def maxLenUniqueSubtring(str):
    # setup the sliding winow
    uniqueList = []
    windowStart = 0
    maxLen = float('-inf') + 1
    
    for windowEnd in range(len(str)):
        right_char = str[windowEnd]
        if right_char in uniqueList:
            while right_char in uniqueList:
                uniqueList = uniqueList[1:]
                windowStart += 1
        uniqueList.append(right_char)
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen


def maxLenSameLetterSubstring(inputStr: str) -> int:
    # setup sliding window
    window_left = 0
    char_freq = {}
    maxLen = float('-inf')
    
    for window_right in range(len(inputStr)):
        right_char = inputStr[window_right]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        
        while len(char_freq) > 2:
            # remove left end from char map
            left_char = inputStr[window_left]
            char_freq[left_char] -= 1
            
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_left += 1
        maxLen = max(maxLen, window_right - window_left + 1)
    return maxLen


def length_of_longest_substring(str, k):
    window_start, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}
    
    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        
        max_repeat_letter_count = max(
            max_repeat_letter_count, frequency_map[right_char])
        
        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def targetPairSumIndex(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return left, right
        elif sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def targetPairSumHashTable(arr, target):
    nums = {}
    for i, num in enumerate(arr):
        if target - num in nums:
            return [i, nums[target - num]]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def targetSumPairHashEasy(arr, target):
    nums = {}
    for i, num in enumerate(len(arr)):
        if target - num in nums:
            return [i, nums[target - num]]
        else:
            nums[target - num] = i
    return [-1, -1]


def targetSumPointers(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


def removeDuplicates(arr):
    next_non_duplicate = 1
    i = 1
    
    while (i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    
    return next_non_duplicate


def makeSquares(arr):
    front = 0
    end = len(arr) // 2
    result = []
    
    while end < len(arr) and front < len(arr):
        frontnum = abs(arr[front])
        endnum = abs(arr[end])
        if frontnum < endnum:
            result.append(pow(frontnum, 2))
            front += 1
        else:
            result.append(pow(endnum, 2))
            end += 1
    return result


def triple_sum_zeor(arr):
    table = arr
    result = []
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                
                if i > 0 and arr[i] == arr[i - 1]:
                    continue
                sum = arr[i] + arr[j]
                if -sum in table:
                    sum_zero_arr = [arr[i], arr[j], -sum]
                    sum_zero_arr.sort()
                    if sum_zero_arr not in result:
                        result.append(sum_zero_arr)
    return result


def findSecLargest(arr):
    """
    returns the second largest num in the arr
    :param arr:
    :return:
    """
    left, right = 0, len(arr) - 1
    second_largest, largest = 0, 0
    while left < right:
        if arr[left] < arr[right]:
            largest = arr[right]
            second_largest = second_largest if second_largest > arr[left] else arr[left]
            left += 1
        else:
            second_largest = second_largest if second_largest > arr[right] else arr[right]
            largest = arr[left]
            right += 1
    return second_largest


def memofib(n, memo={}):
    # if n == 1 or n == 0:
    #     return 1
    # if n in memo:
    #     return memo[n]
    # memo[n] = memofib(n - 1) + memofib(n - 2)
    # return memo[n]
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = memofib(n - 1, memo) + memofib(n - 2, memo)
        memo[n] = result
        return result



def main():
    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = head.next
    # print(cycle_len(head))
    #
    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)
    # head.next.next.next.next.next.next = head.next.next
    # print(cycle_len(head))


if __name__ == "__main__":
    main()
