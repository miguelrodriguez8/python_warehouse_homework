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
last_id = 0
data_file = 'warehouse.data'


#functions

def serialize_catalog():
    global data_file
    writer = open(data_file, 'wb') # wb will create/overwrite the file
    pickle.dump(catalog, writer)
    writer.close()
    print('Data saved!')

def deserialize_catalog():
    global data_file
    global last_id
    try:
        reader = open(data_file, 'rb') # rb will read the binary file/ throw exception if file doesn't exist
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1]
        last_id = last_id + 1
        how_many = len(catalog)
        print(' Deserialized ' + str(how_many) + ' items')

    except:
        print('Error, no data loaded')
 
def register_item():
    clear()
    global last_id
    try:
        print_header("Register new Item")
        title = input('Please provide the title: ')
        category = input ('Name the category: ')
        stock = int(input('Please provide the stock: '))
        price = float(input('Please provide the Price: '))

        the_item = Item(last_id, title, category, stock, price)
        last_id += 1
        # add the obj to the list
        catalog.append(the_item)

        count = len(catalog)
        print('Item saved, you have ' + str(count) + ' items in your catalog')

    except ValueError:
         print('*Error. Provide valid numbers')    
    except:
         print('*Wrong entry. Please try again')


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

def update_price():
    display_catalog()
    id = input("select the Id number: ")
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            price = float(input('Provide new price $'))
            item.price = price

    if(not found):
        print("*Error, invalid ID Please Try Again.")        





   




def delete_item():
    display_catalog()
    id = input("select the Id number: ")
    found = False
    for item in catalog:
        if(str(item.id) == id):
            found = True
            del catalog[int(id)]
            print('*Item has been removed')

    if(not found):
        print("*Error, invalid ID Please Try Again.") 

       

 

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

    elif(opc == '5'):
        update_price()
        serialize_catalog()

    elif(opc == '6'):
        delete_item()
        serialize_catalog()    

    input('Press Enter to continue...')    


""""
-show the catalog
-ask the user to choose an id
-find the id in the catalog
-  ask for the new price
-  set the price
-else, show an error
"""  

  