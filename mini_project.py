products = [{'Name' : 'Pandan Cake', 'Price' : 2.5}, {'Name' : 'Chouquettes', 'Price' : 1.0}, {'Name' : 'Thai Iced Tea', 'Price' : 2.0}, {'Name' : 'Hot Chocolate', 'Price' : 1.5}]
couriers = [{'Name' : 'Dillon', 'Contact Number' : '07931647478'}, {'Name' : 'Oscar', 'Contact Number' : '07800996961'}, {'Name' : 'Saskia', 'Contact Number' : '07931468682'}]
order_1 = {'Name' : 'Andre L', 'Address' : '29 Holland Road, London, NW10 5AH', 'Contact Number' : '07931647479', 'Courier' : 2, 'Status' : 'Preparing', 'Items' : [1, 2, 3]}
order_2 = {'Name' : 'Victoire C', 'Address' : '42 Cadogan Square, London, SW1 0HX', 'Contact Number' : '07800996960', 'Courier' : 3, 'Status' : 'Preparing', 'Items' : [1, 4]}
orders = [order_1, order_2]

def start_app():
    print("\nWelcome to the London Region Anti Coffee Pop Up Café Business App")
    #populate_product_list()
    #populate_courier_list()
    main_menu()

def exit_app():
    #update_products_txt_file()
    #update_couriers_txt_file()
    exit('\nExiting the app.')

def clear():
    print('\n'*3)

def incorrect_command():
    clear()
    print("Sorry, we did not recognise the input! Please enter an appropriate command.")
    print('\n')

# def populate_product_list():
#     try:
#         with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.txt') as product_list_file:
#             for line in product_list_file.readlines():
#                 products.append(line.rstrip())
#     except Exception as e:
#         print('An error occurred when attempting to update the Product List: ' + str(e))

# def populate_courier_list():
#     try:
#         with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.txt') as courier_list_file:
#             for line in courier_list_file.readlines():
#                 couriers.append(line.rstrip())
#     except Exception as e:
#         print('An error occurred when attempting to update the Courier List: ' + str(e))

# def update_products_txt_file():
#     try:
#         with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.txt', 'w') as product_list_file:
#             for product in products:
#                 product_list_file.write(product + '\n')
#     except Exception as e:
#         print('An error occurred when attempting to update the product list text file: ' + str(e))

# def update_couriers_txt_file():
#     try:
#         with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.txt', 'w') as courier_list_file:
#             for name in couriers:
#                 courier_list_file.write(name + '\n')
#     except Exception as e:
#         print('An error occurred when attempting to update the courier list text file: ' + str(e))

def product_list():
    clear()
    while True:
        print_product_list()
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
        print_courier_list()
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

#def print_product_list():
#    print('Product List:\n')
#    for product in products:
#        for key, value in product.items():
#            print(f'{key}: {value}')

def print_product_list():
    print('Product List:\n')
    for count, value in enumerate(products, 1):
        print(f'{count}: {value}')

#def print_courier_list():
#    print('Courier List:\n')
#    for courier in couriers:
#        for key, value in courier.items():
#            print(f'{key}:  {value}')

def print_courier_list():
    print('Courier List:\n')
    for count, value in enumerate(couriers, 1):
        print(f'{count}: {value}')

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
    while True:
        user_input_1 = input("ADD PRODUCT\n\nWhich product would you like to add to the Product List?\n(Note: Be aware that any input will add to the list!)\nIf you would not like to add to the Product List, enter '0' to cancel & return to Product Menu: ")
        if user_input_1 == '0':
            product_menu()
            break
        new_product = {'Name' : '', 'Price' : float}
        new_product['Name'] = user_input_1.title()                #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        try:
            user_input_2 = float(input("What is the price of this item? "))
        except:
            incorrect_command()
            continue
        new_product['Price'] = user_input_2
        print('\nThe following item was successfully added to the Product List:')
        for key, value in new_product.items():
            print(f'{key}: {value}')
        products.append(new_product)
        product_menu()
        break

