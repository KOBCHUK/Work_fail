try:
    line_number = int(input("Enter number the line: "))
    with open("MyDocument.txt", "r+") as f:
        lines = f.readlines()
        print(lines[line_number - 1])
        f.seek(0)
        f.truncate()
        for line in lines:
            if line != lines[line_number - 1]:
                f.write(line)
except Exception as e:
    print(e)
    print("Error")
finally:
    print("Finally")
