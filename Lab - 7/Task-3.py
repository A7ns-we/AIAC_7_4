def write_hello():
    with open("example.txt", "w") as f:
        f.write("Hello, world!")

def write_two_files():
    with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
        f1.write("First file content\n")
        f2.write("Second file content\n")
    print("Files written successfully")

import os

def convert_input_to_upper():
    # Create input.txt with sample data if it doesn't exist
    if not os.path.exists("input.txt"):
        with open("input.txt", "w") as f:
            f.write("hello\nworld\n")
    with open("input.txt", "r") as f:
        data = f.readlines()
    with open("output.txt", "w") as output:
        for line in data:
            output.write(line.upper())
    print("Processing done")

def write_squares():
    squares = []
    # Create numbers.txt with sample data if it doesn't exist
    if not os.path.exists("numbers.txt"):
        with open("numbers.txt", "w") as f:
            f.write("1\n2\n3\n4\n5\n")
    with open("numbers.txt", "r") as f:
        nums = f.readlines()
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))
    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    print("Squares written")

# Run all
write_hello()
write_two_files()
convert_input_to_upper()
write_squares()


