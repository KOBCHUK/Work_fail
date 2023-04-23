try:
  _file = open('filename.txt', 'r')
  content = _file.read()
  print(content)
except FileNotFoundError:
    print("Fail not found.")
except:
    print("Error.")