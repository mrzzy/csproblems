#
# CSProblems
# Cracking the Coding Interview
# 5.9 Enumerate All Primes to n
#


def find_primes(n: int):
    """Generate all primes up to n."""

    # is_prime[i]: whether i is prime
    is_prime, primes = [True] * (n + 1), []

    # 0, 1 not considered primes, skip
    for i in range(2, n + 1):

        if is_prime[i]:
            primes.append(i)
            # mark all other multiples of i up to n as not prime
            # optimisation: mark from i^2 as ki multiples where k < i have
            # already been marked by earlier sieve iterations
            for j in range(i, n // i + 1):
                is_prime[i * j] = False

    return primes


if __name__ == "__main__":
    assert find_primes(10) == [2, 3, 5, 7]
    print(find_primes(128))