def add_courier():
    clear()
    while True:
        user_input_1 = input("ADD COURIER\n\nWhat is the name of the courier you would like to add to the Courier List?\n(Note: Be aware that any input will add to the Courier List!)\nIf you would not like to add to the Courier List, enter '0' to cancel & return to Courier Menu: ")
        if user_input_1 == '0':
            courier_menu()
            break
        new_courier = {'Name' : '', 'Contact Number' : ''}
        new_courier['Name'] = user_input_1.title()                #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        try:
            user_input_2 = input("What is the courier's contact number? ")      #Is there a way to account for incorrect number/input?
        except:
            incorrect_command()
            continue
        new_courier['Contact Number'] = user_input_2
        print('\nThe following courier was successfully added to the Product List:')
        for key, value in new_courier.items():
            print(f'{key}: {value}')
        couriers.append(new_courier)
        courier_menu()
        break

def add_order():
    clear()
    user_input_1 = input("ADD ORDER\n\nWhat is the name of the customer you wish to assign the new order to? (Note: Please be aware that any input in the next few steps will add information for your new order.)\nIf you would not like to add a new order, enter '0' to cancel new order & return to Order Menu: ")
    if user_input_1 == '0':
        order_menu()
    new_order = {'Name' : '', 'Address' : '', 'Contact Number' : '', 'Courier': '', 'Status': 'Preparing', 'Items' : []}
    new_order['Name'] = user_input_1.title()
    user_input_2 = input("What is the full address for the order? ")
    new_order['Address'] = user_input_2.title()
    user_input_4 = input("What is the customer's contact number? ")
    new_order['Contact Number'] = user_input_4
    add_order_product(new_order)
    add_order_another_product(new_order)
    add_order_courier(new_order)
    print('\n')
    for key, value in new_order.items():
        print(f'{key}: {value}')
    print("\nThe new order has successfully been added to the Order List.")
    orders.append(new_order)
    order_menu()

