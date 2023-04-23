try:
    with open('MyDocument.txt', 'r') as file:
        content = file.read()
        old_str = input "Enter the string to be replaced "
        new_str = "New line"
        new_content = content.replace(old_str, new_str)
    with open('MyDocument.txt', 'w') as file:
        file.write(new_content)
except FileNotFoundError:
    print("Fail not found.")
finally:
    print("Done")