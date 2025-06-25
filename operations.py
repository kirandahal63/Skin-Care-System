# Importing functions from user-defined modules for product data handling, billing, invoicing, and date functionalities
from read import read_products_fromfile
from write import bill_generation_and_update_txt
from read import date
from write import stock_invoice
from write import writing_for_sales
from write import writing_for_restock
#Creating function to display details of text file stored in nested dictionary
def display_products(value):
    """
    Display all products from the inventory with updated prices based on a multiplier.

    This function reads product data from 'product_inventory.txt' using the
    read_products_fromfile() function, increases the price of each product by multiplying it with
    the given value, and then displays the updated product details in a tabular format.

    Parameters:
    value (int or float): A custom multiplier used to increase the price of each product.

    Returns: None

    Raises:
    ValueError: If values in the txt file cannot be correctly parsed into integers or expected format.

    Example:
    >>> display_products(1)
    --------------------------------------------------------------------------------
    Product name 		  Brand 	Qnt 	 Price 		 Origin
    --------------------------------------------------------------------------------
    Vitamin C Serum 	  Garnier 	 230 	 Rs 1000 	  France
    Skin Cleanser 		  Cetaphil 	 103 	 Rs 280 	  Switzerland
    Sunscreen 		  Aqualogica 	 807 	 Rs 750 	  India
    --------------------------------------------------------------------------------
    """
    
    # Creating a variable d that holds dictionary returned from read_products_fromfile() function
    d = read_products_fromfile()
    
    print("-" * 80)
    print("Product name \t\t  Brand \tQnt \t Price \t\t Origin")
    print("-" * 80)
    for product, details in d.items():
        # Increasing the price as requested 
        details['price'] *= value
        if len(product) < 15:  # Adjust this length based on expected column width
            print(product, '\t\t', details['brand'], '\t', details['quantity'], '\t',
                  "Rs", details['price'], '\t', details['origin'])
        else:
            print(product, '\t', details['brand'], '\t', details['quantity'], '\t',
                  "Rs", details['price'], '\t', details['origin'])

    print("-" * 80)

#This function asks number as input check whether the number is valid or not
def number_validation():
    """
    Repeatedly asks the user to input a contact number and when the user enter a 10-digit contact number,
    it validates the input and return it.

    Parameters:
    None

    Returns:
    int: A validated 10-digit contact number entered by the user.

    Raises:
    ValueError: If the user inputs other than numbers.

    Example:
    >>> number_validation()
    Enter contact number of the customer: 12345
    Please enter a valid number!!
    Enter contact number of the customer: xyjhbj
    Please enter a valid number!!
    Enter contact number of the customer: 9854123654
    
    9876543210
    """
    while True:
        try:
            num = int(input("Enter contact number of the customer: "))
            if len(str(num))==10:
                break
            else:
                print("Please enter a valid number!!")
        except ValueError:
            print("Please enter a valid number!!")
    return num


#This is a function relating to sales operation

