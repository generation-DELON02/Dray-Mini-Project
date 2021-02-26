import csv
import os
import pymysql
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

products = []
couriers = []
orders = []

def start_app():
    print("\nWelcome to the Anti Coffee Pop Up Café Business App")
    clear_and_populate_product_list_from_db()
    clear_and_populate_courier_list_from_db()
    clear_and_populate_order_list_from_db()
    main_menu()

def exit_app():
    update_products_csv_file()
    update_couriers_csv_file()
    update_orders_csv_file()
    exit('\nExiting the app.')

def clear():
    print('\n' * 3)

def incorrect_command():
    clear()
    print("Sorry, we did not recognise the input! Please enter an appropriate command.\n")

def clear_and_populate_product_list_from_db():
    products.clear()
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM products"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                products.append(row)
        connection.close()
    except Exception as e:
        print('An error occurred when attempting to update the database: ' + str(e))

def clear_and_populate_courier_list_from_db():
    couriers.clear()
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM couriers"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                couriers.append(row)
        connection.close()
    except Exception as e:
        print('An error occurred when attempting to update the database: ' + str(e))

def clear_and_populate_order_list_from_db():
    orders.clear()
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "SELECT * FROM orders"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                orders.append(row)
        connection.close()
    except Exception as e:
        print('An error occurred when attempting to update the database: ' + str(e))
    convert_item_values_to_list()

def convert_item_values_to_list():
    for order in orders:
        converted_list = []
        order['items'] = list(order['items'].split(', '))
        for item in order['items']:
            clean_item = item.replace('[','').replace(']','')
            converted_item = int(clean_item)
            converted_list.append(converted_item)
        order['items'] = converted_list

def update_products_csv_file():
    csv_keys = ['id', 'name', 'price']
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.csv', 'w') as product_list_file:
            writer = csv.DictWriter(product_list_file, fieldnames = csv_keys)
            writer.writeheader()
            for data in products:
                writer.writerow(data)
    except Exception as e:
        print('An error occurred when attempting to update the csv Product file: ' + str(e))

def update_couriers_csv_file():
    csv_keys = ['id', 'name', 'contact number']
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.csv', 'w') as courier_list_file:
            writer = csv.DictWriter(courier_list_file, fieldnames = csv_keys)
            writer.writeheader()
            for data in couriers:
                writer.writerow(data)
    except Exception as e:
        print('An error occurred when attempting to update the csv Courier file: ' + str(e))

def update_orders_csv_file():
    csv_keys = ['id', 'name', 'address', 'contact number', 'courier', 'status', 'items']
    try:
        with open('C:/Users/Ajl-24/Documents/Python/Mini_Project/order_list_file.csv', 'w') as order_list_file:
            writer = csv.DictWriter(order_list_file, fieldnames = csv_keys)
            writer.writeheader()
            for data in orders:
                writer.writerow(data)
    except Exception as e:
        print('An error occurred when attempting to update the csv Order file: ' + str(e))

def print_product_list():
    print('\nProduct List:\n')
    for product in products:
        print(f"ID: {product['id']} - {product['name']}, £{product['price']}")

def print_courier_list():
    print('\nCourier List:\n')
    for courier in couriers:
        print(f"ID: {courier['id']} - {courier['name']}, {courier['contact number']}")

def print_order_list():
    print('\nOrder List:\n')
    for order in orders:
        for key, value in order.items():
            print(f'{key.title()}: {value}')
        print('\n')

def print_selected_order(selected_order):
    print('\nSelected order:\n')
    for key, value in selected_order.items():
        print(f'{key.title()}: {value}')

def view_products():
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

def view_couriers():
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

def view_orders():
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

def add_product():
    clear()
    while True:
        user_input_1 = input("\nADD PRODUCT\n\nWhich product would you like to add to the Product List?\n(Note: Be aware that any input will add to the list!)\nIf you would not like to add to the Product List, enter '0' to cancel & return to Product Menu: ")
        if user_input_1 == '0':
            product_menu()
        elif user_input_1 == '':
            incorrect_command()
            continue
        new_product = {'id': int, 'name': '', 'price': float}
        new_product['name'] = user_input_1.title()
        try:
            user_input_2 = float(input("What is the price of this item? "))
        except:
            incorrect_command()
            continue
        break
    new_product['price'] = user_input_2
    add_product_to_db(new_product)
    clear_and_populate_product_list_from_db()
    print('\nThe following item was successfully added to the Product List:')
    for product in products:
        if product['name'] == new_product['name']:
            for key, value in product.items():
                print(f'{key}: {value}')
    product_menu()

