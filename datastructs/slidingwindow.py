def find_averages_of_subarrays(K, arr):
    """
    using the sliding window method
    :param K:
    :param arr:
    :return:
    """
    result = []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr) - K + 1):
        windowSum += arr[windowEnd]

        if (windowEnd >= K - 1):
            result.append(windowSum / K)
            windowSum -= arr[windowStart]
            windowStart += 1
            #just my playing around
            result.index(min(arr))
            result.index(max(arr))

    return result

def find_max_subArray_sum(K, arr):
   result = []
   windowStart, sum = 0, 0

   # iteratet through the array
   for windowStart in range(len(arr) - 1):
       sum += arr[windowStart]

       if (windowStart >= K - 1):
          result.append(sum)
          sum -= arr[windowStart]
          windowStart += 1

   return max(result)


if __name__ == "__main__":
    # K = 5
    # arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # result = find_averages_of_subarrays(K, arr)
    # print(f'Averages of subarrays of size {K}: is {str(result)}')
    arr = [2, 1, 5, 1, 3, 2]
    arr2 = [2, 3, 4, 1, 5]
    print(find_max_subArray_sum(3, arr))
    print(find_max_subArray_sum(2, arr2))
