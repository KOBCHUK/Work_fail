try:
  file = open('filename.txt', 'r')
  content = file.read()
  print(content)
except FileNotFoundError:
    print("Fail not found.")
except:
    print("Error.")