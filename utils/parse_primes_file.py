# lists of primes can be found at: https://primes.utm.edu/lists/small/millions/

count = 0

filename = "primes1"
extension = ".txt"

output_file = filename + "_processed" + extension

f = open("primes1.txt", "r")

primes = []

for line in f:
    line_arr = line.split()
    if line_arr and line_arr[0].isnumeric():
        primes += line_arr

f.close()

o = open(output_file, "a")
for p in primes:
    o.write(p + "\n")

o.close()