def selling_product():
    """
    Handle the product sales process, allows a user to purchase products by checking if the requested product exists,
    quantity checking,includes promotional logic(buy 3 get 1 free) for free items, updates the inventory accordingly,
    calculates the total bill,and finally collects customer details to generate an invoice and update the inventory file. 

    Parameters:
    None

    Returns:
    None

    Raises:
    ValueError: If the user enters invalid quantity or contact number input.

    Example:
    >>> selling_product()
    --------------------------------------------------------------------------------
    Product name 		  Brand 	Qnt 	 Price 		 Origin
    --------------------------------------------------------------------------------
    Vitamin C Serum 	  Garnier 	 230 	 Rs 2000 	  France
    Skin Cleanser 	  Cetaphil 	 103 	 Rs 560 	  Switzerland
    Sunscreen 		  Aqualogica 	 807 	 Rs 1500 	  India
    --------------------------------------------------------------------------------
    Please enter what do you want to Buy: vitamin c seru


    Product doesnt exists. 

    Please enter what do you want to Buy: vitamin C serum
    Please enter no ofquantity you want to buy3

    Product added Sucessfully!!

    Do you want to buy more products?
    Press y for YES and n for NO: no
    --------------------------------------------------------------------------------
    Bill Generation
    --------------------------------------------------------------------------------
    Enter name of the customer: kiran dahal
    Enter contact number of the customer: 9851058585
    --------------------------------------------------------------------------------

    """
    
    # using list to check existing product bought by customer
    user_list = []
    #Initializing global variables
    total = 0
    grand_total = 0
    d = read_products_fromfile()
    
    purchase_loop = True
    while purchase_loop == True:
        #Display product with 2X of its cost price
        display_products(2)
        
        user_input = input("Please enter what do you want to Buy: ")
        print('\n')
        #store actual key's name to carry other operations with dict
        product_original_key = None
        
        # check if product exists or not
        
        while True:
            for key in d.keys():
                if user_input.lower() == key.lower():
                    product_original_key = key
                    break
            if product_original_key == None:
                print("Product doesnt exists. \n")
                user_input = input("Please enter what do you want to Buy: ")
                print("\n")
            else:
                break

        # check if enough product is there to buy or not
        
        check_quantity_loop = False
        while check_quantity_loop == False:
            
            #storing quantity in a local variable
            stock = d[product_original_key]['quantity']
            max_quantity = (stock*3)//4
            
            loop_maxqty = True
            while loop_maxqty:
                free_items = max_quantity//3
                total_items = max_quantity + free_items
                if total_items>stock:
                   max_quantity -= 1
                else:
                  loop_maxqty = False
                  
            try:
                quantity = int(input("Please enter no of quantity you want to buy: "))
                free_items_byQty = quantity//3
                noOfQty_to_deduct = quantity + free_items_byQty
                
                while quantity>max_quantity or quantity<=0:
                    print("Please enter quantity between range ",0," and ",max_quantity)
                    quantity = int(input("Please enter no of quantity you want to buy: "))
                    free_items_byQty = quantity//3
                    noOfQty_to_deduct = quantity + free_items_byQty
                
                print('\nProduct added Sucessfully!!\n')
                
                
                #find the total amount
                unit_price=d[product_original_key]['price']*2
                total_amount = quantity* unit_price
                grand_total+=total_amount
                
                #checking product was aldready bought or not
                product_was_bought = False
                #using for each loop to check each items from list
                for item in user_list:
                    if item[0] == product_original_key:
                        previous_noOf_total_deduct = item[4]
                        item[2] +=quantity
                        item[3] =item[2]//3
                        item[4] =item[2]+item[3] #quantity to deduct
                        item[6] += total_amount
                        product_was_bought = True
                        final_deduct = item[4] - previous_noOf_total_deduct
                        d[product_original_key]['quantity'] -= final_deduct
                        writing_for_sales(d)
                        break
                       
                #if product doesnt exist append in list
                if product_was_bought == False:  
                    '''working with the list to store details like product type, brand,
                    quantity sold along with free ones, and the total amount only calculated excluding free quantity.'''
                    
                    user_list.append([product_original_key, d[product_original_key]['brand'],quantity,
                                      free_items_byQty, noOfQty_to_deduct, unit_price, total_amount])
                     #update dictionary with quantity
                    d[product_original_key]['quantity'] =d[product_original_key]['quantity']-noOfQty_to_deduct
                    writing_for_sales(d)

                date_of_transaction=None
                while True:
                    #Ask whether customer wants to buy ore product or not
                    ask_continue = input('Do you want to buy more products?\nPress y for YES and n for NO: ')
                    if ask_continue.lower() in ('yes','y'):
                        check_quantity_loop= True
                        break
                    
                    elif ask_continue.lower() in ('no','n'):
                        check_quantity_loop= True
                        purchase_loop = False
                        
                        #asking user their necessary details
                        print("-" * 80)
                        print("Bill Generation")
                        print("-" * 80)
                        customer_name = input("Enter name of the customer: ")
                        date_of_transaction=date()
                        number =number_validation()
                        print("-" * 80)
                        break
                    else:
                        continue
                
            except ValueError:
                print("Please enter a valid number\n")
                
    #calling bill_generation_and_update_txt to generate txt file, generatee invoice and unique text file
                
    bill_generation_and_update_txt(user_list,date_of_transaction,grand_total,customer_name, number)
    


