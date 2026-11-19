
# Write a function create_histogram(numbers, bin_count) that takes a list of numbers and a specified number of bins as input. 
# The function should:
# - divide the range of numbers into bin_count equal-width intervals,
# - count how many values fall into each interval,
# - and return the result as a list of tuples in the format:
# (lower_bound, upper_bound, count)
 
# E.g.
# create_histogram([1, 3, 2, 9, 8, 7], 3)
 
# ->
 
# [
#   (1.0, 3.67, 3),
#   (3.67, 6.33, 0),
#   (6.33, 9.0, 3)
# ]

def create_histogram(num , bin):
    min_val = min(num)
    max_val = max(num)

    bin_width = max_val-min_val
    fial_arr = []

    fial_arr.append(min_val)
    num = 0
    curr_val = min_val
    while num <= 9 :
        num = round(bin_width/bin , 2)
        curr_val += num
        fial_arr.append(curr_val)
        num = curr_val

    return fial_arr

def get_count(numbers,n1,n2):
    count = 0
    for i in range(0,len(numbers)):
        if numbers[i]>= n1 and numbers[i] <= n2:
            count+=1
    return count

def format_output(arr,input_arr):
    result = []
    for i in range(0,len(arr)-1):
        count = get_count(input_arr,arr[i],arr[i+1])
        result.append((arr[i],arr[i+1],count))
    return result


input_arr = [1, 3, 5, 9, 8, 7]
final_arr = create_histogram(input_arr, 3)
print(final_arr)

result = format_output(final_arr,input_arr)
print(result)
