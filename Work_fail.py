try:
    _file = open('MyDocument.txt', 'r')
    content = _file.read()
    words = content.split()
    num_words = len(words)
    print('Number of words on the screen:', num_words)
except Exception as e:
    print("Fail not found.")
finally:
    print("End programm.")
