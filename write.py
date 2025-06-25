from read import date

def writing_for_sales(d):
    '''
     It updates the product inventory in the "product_inventory.txt" file.


     Parameter:
     - d (dict): A dictionary containing product details where the key is the product name, and
                the value is another dictionary with product attributes such as brand, quantity, price, and origin.
     Returns : None
     
    '''
    #updating original text file product_inventory.txt after purchased is made    
    with open("product_inventory.txt", "w") as file1:
        for product, details in d.items():
            line = product + "," + details['brand'] + "," + str(details['quantity']) + "," + str(details['price']) + "," + details['origin'] + "\n"
            file1.write(line)
            
#This function is created to update original text file, create bill and invoice in new and unique text file'''
def bill_generation_and_update_txt(user_list,date_of_transaction,grand_total,customer_name, number):
    ''' 
    This function generates a bill for the customer's purchase by displaying store information,user details,the purchase details, 
    calculating the total cost, VAT, and grand total.It saves the generated invoice in an unique text file.

    Parameters:
    - user_list (list): A list of lists, where each inner list contains details of a purchased product
                (product name, brand, quantity, free items, total quantity, unit price, and total amount).
    - date_of_transaction (str): The date and time of the transaction.
    - grand_total (float): The total amount of the customer's purchase before VAT.
    - customer_name (str): The name of the customer making the purchase.
    - number (str): The contact number of the customer.

    Returns: None:

    Example:
    >>>bill_generation_and_update_txt(d,user_list,date_of_transaction,grand_total,customer_name, number)
    ================================================================================
                               WeCare PVT. LTD 

                     PAN: 369854550,  DDA REG: 3720222221589 

                     Kamaladi, Kathmandu | Phone: 01-5256098
     
                              wecareOfficial26@gmail.com

     
                                                 Invoice Issue: 2025/5/10 11:24:49
    ================================================================================
    Name of the Customer: KIRAN DAHAL
    Contact number:  9851000000
    ================================================================================


    Details:
    --------------------------------------------------------------------------------
    SN  Product Name      Brand          Qty   Free   TotalQty   UnitPrice   Amount

    --------------------------------------------------------------------------------
    1  Vitamin C Serum    Garnier        2     0      2          2000        4000          
    -------------------------------------------------------------------------------- 

    Total: Rs 4000
    Vat Rate: 13%
    Vat Amount: Rs 520.0
    ================================================================================
    Grand Total: Rs 4520.0
    ================================================================================
    
    '''

    #Generating a bill
    print('\n')
    print('\n')
    print("=" * 80)
    print("\t \t \t   WeCare PVT. LTD \n")
    print("\t \t PAN: 369854550,  DDA REG: 3720222221589 \n")
    print("\t \t Kamaladi, Kathmandu | Phone: 01-5256098\n ")
    print("\t \t \t  wecareOfficial26@gmail.com\n\n ")
    print("\t"*5,"    Invoice Issue:",date_of_transaction)
    print("=" * 80)
    print("Name of the Customer: " + customer_name.upper())
    print("Contact number: ", number)
    print("=" * 80)
    print("\n")
    print("Details:")
    print("-" * 80)
    print("SN  Product Name      Brand          Qty   Free   TotalQty   UnitPrice   Amount\n")
    print("-" * 80)
    sn=1
    #using loop to access inner list
    for details in user_list:
        sn_str = str(sn) + " " * (3 - len(str(sn)))
        name_str = details[0] + " " * (18 - len(details[0]))
        brand_str = details[1] + " " * (12 - len(details[1])) + " " * 4  
        qty_str = str(details[2]) + " " * (3 - len(str(details[2])))
        free_str = str(details[3]) + " " * (4 - len(str(details[3])))
        total_qty_str = str(details[4]) + " " * (9 - len(str(details[4])))
        unit_price_str = str(details[5]) + " " * (12 - len(str(details[5])))
        amount_str = str(details[6]) + " " * (14 - len(str(details[6])))

        print(sn_str + name_str + brand_str + qty_str + '   '+ free_str +'   '+
              total_qty_str + '  '+unit_price_str + amount_str)


        sn+=1
    print("-" * 80,"\n")
    print("Total: Rs",str(grand_total))
    print("Vat Rate: 13%")
    print("Vat Amount: Rs",str(grand_total*0.13))
    print("=" * 80)
    print("Grand Total: Rs",str(grand_total+grand_total*0.13)) 
    print("=" * 80,"\n")


    # Saving Invoice to a text file
    date = str(date_of_transaction).replace("/", "-").replace(":", "-").replace(" ", "_")
    with open(customer_name + date + ".txt", "w")as file:
        file.write("\n\n")
        file.write("=" * 80 + "\n")
        file.write("\t \t \t   WeCare PVT. LTD \n")
        file.write("\t \t PAN: 369854550,  DDA REG: 3720222221589 \n")
        file.write("\t \t Kamaladi, Kathmandu | Phone: 01-5256098\n")
        file.write("\t \t \t  wecareOfficial26@gmail.com\n\n")
        file.write("\t" * 5 + "    Invoice Issue: " + str(date_of_transaction) + "\n")
        file.write("=" * 80 + "\n")
        file.write("Name of the Customer: " + customer_name.upper() + "\n")
        file.write("Contact number: " + str(number) + "\n")
        file.write("=" * 80 + "\n\n")
        file.write("Details:\n")
        file.write("-" * 80 + "\n")
        file.write("SN  Product Name      Brand          Qty   Free   TotalQty   UnitPrice   Amount\n")
        file.write("-" * 80 + "\n")

        sn = 1
        for details in user_list:
            sn_str = str(sn) + " " * (3 - len(str(sn)))
            name_str = details[0] + " " * (18 - len(details[0]))
            brand_str = details[1] + " " * (12 - len(details[1])) + " " * 4  
            qty_str = str(details[2]) + " " * (3 - len(str(details[2])))
            free_str = str(details[3]) + " " * (4 - len(str(details[3])))
            total_qty_str = str(details[4]) + " " * (9 - len(str(details[4])))
            unit_price_str = str(details[5]) + " " * (12 - len(str(details[5])))
            amount_str = str(details[6]) + " " * (14 - len(str(details[6])))

            file.write(
                sn_str
                + name_str
                + brand_str
                + qty_str + '   '
                + free_str + '   '
                + total_qty_str + '  '
                + unit_price_str
                + amount_str + "\n"
            )

            sn += 1
        file.write("-" * 80)
        file.write("\n")
        file.write("Total: Rs "+str(grand_total))
        file.write("\n")
        file.write("Vat Rate: 13%")
        file.write("\n")
        file.write("Vat Amount: Rs "+str(grand_total*0.13))
        file.write("\n")
        file.write("=" * 80)
        file.write("\n")
        file.write("Grand Total: Rs "+str(grand_total+grand_total*0.13))
        file.write("\n")
        file.write("=" * 80+"\n")

