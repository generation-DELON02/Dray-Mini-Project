import csv

products = []
couriers = []
orders = []


def start_app():
    # lovely function
    print("\nWelcome to the London Region Anti Coffee Pop Up Café Business App")
    populate_product_list()
    populate_courier_list()
    populate_order_list()
    main_menu()


def exit_app():
    update_products_csv_file()
    update_couriers_csv_file()
    update_orders_csv_file()
    exit("\nExiting the app.")


def clear():
    print("\n" * 3)


def incorrect_command():
    clear()
    print(
        "Sorry, we did not recognise the input! Please enter an appropriate command.\n"
    )


# WRITING (PRODUCTS)
def update_products_csv_file():
    csv_keys = ["Name", "Price"]
    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.csv", "w"
        ) as product_list_file:
            writer = csv.DictWriter(product_list_file, fieldnames=csv_keys)
            writer.writeheader()
            for data in products:
                writer.writerow(data)
    except Exception as e:
        print("An error occurred when attempting to update the Product List: " + str(e))


# READING (PRODUCTS)
def populate_product_list():
    # this is a neat function, but by making it without parameters and relying on global variables
    # you're making it harder to test than it needs to be
    # that being said, testing file reading then appending to list is more integration test territory
    # so no need to worry about it for now

    # what is 'x'?...
    def float_converter(x):
        try:
            x_float = float(x)
        except ValueError:
            # out of interest does the exception still get raised even with the pass?
            # or does it carry on regardless of the exception?
            # if the latter, not much point in having it here
            # if the former, may as well print the exception message to let the user know what happened
            pass
        return x_float

    def convert_product_prices():
        for product in products:
            converted_value = float_converter(product["Price"])
            product["Price"] = converted_value

    # good having dedicated functions for the above
    # out of curiosity, what was the rationale behind defining them inside this function?

    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/product_list_file.csv"
        ) as product_list_file:
            file = csv.DictReader(product_list_file)
            for line in file:
                products.append(line)
    except Exception as e:
        print(
            "An error occurred when attempting to read the product list csv file: "
            + str(e)
        )

    convert_product_prices()


# WRITING (COURIERS)
def update_couriers_csv_file():
    # great name, only doing one thing, thumbs up
    csv_keys = ["Name", "Contact Number"]
    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.csv", "w"
        ) as courier_list_file:
            writer = csv.DictWriter(courier_list_file, fieldnames=csv_keys)
            writer.writeheader()
            for data in couriers:
                writer.writerow(data)
    except Exception as e:
        print("An error occurred when attempting to update the Courier List: " + str(e))


# READING (COURIERS)
def populate_courier_list():
    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/courier_list_file.csv"
        ) as courier_list_file:
            file = csv.DictReader(courier_list_file)
            for line in file:
                couriers.append(line)
    except Exception as e:
        print(
            "An error occurred when attempting to read the courier list csv file: "
            + str(e)
        )


# WRITING (ORDERS)
def update_orders_csv_file():
    csv_keys = ["Name", "Address", "Contact Number", "Courier", "Status", "Items"]
    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/order_list_file.csv", "w"
        ) as order_list_file:
            writer = csv.DictWriter(order_list_file, fieldnames=csv_keys)
            writer.writeheader()
            for data in orders:
                writer.writerow(data)
    except Exception as e:
        print("An error occurred when attempting to update the Order List: " + str(e))


# READING (ORDERS)
def populate_order_list():
    def int_converter(x):
        try:
            x_int = int(x)
        except ValueError:
            pass
        return x_int

    def convert_courier_values():
        for order in orders:
            converted_int = int_converter(order["Courier"])
            order["Courier"] = converted_int

    def convert_item_values():
        for order in orders:
            converted_list = []
            order["Items"] = list(order["Items"].split(", "))
            for item in order["Items"]:
                clean_item = item.replace("[", "").replace("]", "")
                converted_item = int_converter(clean_item)
                converted_list.append(converted_item)
            order["Items"] = converted_list

    try:
        with open(
            "C:/Users/Ajl-24/Documents/Python/Mini_Project/order_list_file.csv"
        ) as order_list_file:
            file = csv.DictReader(order_list_file)
            for line in file:
                orders.append(line)
    except Exception as e:
        print(
            "An error occurred when attempting to read the order list csv file: "
            + str(e)
        )
    # why do you call these outside the try block above?
    convert_courier_values()
    convert_item_values()


