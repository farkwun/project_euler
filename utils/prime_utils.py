def load_primes(filename):
    f = open(filename, "r")
    primes = [int(line.strip()) for line in f]
    f.close()
    return primes
