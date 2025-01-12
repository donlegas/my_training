numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    for j in numbers:
       if i == 1:
           break
       if j == 1:
           continue
       if i > j and i % j != 0:
           continue
       if i > j and i % j == 0:
           not_primes.append(i)
           break
       if j > i:
           break
       else:
           primes.append(i)

print(primes)
print(not_primes)