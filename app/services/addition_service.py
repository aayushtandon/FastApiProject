from multiprocessing import Pool

def add(a, b):
    return a + b

def perform_addition(numbers: list) -> int:
    if not numbers:
        return 0

    while len(numbers) > 1:
        with Pool() as pool:
            it = iter(numbers)
            numbers = pool.starmap(add, zip(it, it))

    return numbers[0]
