import numpy as np

def calculate_mean(numbers):

    arr = np.array(numbers)
    return np.mean(arr)


if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print(f"The mean is: {calculate_mean(numbers)}")