def add_order_product(new_order):
    while True:
        print('\n')
        print_product_list()
        try:
            user_input = int(input("\nSelect a product from the list to add to the new order. Please enter the listing number before the desired product: "))
            products[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            incorrect_command()
            continue
        break
    new_order['Items'].append(user_input)

def add_order_another_product(new_order):
    while True:
        print('\n')
        print_product_list()
        try:
            user_input = int(input("\nSelect another product to add to the new order if you would like. Please enter the listing number before the desired product.\nEnter '0' to not add another product: "))
            products[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            break
        new_order['Items'].append(user_input)
    new_order['Items'].sort()

def add_order_courier(new_order):
    while True:
        print('\n')
        print_courier_list()
        try:
            user_input = int(input("\nSelect a courier from the list above.\nPlease enter the listing number before the desired courier: "))
            couriers[user_input - 1]    
        except:
            incorrect_command()
            continue
        if user_input == 0:
            incorrect_command()
            continue
        break
    new_order['Courier'] = user_input

def change_order_status_order_selection():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(input("Which order would you like to change the status of?\nPlease enter the number of the desired order.\nEnter '0' to cancel update & return to Order Menu: "))
            selected_order = orders[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
            break
        print('\nSelected order:\n')
        for key, value in selected_order.items():
            print(f'{key}: {value}')
        change_order_status_status_selection(selected_order)

def change_order_status_status_selection(selected_order):
    while True:
        print('\nWhat would you like to update the order status to?')
        user_input = input("\nEnter '1' for 'Preparing'\nEnter '2' for 'Ready for collection'\nEnter '3' for 'Out for delivery'\nEnter '4' for 'Delivered': ")
        if user_input == '1':
            new_status = 'Preparing'
        elif user_input == '2':
            new_status = 'Ready For Collection'
        elif user_input == '3':
            new_status = 'Out For Delivery'
        elif user_input == '4':
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
        print('\n')
        print_product_list()
        try:
            user_input_1 = int(input("\nWhich product would you like to replace?\nPlease enter the listing number before the desired product.\nEnter '0' to cancel update & return to Product Menu: "))
            selected_product = products[user_input_1 - 1]
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            product_menu()
            break
        print(f'\nSelected product:')
        for key, value in selected_product.items():
            print(f'{key}: {value}')
        user_input_2 = input('\nWhat would you like to replace the product with? ')
        new_product_name = user_input_2.title()           #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        try:
            new_product_price = float(input('What is the price of this item? '))
        except:
            incorrect_command()
            continue
        print('\n' + selected_product['Name'] + f' has successfully been replaced with {new_product_name} at price {new_product_price}.')
        selected_product['Name'] = new_product_name
        selected_product['Price'] = new_product_price
        product_menu()
        break

def replace_courier():
    clear()
    while True:
        print('\n')
        print_courier_list()
        try:
            user_input_1 = int(input("\nWhich courier would you like to replace?\nPlease enter the listing number before the desired courier.\nEnter '0' to cancel update & return to Courier Menu: "))
            selected_courier = couriers[user_input_1 - 1]
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            courier_menu()
            break
        print(f'\nSelected courier:')
        for key, value in selected_courier.items():
            print(f'{key}: {value}')
        user_input_2 = input('\nWho would you like to replace the courier with? ')
        new_courier_name = user_input_2.title()           #Problem with .title(): capitalises letters after ' & lowercases caps in the middle of words
        try:
            new_courier_number = input("What is the new courier's contact number? ")
        except:
            incorrect_command()
            continue
        print('\n' + selected_courier['Name'] + f' has successfully been replaced with {new_courier_name} and {new_courier_number} as their contact number.')
        selected_courier['Name'] = new_courier_name
        selected_courier['Contact Number'] = new_courier_number
        courier_menu()
        break

def replace_order_values():
    clear()
    while True:
        print('\n')
        print_order_list()
        try:
            user_input = int(input("Which order would you like to update?\nPlease enter the number of the desired order.\nEnter '0' to cancel update & return to Order Menu: "))
            selected_order = orders[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
            break
        print('\nSelected order:\n')
        for key, value in selected_order.items():
            print(f'{key}: {value}')
        print('\n')
        replace_order_value_name(selected_order)
        break
    print('\nOrder succesfully updated:\n')
    for key, value in selected_order.items():
        print(f'{key}: {value}')
    order_menu()

def replace_order_value_name(selected_order):
    user_input = input("What would you like to replace the customer's name associated to the order to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['Name'] = user_input.title()
    replace_order_value_address(selected_order)

def replace_order_value_address(selected_order):
    user_input = input("What would you like to replace the customer's address to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['Address'] = user_input.title()
    replace_order_value_contact_number(selected_order)

def replace_order_value_contact_number(selected_order):
    user_input = input("What would you like to replace the customer's contact number to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['Contact Number'] = user_input
    replace_order_value_courier(selected_order)

def replace_order_value_courier(selected_order):
    while True:
        print('\n')
        print_courier_list()
        user_input = input("\nSelect a courier from the list above to allocate to the order.\nPlease enter the listing number before the desired courier.\nLeave blank & press Enter to skip updating this piece of information: ")
        if user_input == "":
            replace_order_value_adding_product(selected_order)
        try:
            user_input_int = int(user_input)
            couriers[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        break
    selected_order['Courier'] = user_input_int
    replace_order_value_adding_product(selected_order)

def replace_order_value_adding_product(selected_order):
    while True:
        print('\n')
        print_product_list()
        user_input = input("\nWhich product would you like to add to the order?\nPlease enter the listing number before the desired product.\nLeave blank & press Enter to skip adding products to the order: ")
        if user_input == "":
            replace_order_value_removing_product(selected_order)
        try:
            user_input_int = int(user_input)
            products[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        break
    selected_order['Items'].append(user_input_int)
    replace_order_value_adding_another_product(selected_order)

def replace_order_value_adding_another_product(selected_order):
    while True:
        print('\n')
        print_product_list()
        user_input = input("\nIf you would like to add another product to the order, please enter the listing number before the desired product.\nLeave blank & press Enter to skip adding more products to the order: ")
        if user_input == "":
            selected_order['Items'].sort()
            replace_order_value_removing_product(selected_order)
            break
        try:
            user_input_int = int(user_input)
            products[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        selected_order['Items'].append(user_input_int)

def replace_order_value_removing_product(selected_order):
    while True:
        print('\n')
        print_product_list()
        print('\nProducts in selected order:\n')
        for key, value in selected_order.items():
            if key == 'Items':
                print(value)
        user_input = input("\nWhich product would you like to remove from the order?\nPlease enter the listing number associated to the desired product.\nLeave blank & press Enter to skip removing products from the order: ")
        if user_input == "":
            break
        try:
            user_input_int = int(user_input)
            products[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        break
    selected_order['Items'].remove(user_input_int)
    replace_order_value_removing_another_product(selected_order)

def replace_order_value_removing_another_product(selected_order):
    while True:
        print('\n')
        print_product_list()
        print('\nProducts in the selected order:\n')
        for key, value in selected_order.items():
            if key == 'Items':
                print(value)
        user_input = input("\nIf you would like to remove another product to the order, please enter the listing number before the desired product.\nLeave blank & press Enter to skip removing more products from the order: ")
        if user_input == "":
            break
        try:
            user_input_int = int(user_input)
            products[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        selected_order['Items'].remove(user_input_int)

def delete_product():
    clear()
    while True:
        print('\n')
        print_product_list()
        try:
            user_input = int(input("\nWhich product would you like to remove from the Product List?\nPlease enter the listing number before the product.\nEnter '0' to cancel deletion & return to Product Menu: "))
            product_index = user_input - 1
            selected_product = products[product_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            product_menu()
            break
        confirm_delete_product(product_index, selected_product)
        break

def confirm_delete_product(product_index, selected_product):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {selected_product} from the Product List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
            product_menu()
            break
        elif user_input == '1':
            clear()
            print(f'\n{selected_product} has successfully been removed from the Product List.')
            del products[product_index]
            product_menu()
            break
        else:
            incorrect_command()

def delete_courier():
    clear()
    while True:
        print('\n')
        print_courier_list()
        try:
            user_input = int(input("\nWhich courier would you like to remove from the Courier List?\nPlease enter the listing number before the courier.\nEnter '0' to cancel deletion & return to Courier Menu: "))    #FIND how to delete several at once? Same as adding several?
            courier_index = user_input - 1
            selected_courier = couriers[courier_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
            break
        confirm_delete_courier(courier_index, selected_courier)
        break

def confirm_delete_courier(courier_index, selected_courier):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {selected_courier} from the Courier List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
            courier_menu()
            break
        elif user_input == '1':
            clear()
            print(f'\n{selected_courier} has successfully been removed from the Courier List.')
            del couriers[courier_index]
            courier_menu()
            break
        else:
            incorrect_command()

def delete_order():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(input("\nWhich order would you like to remove from the Order List?\nPlease enter the number of the order.\nEnter '0' to cancel deletion & return to Order Menu: "))
            order_index = user_input - 1
            selected_order = orders[order_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
            break
        print('\nSelected Order:\n')
        for key, value in selected_order.items():
            print(f'{key}: {value}')
        confirm_delete_order(order_index)
        break

def confirm_delete_order(order_index):
    while True:
        user_input = input(f"\nAre you sure you would like to remove this order from the Order List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
            order_menu()
            break
        elif user_input == '1':
            clear()
            print(f'\nThe order has successfully been removed from the Order List.')
            del orders[order_index]
            order_menu()
            break
        else:
            incorrect_command()

def product_menu():
    clear()
    while True:
        print('PRODUCT MENU')
        user_input = input("\nEnter '1' to view the Product List\nEnter '2' to add a new product to the Product List\nEnter '3' to update the Product List by replacing a product with a new one\nEnter '4' to delete a product from the Product List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
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
        user_input = input("\nEnter '1' to view the Courier List\nEnter '2' to add a new courier to the Courier List\nEnter '3' to update the Courier List by replacing a courier with a new one\nEnter '4' to delete a courier from the Courier List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
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
        user_input = input("\nEnter '1' to view the Order List\nEnter '2' to add a new order to the Order List\nEnter '3' to change the Order Status of an order\nEnter '4' to update an existing order's information\nEnter '5' to delete an order from the Order List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
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
            break
        elif user_input == '4':
            replace_order_values()
            break
        elif user_input == '5':
            delete_order()
            break
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

### FIND where you enter '0' to 'skip' or not continue & change to empty str + pass
### CHECK that when asking for input based on list numbers, indexing doesn't allow use of '0' (since -1 selects last element in list)

### ADD populate lists & update txt files functions throughout code?
### REFER to products & courier lists by index or name - CONSISTENCY - use n += 1 with for loop
### ENUMERATE product & courier lists when printing (& elsewhere)
### CHANGE populate lists & update txt files functions (to have one of each &) to take arguments depending on if they're used for products or couriers. (vs two seperate functions for populating or for updating txt files)

### Move clear() to bottom/end of functions & see empty lines + incorrect_command() & print_list() interactions
### Make code even cleaner. Add functions to simplify each one