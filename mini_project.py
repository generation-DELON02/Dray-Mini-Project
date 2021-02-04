products = []
couriers = []
order_1 = {'Name' : 'Andre L', 'Address' : '29 Holland Road, London', 'Postcode' : 'NW10 5AH', 'Contact Number' : '07931647479', 'Courier' : '2', 'Status' : 'Preparing'}
order_2 = {'Name' : 'Victoire C', 'Address' : '42 Cadogan Square, London', 'Postcode' : 'SW1 0HX', 'Contact Number' : '07800996960', 'Courier' : '3', 'Status' : 'Preparing'}
orders = [order_1, order_2]

def start_app():
    print("\nWelcome to the London Region Anti Coffee Pop Up Café Business App")
    populate_product_list()
    populate_courier_list()
    main_menu()

def exit_app():
    update_products_txt_file()
    update_couriers_txt_file()
    exit('\nExiting the app.')

def clear():
    print('\n'*3)

def incorrect_command():
    clear()
    print("Sorry, we did not recognise the input! Please enter an appropriate command.")

def populate_product_list():
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.txt') as product_list_file:
            for line in product_list_file.readlines():
                products.append(line.rstrip())
    except Exception as e:
        print('An error occurred when attempting to update the Product List: ' + str(e))

def populate_courier_list():
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.txt') as courier_list_file:
            for line in courier_list_file.readlines():
                couriers.append(line.rstrip())
    except Exception as e:
        print('An error occurred when attempting to update the Courier List: ' + str(e))

def update_products_txt_file():
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.txt', 'w') as product_list_file:
            for product in products:
                product_list_file.write(product + '\n')
    except Exception as e:
        print('An error occurred when attempting to update the product list text file: ' + str(e))

def update_couriers_txt_file():
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.txt', 'w') as courier_list_file:
            for name in couriers:
                courier_list_file.write(name + '\n')
    except Exception as e:
        print('An error occurred when attempting to update the courier list text file: ' + str(e))