def print_product_list():
    # yep, nice
    print("\nProduct List:\n")
    for count, value in enumerate(products, 1):
        print(f"{count}: {value}")


def print_courier_list():
    print("\nCourier List:\n")
    for count, value in enumerate(couriers, 1):
        print(f"{count}: {value}")


def print_order_list():
    print("\nOrder List:\n")
    n = 1
    # to save you declaring and incrementing n manually
    # you could use enumerate here, I think
    # but otherwise, great function
    for order in orders:
        print(f"- {n} -")
        n += 1
        for key, value in order.items():
            print(f"{key}: {value}")
        print("\n")


def product_list():
    # not sure about the above name
    # it's not very descriptive compared to the others
    # show_products() maybe?
    # or even just reverse it, list_products()
    # I'm nitpicking tbh
    # you set the standard too high with the other names haha
    clear()
    while True:
        print_product_list()
        user_input = input(
            "\nEnter '0' to return to Product Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            product_menu()
            break
        else:
            incorrect_command()


def courier_list():
    # same nitpick here as with product_list()
    clear()
    while True:
        print_courier_list()
        user_input = input(
            "\nEnter '0' to return to Courier Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            courier_menu()
            break
        else:
            incorrect_command()


def order_list():
    clear()
    while True:
        print_order_list()
        user_input = input(
            "\nEnter '0' to return to Order Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            order_menu()
            break
        else:
            incorrect_command()


def add_product():
    clear()
    # how come this is in a loop?
    while True:
        # looooads of stuff happening here
        # I'd recommend making dedicated functions for getting new product values (see the example file I uploaded this morning)
        # then dedicated function for creating the new product
        # then finally dedicated function for appending
        # also, why is only one of the input fetching operations in the try block?
        user_input_1 = input(
            "\nADD PRODUCT\n\nWhich product would you like to add to the Product List?\n(Note: Be aware that any input will add to the list!)\nIf you would not like to add to the Product List, enter '0' to cancel & return to Product Menu: "
        )
        if user_input_1 == "0":
            product_menu()
        new_product = {"Name": "", "Price": float}
        new_product["Name"] = user_input_1.title()
        try:
            user_input_2 = float(input("What is the price of this item? "))
        except:
            incorrect_command()
            continue
        break
    new_product["Price"] = user_input_2
    # I would only show the success message after the append operation (and put the append operation into it's own function)
    print("\nThe following item was successfully added to the Product List:")
    for key, value in new_product.items():
        print(f"{key}: {value}")
    products.append(new_product)
    product_menu()


def add_courier():
    clear()
    while True:
        # same points as above
        
        user_input_1 = input(
            "\nADD COURIER\n\nWhat is the name of the courier you would like to add to the Courier List?\n(Note: Be aware that any input will add to the Courier List!)\nIf you would not like to add to the Courier List, enter '0' to cancel & return to Courier Menu: "
        )
        if user_input_1 == "0":
            courier_menu()
        new_courier = {"Name": "", "Contact Number": ""}
        new_courier["Name"] = user_input_1.title()
        try:
            user_input_2 = input(
                "What is the courier's contact number? "
            )  # Is there a way to account for incorrect number/input?
        except:
            incorrect_command()
            continue
        break
    new_courier["Contact Number"] = user_input_2
    print("\nThe following courier was successfully added to the Product List:")
    for key, value in new_courier.items():
        print(f"{key}: {value}")
    couriers.append(new_courier)
    courier_menu()


def add_order():
    clear()
    # user_input_1 ?? : D
    # what about just 'input' or 'choice'?
    user_input_1 = input(
        "ADD ORDER\n\nWhat is the name of the customer you wish to assign the new order to? (Note: Please be aware that any input in the next few steps will allocate information to the new order.)\nIf you would not like to add a new order, enter '0' to cancel new order & return to Order Menu: "
    )
    if user_input_1 == "0":
        order_menu()
    # below nine (or so) lines should be in dedicated functions
    # and then you can update the variables from things like user_input_2 to address
    # etc.
    # and again, only show success message after appending, not before
    new_order = {
        "Name": "",
        "Address": "",
        "Contact Number": "",
        "Courier": "",
        "Status": "Preparing",
        "Items": [],
    }
    new_order["Name"] = user_input_1.title()
    user_input_2 = input("What is the full address for the order? ")
    new_order["Address"] = user_input_2.title()
    user_input_4 = input("What is the customer's contact number? ")
    new_order["Contact Number"] = user_input_4
    add_order_product(new_order)
    add_order_another_product(new_order)
    add_order_courier(new_order)
    print("\n")
    for key, value in new_order.items():
        print(f"{key}: {value}")
    print("\nThe new order has successfully been added to the Order List.")
    orders.append(new_order)
    order_menu()


def add_order_product(new_order):
    while True:
        print_product_list()
        try:
            user_input = int(
                input(
                    "\nSelect a product from the list to add to the new order. Please enter the listing number before the desired product: "
                )
            )
            products[user_input - 1]
        except:
            # I like incorrect_command()
            incorrect_command()
            continue
        if user_input == 0:
            incorrect_command()
            continue
        break
    new_order["Items"].append(user_input)


def add_order_another_product(new_order):
    # feels like this and the above function could be renamed in order to more easily differentiate their behaviour
    # maybe something like add_product_to_order() and add_multiple_products_to_order()

    while True:
        print_product_list()
        try:
            user_input = int(
                input(
                    "\nSelect another product to add to the new order if you would like. Please enter the listing number before the desired product.\nEnter '0' to not add another product: "
                )
            )
            products[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            break
        new_order["Items"].append(user_input)
    # out of interest, why sort them?
    new_order["Items"].sort()


def add_order_courier(new_order):
    # nitpick: add_courier_to_order? (really is a nitpick, feel free to ignore)
    
    while True:
        print_courier_list()
        try:
            user_input = int(
                input(
                    "\nSelect a courier from the list above.\nPlease enter the listing number before the desired courier: "
                )
            )
            couriers[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            incorrect_command()
            continue
        break
    new_order["Courier"] = user_input


def change_order_status_order_selection():
    # I would consider breaking this into three functions
    # a parent function called change_order_status() (which would be called where change_order_status_order_selection()) is currently called)
    # this would then call the current function, which would be renamed to select_order(), you'd make this function return the selected order
    # it would then call the below function (change_order_status_status_selection()), which would take the returned value from select_order() 
    # as its argument e.g. update_order_status(order_to_update)
    # so you'd have something like 
    # 
    # def change_order_status():
    #   order = select_order()
    #   update_order_status(order)
    
    
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(
                input(
                    "Which order would you like to change the status of?\nPlease enter the number of the desired order.\nEnter '0' to cancel update & return to Order Menu: "
                )
            )
            selected_order = orders[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        break
    # I'd have a dedicated function for this printing
    print("\nSelected order:\n")
    for key, value in selected_order.items():
        print(f"{key}: {value}")
    change_order_status_status_selection(selected_order)


def change_order_status_status_selection(selected_order):
    while True:
        print("\nWhat would you like to update the order status to?")
        user_input = input(
            "\nEnter '1' for 'Preparing'\nEnter '2' for 'Ready for collection'\nEnter '3' for 'Out for delivery'\nEnter '4' for 'Delivered': "
        )
        if user_input == "1":
            new_status = "Preparing"
        elif user_input == "2":
            new_status = "Ready For Collection"
        elif user_input == "3":
            new_status = "Out For Delivery"
        elif user_input == "4":
            new_status = "Delivered"
        else:
            incorrect_command()
            continue
        break
    selected_order["Status"] = new_status
    print("\nOrder status succesfully updated:\n")
    for key, value in selected_order.items():
        print(f"{key}: {value}")
    order_menu()


def update_product():
    clear()
    while True:
        print_product_list()
        try:
            user_input_1 = int(
                input(
                    "\nWhich product would you like to update?\nPlease enter the listing number before the desired product.\nEnter '0' to cancel update & return to Product Menu: "
                )
            )
            selected_product = products[user_input_1 - 1]
        except:
            incorrect_command()
            continue
        if user_input_1 == 0:
            product_menu()
        break
    print(f"\nSelected product:")
    for key, value in selected_product.items():
        print(f"{key}: {value}")
    update_product_name(selected_product)
    product_menu()


def update_product_name(selected_product):
    user_input = input(
        "\nWhat would you like to update the product with?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        new_product_name = user_input.title()
        print(
            "\n"
            + selected_product["Name"]
            + f" has successfully been updated with {new_product_name}\n."
        )
        selected_product["Name"] = new_product_name
    update_product_price(selected_product)


def update_product_price(selected_product):
    while True:
        user_input = input(
            "What would you like to update the price of this product to?\nLeave blank & press Enter to skip updating this piece of information: "
        )
        if user_input == "":
            pass
        else:
            try:
                new_product_price = float(user_input)
                print(
                    f"\n{selected_product['Price']} has successfully been updated with {new_product_price}."
                )
                selected_product["Price"] = new_product_price
            except:
                incorrect_command()
                continue
        break


def update_courier():
    clear()
    while True:
        print_courier_list()
        try:
            user_input = int(
                input(
                    "\nWhich courier would you like to update?\nPlease enter the listing number before the desired courier.\nEnter '0' to cancel update & return to Courier Menu: "
                )
            )
            selected_courier = couriers[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
        break
    print(f"\nSelected courier:")
    for key, value in selected_courier.items():
        print(f"{key}: {value}")
    update_courier_name(selected_courier)
    courier_menu()


def update_courier_name(selected_courier):
    user_input = input(
        "\nWho would you like to update the courier with?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        new_courier_name = user_input.title()
        print(
            "\n"
            + selected_courier["Name"]
            + f" has successfully been updated with {new_courier_name}\n."
        )
        selected_courier["Name"] = new_courier_name
    update_courier_number(selected_courier)


def update_courier_number(selected_courier):
    user_input = input(
        "What would you like to update the courier's contact number to?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        new_courier_number = user_input
        print(
            "\n"
            + selected_courier["Contact Number"]
            + f" has successfully been updated with {new_courier_number}."
        )
        selected_courier["Contact Number"] = new_courier_number


def update_order_values():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(
                input(
                    "Which order would you like to update?\nPlease enter the number of the desired order.\nEnter '0' to cancel update & return to Order Menu: "
                )
            )
            selected_order = orders[user_input - 1]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        break
    print("\nSelected order:\n")
    for key, value in selected_order.items():
        print(f"{key}: {value}")
    update_order_value_name(selected_order)
    print("\nOrder succesfully updated:\n")
    for key, value in selected_order.items():
        print(f"{key}: {value}")
    order_menu()


def update_order_value_name(selected_order):
    user_input = input(
        "\nWhat would you like to replace the customer's name associated to the order to?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        selected_order["Name"] = user_input.title()
    update_order_value_address(selected_order)


def update_order_value_address(selected_order):
    user_input = input(
        "What would you like to replace the customer's address to?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        selected_order["Address"] = user_input.title()
    update_order_value_contact_number(selected_order)


def update_order_value_contact_number(selected_order):
    user_input = input(
        "What would you like to replace the customer's contact number to?\nLeave blank & press Enter to skip updating this piece of information: "
    )
    if user_input == "":
        pass
    else:
        selected_order["Contact Number"] = user_input
    update_order_value_adding_product(selected_order)


def update_order_value_adding_product(selected_order):
    while True:
        print("\n-Adding Products-")
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['Items']}")
        user_input = input(
            "\nWhich product would you like to add to the order?\nPlease enter the listing number before the desired product.\nLeave blank & press Enter to skip adding products to the order: "
        )
        if user_input == "":
            update_order_value_removing_product(selected_order)
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
        selected_order["Items"].append(user_input_int)
        update_order_value_adding_another_product(selected_order)
        break


def update_order_value_adding_another_product(selected_order):
    while True:
        print("\n-Adding Products-")
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['Items']}")
        user_input = input(
            "\nIf you would like to add another product to the order, please enter the listing number before the desired product.\nLeave blank & press Enter to skip adding more products to the order: "
        )
        if user_input == "":
            selected_order["Items"].sort()
            update_order_value_removing_product(selected_order)
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
        selected_order["Items"].append(user_input_int)


def update_order_value_removing_product(selected_order):
    while True:
        print("\n-Removing Products-")
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['Items']}")
        user_input = input(
            "\nWhich product would you like to remove from the order?\nPlease enter the listing number associated to the desired product.\nLeave blank & press Enter to skip removing products from the order: "
        )
        if user_input == "":
            update_order_value_courier(selected_order)
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
        selected_order["Items"].remove(user_input_int)
        update_order_value_removing_another_product(selected_order)
        break


def update_order_value_removing_another_product(selected_order):
    while True:
        print("\n-Removing Products-")
        print_product_list()
        print(f"\nProducts in the selected order:\n{selected_order['Items']}")
        user_input = input(
            "\nIf you would like to remove another product to the order, please enter the listing number before the desired product.\nLeave blank & press Enter to skip removing more products from the order: "
        )
        if user_input == "":
            update_order_value_courier(selected_order)
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
        selected_order["Items"].remove(user_input_int)


def update_order_value_courier(selected_order):
    while True:
        print_courier_list()
        print(
            f"\nCourier allocated to the selected order:\n{selected_order['Courier']}"
        )
        user_input = input(
            "\nSelect a courier from the list above to allocate to the order.\nPlease enter the listing number before the desired courier.\nLeave blank & press Enter to skip updating this piece of information: "
        )
        if user_input == "":
            break
        try:
            user_input_int = int(user_input)
            couriers[user_input_int - 1]
        except:
            incorrect_command()
            continue
        if user_input_int == 0:
            incorrect_command()
            continue
        selected_order["Courier"] = user_input_int
        break


def delete_product():
    clear()
    while True:
        print_product_list()
        try:
            user_input = int(
                input(
                    "\nWhich product would you like to remove from the Product List?\nPlease enter the listing number before the product.\nEnter '0' to cancel deletion & return to Product Menu: "
                )
            )
            product_index = user_input - 1
            selected_product = products[product_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            product_menu()
        break
    confirm_delete_product(product_index, selected_product)


def confirm_delete_product(product_index, selected_product):
    while True:
        user_input = input(
            f"\nAre you sure you would like to remove {selected_product} from the Product List?\n\nEnter '1' for YES\nEnter '0' for NO: "
        )
        if user_input == "0":
            print("\nDeletion cancelled.")
        elif user_input == "1":
            clear()
            print(
                f"\n{selected_product} has successfully been removed from the Product List."
            )
            del products[product_index]
        else:
            incorrect_command()
            continue
        break
    product_menu()


def delete_courier():
    clear()
    while True:
        print_courier_list()
        try:
            user_input = int(
                input(
                    "\nWhich courier would you like to remove from the Courier List?\nPlease enter the listing number before the courier.\nEnter '0' to cancel deletion & return to Courier Menu: "
                )
            )
            courier_index = user_input - 1
            selected_courier = couriers[courier_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            courier_menu()
        break
    confirm_delete_courier(courier_index, selected_courier)


def confirm_delete_courier(courier_index, selected_courier):
    while True:
        user_input = input(
            f"\nAre you sure you would like to remove {selected_courier} from the Courier List?\n\nEnter '1' for YES\nEnter '0' for NO: "
        )
        if user_input == "0":
            print("\nDeletion cancelled.")
        elif user_input == "1":
            clear()
            print(
                f"{selected_courier} has successfully been removed from the Courier List."
            )
            del couriers[courier_index]
        else:
            incorrect_command()
            continue
        break
    courier_menu()


def delete_order():
    clear()
    while True:
        print_order_list()
        try:
            user_input = int(
                input(
                    "\nWhich order would you like to remove from the Order List?\nPlease enter the number of the order.\nEnter '0' to cancel deletion & return to Order Menu: "
                )
            )
            order_index = user_input - 1
            selected_order = orders[order_index]
        except:
            incorrect_command()
            continue
        if user_input == 0:
            order_menu()
        break
    print("\nSelected Order:\n")
    for key, value in selected_order.items():
        print(f"{key}: {value}")
    confirm_delete_order(order_index)


def confirm_delete_order(order_index):
    while True:
        user_input = input(
            f"\nAre you sure you would like to remove this order from the Order List?\n\nEnter '1' for YES\nEnter '0' for NO: "
        )
        if user_input == "0":
            print("\nDeletion cancelled.")
        elif user_input == "1":
            clear()
            print(f"The order has successfully been removed from the Order List.")
            del orders[order_index]
        else:
            incorrect_command()
            continue
        break
    order_menu()


def product_menu():
    clear()
    while True:
        print("PRODUCT MENU")
        user_input = input(
            "\nEnter '1' to view the Product List\nEnter '2' to add a new product to the Product List\nEnter '3' to update the Product List by replacing a product with a new one\nEnter '4' to delete a product from the Product List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            main_menu()
        elif user_input == "1":
            product_list()
        elif user_input == "2":
            add_product()
        elif user_input == "3":
            update_product()
        elif user_input == "4":
            delete_product()
        else:
            incorrect_command()
            continue
        break


def courier_menu():
    clear()
    while True:
        print("COURIER MENU")
        user_input = input(
            "\nEnter '1' to view the Courier List\nEnter '2' to add a new courier to the Courier List\nEnter '3' to update the Courier List by replacing a courier with a new one\nEnter '4' to delete a courier from the Courier List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            main_menu()
        elif user_input == "1":
            courier_list()
        elif user_input == "2":
            add_courier()
        elif user_input == "3":
            update_courier()
        elif user_input == "4":
            delete_courier()
        else:
            incorrect_command()
            continue
        break


def order_menu():
    clear()
    while True:
        print("ORDER MENU")
        user_input = input(
            "\nEnter '1' to view the Order List\nEnter '2' to add a new order to the Order List\nEnter '3' to change the Order Status of an order\nEnter '4' to update an existing order's information\nEnter '5' to delete an order from the Order List\nEnter '0' to return to Main Menu\nEnter '00' to exit the app: "
        )
        if user_input == "00":
            exit_app()
        elif user_input == "0":
            main_menu()
        elif user_input == "1":
            order_list()
        elif user_input == "2":
            add_order()
        elif user_input == "3":
            change_order_status_order_selection()
        elif user_input == "4":
            update_order_values()
        elif user_input == "5":
            delete_order()
        else:
            incorrect_command()
            continue
        break


def main_menu():
    while True:
        user_input = input(
            "\nMAIN MENU\n\nEnter '1' to view the Product Menu\nEnter '2' to view the Courier Menu\nEnter '3' to view the Order Menu\nEnter '0' to exit the app: "
        )
        if user_input == "0":
            exit_app()
        elif user_input == "1":
            product_menu()
        elif user_input == "2":
            courier_menu()
        elif user_input == "3":
            order_menu()
        else:
            incorrect_command()
            continue
        break


start_app()

### ACCOUNT for not allowing blank input when adding new order
### Move clear() to bottom/end of functions & see empty lines + incorrect_command() & print_list() interactions
### PRINT product & courier lists without {} & each product/courier dict on one line

### CHANGE populate_list & update_csv_file functions (to have 1 of each &) to take arguments depending on if they're used for products or couriers (vs 2 seperate functions for populating/updating_csv_files) #SAME for orders?
### ADD update csv files functions throughout code?