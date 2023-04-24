try:
    _file = open('Biografy.txt', 'r')
    content = _file.read()
    if 'Yevhen Kobchuk' in content:
        print('Row found')
    else:
        print('Row not found')
except FileNotFoundError:
    print("Fail not found.")
except:
    print("Error.")
