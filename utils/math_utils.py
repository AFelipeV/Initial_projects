import logging


def add_numbers(*numbers):
    """
    Add any number of values together.

    Args:
        Tuple of undefined amount of values.

    Returns:
        float: The sum of the given numbers.
    """
    logging.debug(f"Adding numbers: {numbers}")
    return sum(numbers)


def calculate_mean(numbers_amount):
    """
    Calculate the mean (average) of a list of numbers.

    Args:
        int number: Number of values to input.

    Returns:
        float: The mean of the given numbers.
    """
    total = 0
    for i in range(numbers_amount):
        try:
            value = float(input('Enter number '+str(i+1)+': '))
            total += value
        except ValueError:
            logging.error("Only numeric input is allowed.")
            break
    mean = total/numbers_amount if numbers_amount else 0
    return mean


def calculate_median(list_of_numbers):
    """Calculate the median of a list of numbers.

    Args:
        numbers (list of int or float): A list of numeric values.

    Returns:
        float: The median of the list.
    """
    sorted_numbers = sorted(list_of_numbers)
    n = len(sorted_numbers)
    if n == 0:
        logging.warning("Empty list provided to calculate_median.")
        return None
    if n % 2 == 0:
        lower_mid = sorted_numbers[n // 2 - 1]
        upper_mid = sorted_numbers[n//2]
        median = (lower_mid+upper_mid)/2
    else:
        median = sorted_numbers[n//2]
    return median


if __name__ == "__main__":
    # Test examples
    print(add_numbers(5, 7, 7, 8))
    print(calculate_mean(4))
    print(calculate_median([1, 2, 3, 4, 5]))
    print(calculate_median([1, 3, 4, 5]))