def add_product_to_db(new_product):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
            val = (new_product['name'], new_product['price'])
            cursor.execute(sql, val)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's product table" + str(e))

def add_courier():
    clear()
    while True:
        user_input_1 = input("\nADD COURIER\n\nWhat is the name of the courier you would like to add to the Courier List?\n(Note: Be aware that any input will add to the Courier List!)\nIf you would not like to add to the Courier List, enter '0' to cancel & return to Courier Menu: ")
        if user_input_1 == '0':
            courier_menu()
        new_courier = {'id': int, 'name' : '', 'contact number' : ''}
        new_courier['name'] = user_input_1.title()
        try:
            user_input_2 = input("What is the courier's contact number? ")      #Is there a way to account for incorrect number/input?
        except:
            incorrect_command()
            continue
        break
    new_courier['contact number'] = user_input_2
    add_courier_to_db(new_courier)
    clear_and_populate_courier_list_from_db()
    print('\nThe following courier was successfully added to the Product List:')
    for courier in couriers:
        if courier['name'] == new_courier['name']:
            for key, value in courier.items():
                print(f'{key}: {value}')
    courier_menu()

def add_courier_to_db(new_courier):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor: 
            sql = "INSERT INTO couriers (name, `contact number`) VALUES (%s, %s)"
            val = (new_courier['name'], new_courier['contact number'])
            cursor.execute(sql, val)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's courier table" + str(e))

def add_order():
    clear()
    print('ADD ORDER')
    new_order = {'id': int, 'name': '', 'address': '', 'contact number': '', 'courier': int, 'status': 'Preparing', 'items': []}
    add_order_add_name(new_order)
    add_order_add_address(new_order)
    add_order_add_contact_number(new_order)
    add_order_add_product(new_order)
    add_order_add_multiple_products(new_order)
    add_order_add_courier(new_order)
    add_order_to_db(new_order)
    clear_and_populate_order_list_from_db()
    for order in orders:
        if order['name'] == new_order['name']:
            print("\nThe new order has successfully been added to the Order List:\n")
            for key, value in order.items():
                print(f'{key.title()}: {value}')
    order_menu()

def add_order_add_name(new_order):
    user_input = input("\nWhat is the name of the customer you wish to assign the new order to? (Note: Please be aware that any input in the next few steps will allocate information to the new order.)\nIf you would not like to add a new order, enter '0' to cancel new order & return to Order Menu: ")
    if user_input == '0':
        order_menu()
    elif user_input == '':
        incorrect_command()
        add_order()
    new_order['name'] = user_input.title()

def add_order_add_address(new_order):
    while True:
        user_input = input("What is the full address for the order? ")
        if user_input == '':
            incorrect_command()
            continue
        new_order['address'] = user_input.title()
        break

def add_order_add_contact_number(new_order):
    while True:
        user_input = input("What is the customer's contact number? ")
        if user_input == '':
            incorrect_command()
            continue
        new_order['contact number'] = user_input
        break

def add_order_add_product(new_order):
    while True:
        print_product_list()
        try:
            user_input = int(input("\nSelect a product from the list to add to the new order. Please enter the ID of the desired product: "))
        except:
            incorrect_command()
            continue
        for product in products:
            if user_input == product['id']:
                selected_product = product
                break
            else:
                selected_product = None
        if selected_product == None:
            incorrect_command()
            continue
        break
    new_order['items'].append(user_input)

def add_order_add_multiple_products(new_order):
    while True:
        print('\nProducts in the new order:\n' + str(new_order['items']))
        print_product_list()
        user_input = input("\nSelect another product to add to the new order if you would like. Please enter the ID of the desired product.\nLeave blank & press Enter to skip adding more products: ")
        if user_input == '':
            new_order['items'].sort()
            break
        try:
            user_input_int = int(user_input)
        except:
            incorrect_command()
            continue
        for product in products:
            if user_input_int == product['id']:
                selected_product = product
                break
            else:
                selected_product = None
        if selected_product == None:
            incorrect_command()
            continue
        new_order['items'].append(user_input_int)
        new_order['items'].sort()

def add_order_add_courier(new_order):
    while True:
        print_courier_list()
        try:
            user_input = int(input("\nSelect a courier from the list above.\nPlease enter the ID of the desired courier: "))   
        except:
            incorrect_command()
            continue
        if user_input == 0:
            incorrect_command()
            continue
        for courier in couriers:
            if user_input == courier['id']:
                selected_courier = courier
                break
            else:
                selected_courier = None
        if selected_courier == None:
            incorrect_command()
            continue
        break
    new_order['courier'] = user_input

