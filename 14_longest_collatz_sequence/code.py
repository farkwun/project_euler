import time

tic = time.perf_counter()
memo = {}


def recursive_collatz_sequence(n):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        length = recursive_collatz_sequence(n // 2)
    else:
        length = recursive_collatz_sequence((3 * n) + 1)
    memo[n] = length + 1
    return memo[n]


starting_number = starting_length = 1
longest_chain_tuple = (starting_number, starting_length)

while starting_number < 1000000:
    starting_number += 1
    temp_length = recursive_collatz_sequence(starting_number)
    if temp_length > longest_chain_tuple[1]:
        longest_chain_tuple = (starting_number, temp_length)

toc = time.perf_counter()
print(longest_chain_tuple)
print(toc - tic)
