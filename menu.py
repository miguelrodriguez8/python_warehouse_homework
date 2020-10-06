import os

def print_menu():
    print("_" * 30)

    print("Warehouse control")
    print("_" * 30)

    print('[1] Register new item')
    print('[2] Display catalog')
    print('[3] Display items out of stock')
    print('[4] Stock value')


    print('[x] Close')

def clear():
    command = 'clear'
    if(os.name == 'nt'):
        command = 'cls'
    return os.system(command)
    


def print_item(item):
    print(str(item.id) + " | " + item.title + " | " + item.category + " | " + str(item.stock) + " | " + str(item.price))

def print_header(title):
    clear()
    print("_" * 50)
    print(title)
    print("_" * 50)


"""
1 - finish opc 4
2 - clear the screen
3 - Inv what is object serialization
"""