try:
    file = open('Biografy.txt', 'r')
    content = file.read()
    if 'Yevhen Kobchuk' in content:
        print('Row found')
    else:
        print('Row not found')
except FileNotFoundError:
    print("Fail not found.")
except:
    print("Error.")
