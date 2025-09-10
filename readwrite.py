#Write initial text
with open('pqr.txt', 'w') as file:
    file.write('Hello World!')

#Read the file
with open('pqr.txt', 'r') as file:
    content = file.read()
    print("After writing:")
    print(content)

# Append new line
with open('pqr.txt', 'a') as file:
    file.write('\nThis is new line')

#Read again
with open('pqr.txt', 'r') as file:
    content = file.read()
    print("\nAfter appending:")
    print(content)

# Append content from pqr.txt to xyz.txt
with open('xyz.txt', 'a') as file_xyz, open('pqr.txt', 'r') as file_pqr:
    content_pqr = file_pqr.read()
    file_xyz.write(content_pqr)
    print("\nContent from pqr.txt appended to xyz.txt:")
    print(content_pqr)

# Using r+ mode (Read + Write)
with open('pqr.txt', 'r+') as file:
    content = file.read()
    print("\nUsing r+ mode (before writing):")
    print(content)
    file.write("\nDYPCET")
    file.seek(0)
    content = file.read()
    print("Using r+ mode (after writing):")
    print(content)

# Using w+ mode (Write + Read, overwrite)
with open('pqr.txt', 'w+') as file:
    file.write("Overwriting content using w+ mode")
    file.seek(0)
    content = file.read()
    print("\nUsing w+ mode:")
    print(content)

# Using a+ mode (Append + Read)
with open('pqr.txt', 'a+') as file:
    file.write("\nAppending new line using a+ mode")
    file.seek(0)
    content = file.read()
    print("\nUsing a+ mode:")
    print(content)

# Read first 10 bytes
with open("pqr.txt", "r") as file:
    first_10_bytes = file.read(10)
    print("\nFirst 10 bytes of pqr.txt:")
    print(first_10_bytes)

# Current position of file pointer after reading 5 bytes
with open("pqr.txt", "r") as file:
    file.read(5)
    position = file.tell()
    print("\nCurrent position of file pointer after reading 5 bytes:")
    print(position)

#read first two lines
with open("pqr.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()
    print("\nFirst two lines of pqr.txt:")
    print(first_line.strip())
    print(second_line.strip())