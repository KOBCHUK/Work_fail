try:
    with open("MyDocument.txt", "r+") as f:
        lines = f.readlines()
        sorted_lines = sorted(lines)
        f.seek(0)
        f.truncate()
        for line in sorted_lines:
            f.write(line)
except Exception as e:
    print(e)
    print("Error")
finally:
    print("Finally")