def writing_for_restock(d):
    '''
     It updates the product inventory in the "product_inventory.txt" file.


     Parameter:
     - d (dict): A dictionary containing product details where the key is the product name, and
                the value is another dictionary with product attributes such as brand, quantity, price, and origin.
     Returns : None
     
    '''
   #opening text file to update restocked product
    with open("product_inventory.txt", "w") as files:
        for product, details in d.items():
            line = product + "," + details['brand'] + "," + str(details['quantity']) + "," + str(details['price']) + "," + details['origin'] + "\n"
            files.write(line)

#function to generate Restock bill invoice and Invoice txt
def stock_invoice(restock_list, supplier,date_of_transaction,grand_total):
    '''
    Generates and  prints suppliers name,invoice details (product name,brand, quantity, price, and total) to the console,
    saves the same info to a unique text file, and 
    updates 'product_inventory.txt' with the new stock data.

    Parameters:
    - d (dict): A dictionary of current product data. Each key is a product name and its value 
                is another dictionary containing product attributes like brand, quantity, price, and origin.
    - restock_list (list): A list of restocked items. Each item is a list containing 
                [product name, brand, quantity restocked, unit price, total amount].
    - supplier (str): Name of the supplier providing the restocked products.
    - date_of_transaction (str): The date and time when the restocking occurred.
    - grand_total (float): The total cost of all restocked items before VAT.

    Returns: None:

    Example:
    >>> stock_invoice(d,restock_list, supplier,date_of_transaction,grand_total)
    ================================================================================
                               WeCare PVT. LTD 

                     PAN: 369854550,  DDA REG: 3720222221589 

                     Kamaladi, Kathmandu | Phone: 01-5256098
     
                              wecareOfficial26@gmail.com

     
                                       Restock Invoice Issue: 2025/5/10 11:29:18
    ================================================================================
    Name of the Supplier: Ghanshyam distributors
    ================================================================================


    Details:
    --------------------------------------------------------------------------------
    SN  Product name 		  Brand 	Qnt 	 Price 		 Amount
    --------------------------------------------------------------------------------
    1     Vitamin C Serum 		  Garnier 	 15 	 Rs 1000 	 15000
    -------------------------------------------------------------------------------- 

    Total: Rs 15000
    Vat Rate: 13%
    Vat Amount: Rs 1950.0
    ================================================================================
    Grand Total: Rs 16950.0
    ================================================================================ 
    '''
 
    #Generating Restock Invoice
    print('\n')
    print('\n')
    print("=" * 80)
    print("\t \t \t   WeCare PVT. LTD \n")
    print("\t \t PAN: 369854550,  DDA REG: 3720222221589 \n")
    print("\t \t Kamaladi, Kathmandu | Phone: 01-5256098\n ")
    print("\t \t \t  wecareOfficial26@gmail.com\n\n ")
    print("\t"*4,"  Restock Invoice Issue:",date_of_transaction)
    print("=" * 80)
    print("Name of the Supplier: " + supplier.upper())
    print("=" * 80)
    print("\n")
    print("Details:")
    print("-" * 80)
    print("SN  Product name \t\t  Brand \tQnt \t Price \t\t Amount")
    print("-" * 80)
    sn=1
    #using loop to access inner list
    for details in restock_list:
        print(sn,'   ',details[0], '\t\t', details[1], '\t', details[2], '\t',"Rs", details[3], '\t', details[4])
        sn+=1
    print("-" * 80,"\n")
    print("Total: Rs",grand_total)
    print("Vat Rate: 13%")
    print("Vat Amount: Rs",str(grand_total*0.13))
    print("=" * 80)
    print("Grand Total: Rs",str(grand_total+grand_total*0.13)) 
    print("=" * 80,"\n"*3)

    # creating a text file for invoice
    date = str(date_of_transaction).replace("/", "-").replace(":", "-").replace(" ", "_")
    with open(supplier+ date + ".txt", "w") as invoice:
        invoice.write('\n')
        invoice.write('\n')
        invoice.write("=" * 80 + "\n")
        invoice.write("\t \t \t   WeCare PVT. LTD \n")
        invoice.write("\t \t PAN: 369854550,  DDA REG: 3720222221589 \n")
        invoice.write("\t \t Kamaladi, Kathmandu | Phone: 01-5256098\n ")
        invoice.write("\t \t \t  wecareOfficial26@gmail.com\n\n ")
        invoice.write("\t" * 4 + "  Restock Invoice Issue:" + str(date_of_transaction) + "\n")
        invoice.write("=" * 80 + "\n")
        invoice.write("Name of the Supplier: " + supplier.upper() + "\n")
        invoice.write("=" * 80 + "\n")
        invoice.write("\n")
        invoice.write("Details:\n")
        invoice.write("-" * 80 + "\n")
        invoice.write("SN  Product name \t\t  Brand \tQnt \t Price \t\t Amount\n")
        invoice.write("-" * 80 + "\n")
        sn = 1
        for details in restock_list:
            invoice.write(str(sn) + '   ' + details[0] + '\t\t' + details[1] + '\t' + str(details[2]) +
                          '\t' + "Rs " + str(details[3]) + '\t' + str(details[4]) + '\n')
            sn += 1
        invoice.write("-" * 80)
        invoice.write("\n")
        invoice.write("Total: Rs "+str(grand_total))
        invoice.write("\n")
        invoice.write("Vat Rate: 13%")
        invoice.write("\n")
        invoice.write("Vat Amount: Rs "+str(grand_total*0.13))
        invoice.write("\n")
        invoice.write("=" * 80)
        invoice.write("\n")
        invoice.write("Grand Total: Rs "+str(grand_total+grand_total*0.13))
        invoice.write("\n")
        invoice.write("=" * 80)

