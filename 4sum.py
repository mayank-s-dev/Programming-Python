# Python3 program to find four
# elements with the given sum

# Function to find 4 elements that
# add up to given sum
def fourSum(X, arr, Map, N):
    temp = [0 for i in range(N)]
    print(temp)
    # Iterate from 0 to length of arr
    for i in range(N - 1):

        # Iterate from i + 1 to length of arr
        for j in range(i + 1, N):
            curr_sum = arr[i] + arr[j]

            # Check if X - curr_sum if present
            # in map
            if (X - curr_sum) in Map:

                # Store pair having map value
                # X - curr_sum
                p = Map[X - curr_sum]
                print(p)
                if (p[0] != i and p[1] != i and
                        p[0] != j and p[1] != j and
                        temp[p[0]] == 0 and temp[p[1]] == 0 and
                        temp[i] == 0 and temp[j] == 0):
                    # Print the output
                    print(arr[i], ",", arr[j], ",",
                          arr[p[0]], ",", arr[p[1]],
                          sep="")

                    temp[p[1]] = 1
                    temp[i] = 1
                    temp[j] = 1
                    break


# Function for two Sum
def twoSum(nums, N):
    Map = {}

    for i in range(N - 1):
        for j in range(i + 1, N):
            Map[nums[i] + nums[j]] = []
            Map[nums[i] + nums[j]].append(i)
            Map[nums[i] + nums[j]].append(j)

    return Map


# Driver code
arr = [10, 20, 30, 40, 1, 2]
n = len(arr)
X = 91
Map = twoSum(arr, n)
print(Map)
# Function call
fourSum(X, arr, Map, n)

# This code is contributed by avanitrachhadiya2155
