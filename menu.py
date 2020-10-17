import os
import datetime

def print_menu():
    print("_" * 43)

    print("Warehouse control   " + "[" + get_date_time() + "]")
    print("_" * 43)

    print('[1] Register new item')
    print('[2] Display catalog')
    print('[3] Display items out of stock')
    print('[4] Stock value')
    print('[5] Update price')
    print('[6] Delete item')
    print('[7] Update item stock')
    print('[8] Display category')
    print('[9] Cheapest product')
    print('[10] 3 most expensive products')

    print('[x] Close')


def get_date_time():
    now = datetime.datetime.now()
    return now.strftime("%b/%d/%Y %T")

def clear():
    command = 'clear'
    if (os.name == 'nt'):
        command = 'cls'
    return os.system(command)


def print_item(item):
    print(
        str(item.id).ljust(2) + " | " + item.title.ljust(12) + " | " +
        item.category.ljust(10) + " | " + str(item.stock) + " | " + '$' +
        str(item.price))


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