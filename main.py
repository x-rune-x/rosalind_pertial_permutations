from math import factorial

# This solves the Partial Permutations problem in Rosalind that asks for the number of permutations of a given
# length (k) exist for a number (n).
# This can be easily solved with the permutation formula.


def partial_perm(n, k):
    # Apply permutations formula nPr = n!/(n-r)!
    return int((factorial(n)/factorial(n-k)) % 1000000)


print(partial_perm(80, 10))
