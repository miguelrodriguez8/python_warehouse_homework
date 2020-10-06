"""
Program: Warehouse control
Author: Miguel Rodriguez
Functionality:
    -Register Items
        -id (auto generated): integer
        -title: str
        -category: str
        -stock: integer
        -price: float

"""


#imports
from menu import print_menu, clear, print_item, print_header
from item import Item
import pickle




#global vars

catalog = []



#functions

def serialize_catalog():
    writer = open('warehouse.data', 'wb') # wb will create/overwrite the file
    pickle.dump(catalog, writer)
    writer.close()
    print('Data saved!')

def deserialize_catalog():
    reader = open('warehouse.data', 'rb') # rb will read the binary file/ throw exception if file doesn't exist
    temp_list = pickle.load(reader)

    for item in temp_list:
        catalog.append(item)

    how_many = len(catalog)
    print(' Deserialized ' + str(how_many) + ' items')


def register_item():
    clear()
    print_header("Register new Item")
    title = input('Please provide the title: ')
    category = input ('Name the category: ')
    stock = int(input('Please provide the stock: '))
    price = float(input('Please provide the Price: '))

    the_item = Item(1, title, category, stock, price)
    # add the obj to the list
    catalog.append(the_item)

    count = len(catalog)
    print('Item saved, you have ' + str(count) + ' items in your catalog')


def display_catalog():
    print_header("Your catalog")
    for item in catalog:
        print_item(item)

def display_out_of_stock():
    print_header("Items out of stock")
    for item in catalog:
        if(item.stock == 0):
            print_item(item)        

def total_stock_value():
    print_header("Total stock value")
    total = 0.0
    for item in catalog:
        total += item.stock * item.price

    print('The total is: $' + str(total))


#instructions
deserialize_catalog()
input('Press Enter to continue...')


opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input ('Please select an option: ')

    if(opc =='1'):
        register_item()
        serialize_catalog()

    elif(opc == '2'):
        display_catalog()
    
    elif(opc == '3'):
        display_out_of_stock()

    elif(opc == '4'):
        total_stock_value()


    input('Press Enter to continue...')    

