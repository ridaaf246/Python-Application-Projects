import random
import string

word = input("Enter word: ")

reverse = word[::-1]

start = ''.join(random.choices(string.ascii_lowercase, k=3))
end = ''.join(random.choices(string.ascii_lowercase, k=3))

encode = start + reverse + end

# ENCODE #
if len(word) <= 3:
    print("Encoded:", reverse)
else:
    print("Encoded:", encode)


# DECODE #
if len(encode) <= 3:
    print("Decoded:", encode[::-1])
else:
    print("Decoded:", encode[3:-3][::-1])