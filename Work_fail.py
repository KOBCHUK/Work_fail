try:
    with open('MyDocument.txt', 'r') as _file:
        content = _file.read()
        words = content.split()
        numbers = []
        for word in words:
            try:
                number = float(word)
                numbers.append(number)
            except ValueError:
                pass
        print("The numbers contained in the file:", numbers)
except FileNotFoundError:
    print("Fail not found.")
finally:
    print("Done.")