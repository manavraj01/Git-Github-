def sieve_of_eratosthenes(n):
    """
    Generates all prime numbers up to a given integer n using the 
    Sieve of Eratosthenes algorithm.
    """
    # Create a boolean array "prime[0..n]" and initialize
    # all entries as True. A value in prime[i] will 
    # finally be False if i is not a prime, else True.
    prime = [True] * (n + 1)
    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False
    
    p = 2
    # The outer loop only needs to go up to the square root of n
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p, starting from p*p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
        
    # Collect all the prime numbers
    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)
            
    return prime_numbers