#This functions works with restocking products
def restocking_products():
    """
    Restock existing products by increasing their quantity and optionally updating their price.
    It displays available products, validates restock input,calculates total cost for restocking,
    and collects supplier and date details.Finally,it generates a restock invoice and updates the product file.

    Parameters:
    None

    Returns:
    None

    Raises:
    ValueError: If the user enters invalid(non-integer) quantity or price.

    Example:
    >>> restocking_products()
    
    --------------------------------------------------------------------------------
    Product name 	  Brand 	Qnt 	 Price 		 Origin
    --------------------------------------------------------------------------------
    Vitamin C Serum 	  Garnier 	 226 	 Rs 1000 	  France
    Skin Cleanser 	  Cetaphil 	 103 	 Rs 280 	  Switzerland
    Sunscreen 		  Aqualogica 	 807 	 Rs 750 	  India
    --------------------------------------------------------------------------------

    Please enter what do you want to Restock: vitamin c serum


    Admin! Please enter no of quantity you want to restock: 4

    Do you want to UPDATE product price?
    Press y for YES and n for NO: no
    --------------------------------------------------------------------------------
    Do you want to restock another product?
    Press y for YES and n for NO: no
    --------------------------------------------------------------------------------

    Enter name of supplier: Adarsh Suppliers
    """
    
    #calling read_products_fromfile() which returns dictionary
    d = read_products_fromfile()
    
    #Initialize global variables
    restock_list = []
    total_amount=0
    grand_total=0
    
    restock_loop = True
    while restock_loop == True:
        #calling display_product function
        display_products(1)
        #asking user what to input
        user_input = input("\nPlease enter what do you want to Restock: ")
        print('\n')
        product_original_key = None        
        # check if product exists or not        
        while True:
            for key in d.keys():
                if user_input.lower() == key.lower():
                    product_original_key = key
                    break
            if product_original_key == None:
                print("Product doesnt exists. \n")
                user_input = input("Admin! Please enter what do you want to Restock: ")
            else:
                break
        ask_loop = True
        while ask_loop == True:
            try:
                ask_admin_qty = int(input("Admin! Please enter no of quantity you want to restock: "))
                #updating quantity in dictionarry with user input quantity
                while (ask_admin_qty < 0 or ask_admin_qty>500):
                    try:
                        print("\nPlease enter quantity to restock between 0 to 500.\n")
                        ask_admin_qty = int(input("Admin! Please enter no of quantity you want to restock: "))
                    except:
                        print("Please enter a valid number!!!")
                    
                d[product_original_key]['quantity']+=ask_admin_qty
                update_price=0
                
                option_admin = input('\nDo you want to UPDATE product price?\nPress y for YES and n for NO: ')
                if option_admin.lower() in ('yes','y'):
                    while True:
                        try:
                            update_price = int(input("\nPlease enter Updated price: "))
                            d[product_original_key]['price']=update_price
                            break
                        except ValueError:
                            print("Please enter a valid number!!!")
                        
                total_amount = d[product_original_key]['price']*ask_admin_qty

                grand_total += total_amount
                #updating text file
                writing_for_restock(d)
                
                #checking product was aldready ADDED or not
                product_was_added = False
                #using for each loop to check each items from list
                for item in restock_list:
                    if item[0] == product_original_key:
                        item[2] += ask_admin_qty
                        item[3] = d[product_original_key]['price']
                        item[4] += total_amount
                        product_was_added = True
                        break
                #if product doesnt exist append in list
                if product_was_added == False:  
            
                    '''product type, brand, quantity bought, 
                    name of the vendor/supplier, cost/rate of item, date of transaction and the total 
                    amount.'''
                    restock_list.append([product_original_key,d[product_original_key]['brand'],ask_admin_qty,
                                      d[product_original_key]['price'],total_amount])
                ask_loop = False
            except ValueError:
                print("Please enter a valid number!!!\n")
                continue

            while True:
                print("-" * 80)
                ask_continue = input('Do you want to restock another product?\nPress y for YES and n for NO: ')
                print("-" * 80)    
                if ask_continue.lower() in ('yes','y'):
                    restock_loop = True
                    break
                    
                elif ask_continue.lower() in ('no','n'):
                    restock_loop = False
                    supplier = input("\nEnter name of supplier: ")
                    date_of_transaction=date()
                    break
                else:
                    continue
                
    #calling restock invoice function 
    stock_invoice(restock_list, supplier,date_of_transaction,grand_total)
