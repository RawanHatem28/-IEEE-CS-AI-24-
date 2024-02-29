import methods
if __name__ == "__main__":
    numbers = methods.get_numbers()
    min_value = methods.find_min(numbers)
    max_value = methods.find_max(numbers)
    mean_value = methods.find_mean(numbers)
    mode_value = methods.find_mode(numbers)
    median_value = methods.find_median(numbers)
    range_value = methods.find_range(numbers)
    variance_value = methods.find_variance(numbers)
    STD_value = methods.find_STD(numbers)
    # q1, q2, q3 = methods.find_quartiles(numbers)
    # IQR_value = methods.find_IQR(numbers)

    if min_value is not None:
        print("Min: ", min_value)
    else:
        print("Cannot calculate min value. The list is empty.")

    if max_value is not None:
        print("Max: ", max_value)
    else:
        print("Cannot calculate max value. List is empty")

    if mean_value is not None:
        print("Mean: ", mean_value)
    else:
        print("Cannot calculate mean value. The list is empty.")

    if mode_value is not None:
        print("Mode: ", mode_value)
    else:
        print("Cannot calculate mode value. The list is empty.")

    if median_value is not None:
        print("Median: ", median_value)
    else:
        print("Cannot calculate median value. The list is empty.")

    if range_value is not None:
        print("Range: ", range_value)
    else:
        print("Cannot calculate range value. The list is empty.")

    if variance_value is not None:
        print("Variance: ", variance_value)
    else:
        print("Cannot calculate variance value. The list is empty.")

    if STD_value is not None:
        print("STD: ", STD_value)
    else:
        print("Cannot calculate STD value. The list is empty.")

    # if q1 and q2 and q3 is not None:
    #     print(f"({q1}, {q2}, {q3})")
    # else:
    #     print("Cannot calculate quartiles value. The list is empty.")
    #
    # if q1 and q2 and q3 is not None:
    #     print("IQR: ", IQR_value)
    # else:
    #     print("Cannot calculate IQR value. The list is empty.")
