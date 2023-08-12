def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The calculated average.
    """
    if not numbers:
        raise ValueError("The list is empty")

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average


if __name__ == "__main__":
    data = [25, 30, 35, 40, 45]
    avg = calculate_average(data)
    print(f"The average is: {avg:.2f}")
