"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []
   
    for i in candidates[1:]:
        if i%2!=0:
            x=0
            for h in range(3,i+1):
                    if i%h!=0:
                        x+=1
                    elif x==i-3 and i%h==0:
                        primes.append(i)

    # FIXME: fill out this bit

    return primes