def add_order_to_db(new_order):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = "INSERT INTO orders (name, address, `contact number`, courier, status, items) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (new_order['name'], new_order['address'], new_order['contact number'], new_order['courier'], new_order['status'], str(new_order['items']))
            cursor.execute(sql, val)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's order table" + str(e))

def change_order_status_order_selection():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(input("Which order would you like to change the status of?\nPlease enter the ID of the desired order.\nEnter '0' to cancel update & return to Order Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        for order in orders:
            if user_input == order['id']:
                selected_order = order
                break
            else:
                selected_order = None
        if selected_order == None:
            incorrect_command()
            continue
        break
    print_selected_order(selected_order)
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
        break
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"UPDATE orders SET status = '{new_status}' WHERE id = {selected_order['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print('An error occurred when attempting to update the database: ' + str(e))
    selected_order['status'] = new_status
    print('\nOrder status succesfully updated:\n')
    for key, value in selected_order.items():
        print(f'{key}: {value}')
    order_menu()

def update_product():
    clear()
    while True:
        print_product_list()
        try:
            user_input = int(input("\nWhich product would you like to update?\nPlease enter the ID of the desired product.\nEnter '0' to cancel update & return to Product Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            product_menu()
        for product in products:
            if user_input == product['id']:
                selected_product = product
                break
            else:
                selected_product = None
        if selected_product == None:
            incorrect_command()
            continue
        break
    print('\nSelected product:')
    for key, value in selected_product.items():
        print(f'{key}: {value}')
    update_product_name(selected_product)
    product_menu()

def update_product_name(selected_product):
    user_input = input('\nWhat would you like to update the product name with?\nLeave blank & press Enter to skip updating this piece of information: ')
    if user_input == "":
        pass
    else:
        new_product_name = user_input.title()
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE products SET name = '{new_product_name}' WHERE id = {selected_product['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
        print('\n' + selected_product['name'] + f' has successfully been updated with {new_product_name}.\n')
        selected_product['name'] = new_product_name
    update_product_price(selected_product)

def update_product_price(selected_product):
    while True:
        user_input = input('What would you like to update the price of this product to?\nLeave blank & press Enter to skip updating this piece of information: ')
        if user_input == "":
            pass
        else:
            try:
                new_product_price = float(user_input)
            except:
                incorrect_command()
                continue
            try:
                connection = pymysql.connect(host, user, password, database)
                with connection.cursor() as cursor:
                    sql = f"UPDATE products SET price = {new_product_price} WHERE id = {selected_product['id']}"
                    cursor.execute(sql)
                    connection.commit()
                connection.close()
            except Exception as e:
                print('An error occurred when attempting to update the database: ' + str(e))
            print(f"\n{selected_product['price']} has successfully been updated with {new_product_price}.")
            selected_product['price'] = new_product_price
        break

def update_courier():
    clear()
    while True:
        print_courier_list()
        try:
            user_input = int(input("\nWhich courier would you like to update?\nPlease enter the ID of the desired courier.\nEnter '0' to cancel update & return to Courier Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
        for courier in couriers:
            if user_input == courier['id']:
                selected_courier = courier
                break
            else:
                selected_courier = None
        if selected_courier == None:
            incorrect_command()
            continue
        break
    print('\nSelected courier:')
    for key, value in selected_courier.items():
        print(f'{key}: {value}')
    update_courier_name(selected_courier)
    courier_menu()

def update_courier_name(selected_courier):
    user_input = input("\nWho would you like to update the courier's name with?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        new_courier_name = user_input.title()
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE couriers SET name = '{new_courier_name}' WHERE id = {selected_courier['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
        print('\n' + selected_courier['name'] + f' has successfully been updated with {new_courier_name}.\n')
        selected_courier['name'] = new_courier_name
    update_courier_number(selected_courier)

def update_courier_number(selected_courier):
    user_input = input("What would you like to update the courier's contact number to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        new_courier_number = user_input
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE couriers SET `contact number` = {new_courier_number} WHERE id = {selected_courier['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
        print('\n' + selected_courier['contact number'] + f' has successfully been updated with {new_courier_number}.')
        selected_courier['contact number'] = new_courier_number

def update_order_values():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(input("Which order would you like to update?\nPlease enter the ID of the desired order.\nEnter '0' to cancel update & return to Order Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        for order in orders:
            if user_input == order['id']:
                selected_order = order
                break
            else:
                selected_order = None
        if selected_order == None:
            incorrect_command()
            continue
        break
    print_selected_order(selected_order)
    update_order_value_name(selected_order)
    print('\nOrder succesfully updated:\n')
    for key, value in selected_order.items():
        print(f'{key}: {value}')
    order_menu()

def update_order_value_name(selected_order):
    user_input = input("\nWhat would you like to replace the customer's name associated to the order to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['name'] = user_input.title()
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE orders SET name = '{selected_order['name']}' WHERE id = {selected_order['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
    update_order_value_address(selected_order)

def update_order_value_address(selected_order):
    user_input = input("What would you like to replace the customer's address to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['address'] = user_input.title()
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE orders SET address = '{selected_order['address']}' WHERE id = {selected_order['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
    update_order_value_contact_number(selected_order)

def update_order_value_contact_number(selected_order):
    user_input = input("What would you like to replace the customer's contact number to?\nLeave blank & press Enter to skip updating this piece of information: ")
    if user_input == "":
        pass
    else:
        selected_order['contact number'] = user_input
        try:
            connection = pymysql.connect(host, user, password, database)
            with connection.cursor() as cursor:
                sql = f"UPDATE orders SET `contact number` = '{selected_order['contact number']}' WHERE id = {selected_order['id']}"
                cursor.execute(sql)
                connection.commit()
            connection.close()
        except Exception as e:
            print('An error occurred when attempting to update the database: ' + str(e))
    update_order_value_adding_product(selected_order)

def update_order_value_adding_product(selected_order):
    while True:
        print('\n-Adding Products-')
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['items']}")
        user_input = input("\nWhich product would you like to add to the order?\nPlease enter the ID of the desired product.\nLeave blank & press Enter to skip adding products to the order: ")
        if user_input == "":
            update_order_value_removing_product(selected_order)
            break
        try:
            user_input_int = int(user_input)   
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        for product in products:
            if user_input_int == product['id']:
                selected_product = product
                break
            else:
                selected_product = None
        if selected_product == None:
            incorrect_command()
            continue
        selected_order['items'].append(user_input_int)
        selected_order['items'].sort()
        update_order_items_in_db(selected_order)

def update_order_value_removing_product(selected_order):
    while True:
        print('\n-Removing Products-')
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['items']}")
        user_input = input("\nWhich product would you like to remove from the order?\nPlease enter the ID of the desired product.\nLeave blank & press Enter to skip removing products from the order: ")
        if user_input == "":
            update_order_value_courier(selected_order)
            break
        try:
            user_input_int = int(user_input)
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        if user_input_int in selected_order['items']:
            selected_order['items'].remove(user_input_int)
            update_order_items_in_db(selected_order)
        else:
            incorrect_command()

def update_order_value_courier(selected_order):
    while True:
        print_courier_list()
        print(f"\nCourier allocated to the selected order:\n{selected_order['courier']}")
        user_input = input("\nSelect a courier from the list above to allocate to the order.\nPlease enter the listing number before the desired courier.\nLeave blank & press Enter to skip updating this piece of information: ")
        if user_input == "":
            break
        try:
            user_input_int = int(user_input)
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        for courier in couriers:
            if user_input_int == courier['id']:
                selected_courier = courier
                break
            else:
                selected_courier = None
        if selected_courier == None:
            incorrect_command()
            continue
        selected_order['courier'] = selected_courier['id']
        update_order_courier_in_db(selected_order)
        break

def update_order_items_in_db(selected_order):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"UPDATE orders SET items = '{str(selected_order['items'])}' WHERE id = {selected_order['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's order table" + str(e))

def update_order_courier_in_db(selected_order):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"UPDATE orders SET courier = {selected_order['courier']} WHERE id = {selected_order['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's order table: " + str(e))

def delete_product():
    clear()
    while True:
        print_product_list()
        try:
            user_input = int(input("\nWhich product would you like to remove from the Product List?\nPlease enter the ID of the product.\nEnter '0' to cancel deletion & return to Product Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            product_menu()
        for product in products:
            if user_input == product['id']:
                selected_product = product
                break
            else:
                selected_product = None
        if selected_product == None:
            incorrect_command()
            continue
        break
    confirm_delete_product(selected_product)

def confirm_delete_product(selected_product):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {selected_product['name']} from the Product List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
        elif user_input == '1':
            clear()
            delete_product_from_db(selected_product)
            print(f'\n{selected_product} has successfully been removed from the Product List.')
            clear_and_populate_product_list_from_db()
        else:
            incorrect_command()
            continue
        break
    product_menu()

def delete_product_from_db(selected_product):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"DELETE FROM products WHERE id = {selected_product['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's product table: " + str(e))

def delete_courier():
    clear()
    while True:
        print_courier_list()
        try:
            user_input = int(input("\nWhich courier would you like to remove from the Courier List?\nPlease enter the ID of the courier.\nEnter '0' to cancel deletion & return to Courier Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
        for courier in couriers:
            if user_input == courier['id']:
                selected_courier = courier
                break
            else:
                selected_courier = None
        if selected_courier == None:
            incorrect_command()
            continue
        break
    confirm_delete_courier(selected_courier)

def confirm_delete_courier(selected_courier):
    while True:
        user_input = input(f"\nAre you sure you would like to remove {selected_courier['name']} from the Courier List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
        elif user_input == '1':
            clear()
            delete_courier_from_db(selected_courier)
            print(f'\n{selected_courier} has successfully been removed from the Courier List.')
            clear_and_populate_courier_list_from_db()
        else:
            incorrect_command()
            continue
        break
    courier_menu()

def delete_courier_from_db(selected_courier):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"DELETE FROM couriers WHERE id = {selected_courier['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's courier table: " + str(e))

def delete_order():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(input("\nWhich order would you like to remove from the Order List?\nPlease enter the ID of the order.\nEnter '0' to cancel deletion & return to Order Menu: "))
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        for order in orders:
            if user_input == order['id']:
                selected_order = order
                break
            else:
                selected_order = None
        if selected_order == None:
            incorrect_command()
            continue
        break
    print_selected_order(selected_order)
    confirm_delete_order(selected_order)

def confirm_delete_order(selected_order):
    while True:
        user_input = input(f"\nAre you sure you would like to remove this order from the Order List?\n\nEnter '1' for YES\nEnter '0' for NO: ")
        if user_input == '0':
            print('\nDeletion cancelled.')
        elif user_input == '1':
            clear()
            delete_order_from_db(selected_order)
            clear_and_populate_order_list_from_db()
            print(f'The order has successfully been removed from the Order List.')
        else:
            incorrect_command()
            continue
        break
    order_menu()

def delete_order_from_db(selected_order):
    try:
        connection = pymysql.connect(host, user, password, database)
        with connection.cursor() as cursor:
            sql = f"DELETE FROM orders WHERE id = {selected_order['id']}"
            cursor.execute(sql)
            connection.commit()
        connection.close()
    except Exception as e:
        print("An error occurred when attempting to update the database's order table: " + str(e))

def product_menu():
    clear()
    while True:
        print('PRODUCT MENU')
        user_input = input("\nEnter '1' to view the Product List\nEnter '2' to add a new product to the Product List\nEnter '3' to update the Product List by replacing a product with a new one\nEnter '4' to delete a product from the Product List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
        elif user_input == '1':
            view_products()
        elif user_input == '2':
            add_product()
        elif user_input == '3':
            update_product()
        elif user_input == '4':
            delete_product()
        else:
            incorrect_command()
            continue
        break

def courier_menu():
    clear()
    while True:
        print('COURIER MENU')
        user_input = input("\nEnter '1' to view the Courier List\nEnter '2' to add a new courier to the Courier List\nEnter '3' to update the Courier List by replacing a courier with a new one\nEnter '4' to delete a courier from the Courier List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
        elif user_input == '1':
            view_couriers()
        elif user_input == '2':
            add_courier()
        elif user_input == '3':
            update_courier()
        elif user_input == '4':
            delete_courier()
        else:
            incorrect_command()
            continue
        break

def order_menu():
    clear()
    while True:
        print('ORDER MENU')
        user_input = input("\nEnter '1' to view the Order List\nEnter '2' to add a new order to the Order List\nEnter '3' to change the Order Status of an existing order\nEnter '4' to update an existing order's information\nEnter '5' to delete an order from the Order List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: ")
        if user_input == '00':
            exit_app()
        elif user_input == '0':
            main_menu()
        elif user_input == '1':
            view_orders()
        elif user_input == '2':
            add_order()
        elif user_input == '3':
            change_order_status_order_selection()
        elif user_input == '4':
            update_order_values()
        elif user_input == '5':
            delete_order()
        else:
            incorrect_command()
            continue
        break
        
def main_menu():
    while True:
        user_input = input("\nMAIN MENU\n\nEnter '1' to view the Product Menu\nEnter '2' to view the Courier Menu\nEnter '3' to view the Order Menu\nEnter '0' to exit the app: ")
        if user_input == '0':
            exit_app()
        elif user_input == '1':
            product_menu()
        elif user_input == '2':
            courier_menu()
        elif user_input == '3':
            order_menu()
        else:
            incorrect_command()
            continue
        break

start_app()

### ACCOUNT for not allowing blank input when adding new order
### Move clear() to bottom/end of functions & see empty lines + incorrect_command() & print_list() interactions
### TRY to use ID check function - SEE update_product & more

### ADD update csv files functions throughout code?