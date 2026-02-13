def check_number(num: int) -> str:

    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def first_n_primes(n: int) -> list:

    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

        candidate += 1

    return primes


def sum_1_to_100() -> int:
    total = 0
    i = 1

    while i <= 100:
        total += i
        i += 1

    return total
