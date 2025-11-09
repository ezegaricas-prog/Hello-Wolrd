def main():
    filename = input("Enter the name of a text file: ")
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")

    print("This file has", len(lines), "lines.")

    line_number = int(input("Enter a line number (0 to quit): "))
    while line_number != 0:
        if line_number >= 1 and line_number <= len(lines):
            print("Line", line_number, ":", lines[line_number - 1])
        else:
            print("Invalid line number.")
        line_number = int(input("Enter a line number (0 to quit): "))

    print("Goodbye!")

main()
