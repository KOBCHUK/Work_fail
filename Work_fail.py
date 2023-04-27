try:
    with open("MyDocument.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        unique_lines = set(lines)
        if len(lines) != len(unique_lines):
            print("The file has duplicate lines.")
        else:
            print("There are no duplicate lines in the file.")
except Exception as e:
    print(e)
    print("Error")
finally:
    print("Done")