def product_list():
    clear()
    while True:
        print(f'Product List:\n{products}')    ###Maybe def a for loop (to print out the list 'à la ligne' per element)
        user_input = input("\nEnter '0' to return to Product Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            product_menu()
            break
        else:
            incorrect_command()

def courier_list():
    clear()
    while True:
        print(f'Courier List:\n{couriers}')    ###Maybe def a for loop (to print out the list 'à la ligne' per element) #SEE 143 (in add_order function)
        user_input = input("\nEnter '0' to return to Courier Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            courier_menu()
            break
        else:
            incorrect_command()

def order_list():
    clear()
    while True:
        print_order_list()
        user_input = input("\nEnter '0' to return to Order Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            order_menu()
            break
        else:
            incorrect_command()

def print_order_list():
    print('Order List:\n')
    n = 1
    for order in orders:
        print(f'- {n} -')
        n += 1
        for key, value in order.items():
            print(f'{key}: {value}')
        print('\n')

def add_product():
    clear()
    user_input = input("Which product(s) would you like to add to your Product List?\n(Note: if adding multiple products, please seperate them with commas. Be aware that any input will add to your Product List!)\nIf you would not like to add to your Product List, enter '0' to cancel & return to Product Menu: ")
    if user_input == '0':
        product_menu()
    else:
        products.extend(user_input.title().split(', '))    #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        print(f'\nSuccessfully added: {user_input.title()}')
        product_menu()

def add_courier():
    clear()
    user_input = input("Which courier(s) would you like to add to your Courier List?\n(Note: if adding multiple couriers, please seperate them with commas. Be aware that any input will add to your Courier List!)\nIf you would not like to add to your Courier List, enter '0' to cancel & return to Courier Menu: ")
    if user_input == '0':
        courier_menu()
    else:
        couriers.extend(user_input.title().split(', '))    #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        print(f'\nSuccessfully added: {user_input.title()}')
        courier_menu()

def add_order():
    clear()
    user_input_1 = input("(Note: Please be aware that any input will add information for your new order)\nIf you would not like to add a new order, enter '0' to cancel new order & return to Order Menu\nOtherwise, what is the name of the customer your will assign the new order to? ")
    if user_input_1 == '0':
        order_menu()
    else:
        new_order = {'Name' : '', 'Address' : '', 'Postcode' : '', 'Contact Number' : '', 'Courier': '', 'Status': ''}
    new_order['Name'] = user_input_1.title()
    user_input_2 = input("What is the address for the order? ")
    new_order['Address'] = user_input_2.title()
    user_input_3 = input("What is the post code for the order? ")
    new_order['Postcode'] = user_input_3.upper()
    user_input_4 = input("What is the customer's contact number? ")
    new_order['Contact Number'] = user_input_4
    print(f'\nCourier List:\n{couriers}')
    user_input_5 = input("Please select a courier from the list above\nPlease enter the number of the position of the courier. (e.g. To select the third courier, enter 3) ")    ###CHANGE to name of courier instead if need be
    new_order['Courier'] = user_input_5
    new_order['Status'] = 'Preparing'
    print('\n')
    for key, value in new_order.items():
        print(f'{key}: {value}')
    print("\nThe new order has successfully been added to your Order List")
    orders.append(new_order)
    order_menu()

def change_order_status_order_selection():
    clear()
    while True:
        print_order_list()
        try:
            user_input_1 = int(input("Which order would you like to change the status of?\nPlease enter the number of the order.\nEnter '0' to cancel update & return to Order Menu: "))
            selected_order = orders[user_input_1 - 1]
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            order_menu()
            break
        print('\nSelected order:\n')
        for key, value in selected_order.items():
            print(f'{key}: {value}')
        change_order_status_status_selection(selected_order)

def change_order_status_status_selection(selected_order):
    while True:
        print('\nWhat would you like to update the order status to?')
        user_input_2 = input("\nEnter '1' for 'Preparing'\nEnter '2' for 'Ready for collection'\nEnter '3' for 'Out for delivery'\nEnter '4' for 'Delivered': ")
        if user_input_2 == '1':
            new_status = 'Preparing'
        elif user_input_2 == '2':
            new_status = 'Ready For Collection'
        elif user_input_2 == '3':
            new_status = 'Out For Delivery'
        elif user_input_2 == '4':
            new_status = 'Delivered'
        else:
            incorrect_command()
            continue
        selected_order['Status'] = new_status
        print('\nOrder status succesfully updated:\n')
        for key, value in selected_order.items():
            print(f'{key}: {value}')
        order_menu()
        break

def replace_product():
    clear()
    while True:
        print(f'Product List:\n{products}')    ###Maybe def a for loop (to print out the list 'à la ligne' per element)
        try:
            user_input_1 = int(input("\nWhich product would you like to replace?\nPlease enter the number of the position of the product. (e.g. To replace the third product, enter 3)\nEnter '0' to cancel update & return to Product Menu: "))     #FIND how to replace several at once? Same as adding several?
            print(f'\nSelected product: {products[user_input_1 - 1]}')     ###DEF SELECTED PRODUCT/COURIER FUNCTION?
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            product_menu()
            break
        user_input_2 = input('\nWhat would you like to replace the product with? ')
        print(f'\n{products[user_input_1 - 1]} has sucessfully been replaced with {user_input_2.title()}.')    #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        products[user_input_1 - 1] = user_input_2.title()
        product_menu()
        break

def replace_courier():
    clear()
    while True:
        print(f'Courier List:\n{couriers}')    ###Maybe def a for loop (to print out the list 'à la ligne' per element)
        try:
            user_input_1 = int(input("\nWhich courier would you like to replace?\nPlease enter the number of the position of the courier. (e.g. To replace the third courier, enter 3)\nEnter '0' to cancel update & return to Courier Menu: "))     #FIND how to replace several at once? Same as adding several?
            print(f'\nSelected courier: {couriers[user_input_1 - 1]}')     ###DEF SELECTED PRODUCT/COURIER FUNCTION?
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            courier_menu()
            break
        user_input_2 = input('\nWhat would you like to replace the selected courier with? ')
        print(f'\n{couriers[user_input_1 - 1]} has sucessfully been replaced with {user_input_2.title()}.')    #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        couriers[user_input_1 - 1] = user_input_2.title()
        courier_menu()
        break

def delete_product(): 
    clear()
    while True:
        print(f'Product List:\n{products}')
        try:
            user_input = int(input("\nWhich product would you like to remove from your Product List?\nPlease enter the number of the position of the product. (e.g. To remove the third product, enter 3)\nEnter '0' to cancel deletion & return to Product Menu: "))    #FIND how to delete several at once? Same as adding several?
            products[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            product_menu()
            break
        confirm_delete_product(user_input)
        break

def confirm_delete_product(product_index):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {products[product_index - 1]} from your Product List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
            product_menu()
            break
        elif user_input == '1':
            clear()
            print(f'\n{products[product_index - 1]} has successfully been removed from your Product List.')
            del products[product_index - 1]
            product_menu()
            break
        else:
            incorrect_command()

def delete_courier():
    clear()
    while True:
        print(f'Courier List:\n{couriers}')
        try:
            user_input = int(input("\nWhich courier would you like to remove from your Courier List?\nPlease enter the number of the position of the courier. (e.g. To remove the third courier, enter 3)\nEnter '0' to cancel deletion & return to Courier Menu: "))    #FIND how to delete several at once? Same as adding several?
            couriers[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
            break
        confirm_delete_courier(user_input)
        break

def confirm_delete_courier(courier_index):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {couriers[courier_index - 1]} from your Courier List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
            courier_menu()
            break
        elif user_input == '1':
            clear()
            print(f'\n{couriers[courier_index - 1]} has successfully been removed from your Courier List.')
            del couriers[courier_index - 1]
            courier_menu()
            break
        else:
            incorrect_command()

def product_menu():
    clear()
    while True:
        print('PRODUCT MENU')
        user_input = input("\nEnter '1' to view your Product List\nEnter '2' to add a product to your Product List\nEnter '3' to update your Product List by replacing a product with a new one\nEnter '4' to delete a product from your Product List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
            break
        elif user_input == '1':
            product_list()
            break
        elif user_input == '2':
            add_product()
            break
        elif user_input == '3':
            replace_product()
            break
        elif user_input == '4':
            delete_product()
            break
        else:
            incorrect_command()

def courier_menu():
    clear()
    while True:
        print('COURIER MENU')
        user_input = input("\nEnter '1' to view Courier List\nEnter '2' to add a courier to your Courier List\nEnter '3' to update your Courier List by replacing a courier with a new one\nEnter '4' to delete a courier from your Courier List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
            break
        elif user_input == '1':
            courier_list()
            break
        elif user_input == '2':
            add_courier()
            break
        elif user_input == '3':
            replace_courier()
            break
        elif user_input == '4':
            delete_courier()
            break
        else:
            incorrect_command()

def order_menu():
    clear()
    while True:
        print('ORDER MENU')
        user_input = input("\nEnter '1' to view your Order List\nEnter '2' to add a new order to your Order List\nEnter '3' to change the Order Status of an order\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
            break
        elif user_input == '1':
            order_list()
            break
        elif user_input == '2':
            add_order()
            break
        elif user_input == '3':
            change_order_status_order_selection()
        else:
            incorrect_command()
        
def main_menu():
    while True:
        user_input = input("\nMAIN MENU\n\nEnter '1' to view the Product Menu\nEnter '2' to view the Courier Menu\nEnter '3' to view the Order Menu\nEnter '0' to exit the app: ")
        if user_input == '0':
            exit_app()
        elif user_input == '1':
            product_menu()
            break
        elif user_input == '2':
            courier_menu()
            break
        elif user_input == '3':
            order_menu()
            break
        else:
            incorrect_command()

start_app()

### ADD populate lists & update txt files functions throughout code?
### REFER to products & courier lists by index or name - CONSISTENCY - use n += 1 with for loop
### CHANGE populate lists & update txt files functions (to have one of each &) to take arguments depending on if they're used for products or couriers. (vs two seperate functions for populating or for updating txt files)

#lil useless change

### Move clear() to bottom/end of functions
### Make code even cleaner. Add functions to simplify each one