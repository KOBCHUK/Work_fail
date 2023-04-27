try:
    with open('MyDocument.txt', 'r') as _file:
        content = _file.read()
        old_str = input ("Enter the string to be replaced: ")
        new_str = input("Enter the new line: ")
        new_content = content.replace(old_str, new_str)
    with open('MyDocument.txt', 'w') as _file:
        _file.write(new_content)
except FileNotFoundError:
    print("Fail not found.")
finally:
    print("Done")