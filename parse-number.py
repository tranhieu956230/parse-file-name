import os
from os import listdir
from os.path import isfile, join
import sys
import re

path = sys.argv[1] or "./"

def is_format(file, format):
    return re.search(f'.{format}$', file)

def main():
    mp4_files = [file for file in listdir(path) if isfile(join(path, file)) and is_format(file, "mp4")]
    numbers = []

    for file in mp4_files:
        number = int(file.split(".")[0])
        numbers.append(number)

    max_number = max(numbers)
    max_digit = len(str(max_number))

    for i in range(len(mp4_files)):
        old_name = mp4_files[i]
        split = old_name.split(".")
        split[0] = "0" * (max_digit - len(str(numbers[i]))) + str(numbers[i])
        new_name = ".".join(split)
        os.rename(join(path, old_name), join(path, new_name))

if __name__ == "__main__":
    main()
