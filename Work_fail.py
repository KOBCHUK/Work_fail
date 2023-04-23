try:
  
    with open('filename.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Fail not found.")
except:
    print("Error.")