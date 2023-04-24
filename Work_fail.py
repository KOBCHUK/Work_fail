try:
    with open('MyDocument.txt', 'r') as _file:
        content = _file.read()
        lines = content.split('\n')
        search_word = input("Enter world for search: ")
        matching_lines = [line for line in lines if search_word in line]
        print("Lines containing the word '", search_word, "':", sep='')
        for line in matching_lines:
            print(line)
except FileNotFoundError:
    print("Fail not found.")
finally:
    print("Program finished.")