import time
import sys

sys.path.append(".")

# if importing below sys:
# from utils.prime_utils import load_primes  # noqa: E402

tic = time.perf_counter()

NUM_DICT = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def get_word_version_of(number_str):
    word_arr = []
    if not number_str:
        return [""]

    if all(c == "0" for c in number_str):
        return [""]

    if len(number_str) == 4:
        word_arr.append(NUM_DICT[1000])

    if len(number_str) == 3:
        word_arr.append(NUM_DICT[100])

    if len(number_str) <= 2:
        num = int(number_str)
        if num <= 20:
            word_arr.append(NUM_DICT[num])
        else:
            word_arr.append(NUM_DICT[int(number_str[0] + "0")])
            word_arr += get_word_version_of(number_str[1:])
        return word_arr

    word_arr.append(NUM_DICT[int(number_str[0])])
    new_words = get_word_version_of(number_str[1:])
    if "".join(new_words):
        if len(number_str) == 3:
            word_arr.append("and")
        word_arr += new_words

    return word_arr


sum_ = 0

for i in range(1001):
    word_version = get_word_version_of(str(i))
    sum_ += len("".join(word_version))


print(sum_)

toc = time.perf_counter()
print(toc - tic)
