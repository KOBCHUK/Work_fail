try:
    with open('MyDocument.txt', 'r') as file:
        content = file.read()
        lines = content.split('\n')
        n = int(input("Enter quantity lines: "))
        print("Last", n, "lines:")
        for line in lines[-n:]:
            print(line)
except FileNotFoundError:
    print('Fail not found')
finally:
    print("Done")



