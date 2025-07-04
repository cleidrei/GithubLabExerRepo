filename = input("Enter the filename: ")

try:
    lines = open(filename).readlines()
except:
    print("File not found.")
    exit()

print("The file has", len(lines), "lines.")

while True:
    line = input("Enter a line number (0 to quit): ")

    if line == "0":
        break
    if line.isdigit():
        num = int(line)
        if 1 <= num <= len(lines):
            print("Line", num, ":", lines[num - 1].strip())
        else:
            print("Invalid line number.")
    else:
        print("Please enter a number.")
