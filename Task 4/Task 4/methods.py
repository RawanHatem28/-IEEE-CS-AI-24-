def get_numbers():
    numbers = [int(x) for x in input("Enter list values separated by space: ").split()]
    return numbers


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


def find_max(lst):
    if not lst:
        return None

    max_val = lst[0]

    # Iterate through the list starting from the second element
    for num in lst[1:]:
        if num > max_val:
            max_val = num  # Update max_val if a larger number is found

    return max_val


def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val


def find_mean(lst):
    total = 0
    count = 0
    for num in lst:
        total += num
        count += 1
    if count == 0:
        return None  # Avoid division by zero
    mean = total / count
    return mean


def find_mode(nums):
    # Dictionary to store frequencies of elements
    freq_dict = {}

    # Count frequencies
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    # Find the maximum frequency
    max_freq = max(freq_dict.values())

    # Find all numbers with maximum frequency
    mode = [key for key, value in freq_dict.items() if value == max_freq]

    return mode


def find_median(lst):
    bubble_sort(lst)
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]


def find_range(lst):
    return find_max(lst) - find_min(lst)


def find_variance(lst):
    mean = find_mean(lst)
    squared_diff = [(x - mean) ** 2 for x in lst]
    variance = sum(squared_diff) / len(lst)
    return variance


def find_STD(lst):
    variance = find_variance(lst)
    return variance ** 0.5


def find_quartiles(lst):
    sorted_lst = bubble_sort(lst)
    q2 = find_median(lst)
    lower_half = [x for x in sorted_lst if x < q2]
    upper_half = [x for x in sorted_lst if x > q2]
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)
    return q1, q2, q3


def find_IQR(lst):
    q1, q2, q3 = find_quartiles(lst)
    return q3 - q1

