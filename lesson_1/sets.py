# Sets
primes = {2, 3, 5, 7}
odds = {1, 3, 5, 7, 9}

# union: items appearing in either  
union = primes | odds      # with an operator
union = primes.union(odds) # equivalently with a method
print(union)

# intersection: items appearing in both
intersection = primes & odds             # with an operator
intersection = primes.intersection(odds) # equivalently with a method
print(intersection)

# difference: items in primes but not in odds
difference = primes - odds           # with an operator
difference = primes.difference(odds) # equivalently with a method
print(difference)

# symmetric difference: items appearing in only one set
symmetric_difference = primes ^ odds # with an operator
symmetric_difference = primes.symmetric_difference(odds) # equivalently with a method
print(symmetric_difference)

L = [1, 1, 1, 2, 3, 2]
numbers = set(L)
print(numbers)
