#importing datetime functin from datetime module 
from datetime import datetime

#Creating a function to read product_inventory.txt text file and return details using dict
def read_products_fromfile():
    """
    Reads product information from 'product_inventory.txt' text file containing product details,
    processes each line to extract information,and stores it in a nested dictionary where each
    key is a product name and its value is another dictionary containing brand, quantity, price, and origin.

    Parameters: None

    Returns:
    dict: A dictionary containing product information with the following key and value pair:
        - Key (str): The name of the product.
        - Value (dict): A nested dictionary with the following keys:
            - 'brand' (str): The brand of the product.
            - 'quantity' (int): The quantity of the product.
            - 'price' (int): The cost price of the product.
            - 'origin' (str): The origin location of the product.

    Raises:
    FileNotFoundError: If the file 'product_inventory.txt' does not exist or troubleshoot to access it.

    Example:
    >>> d = 
    {
        'Vitamin C Serum': {'brand': 'Garnier', 'quantity': 250, 'price': 1200, 'origin': 'France'},
        'Skin Cleanser': {'brand': 'Cetaphil', 'quantity': 84, 'price': 280, 'origin': 'Switzerland'},
        'Sunscreen': {'brand': 'Aqualogica', 'quantity': 200, 'price': 750, 'origin': 'India'}
    }
    """
    #creating empty dictionary
    d = {}
    
    #handling exceptions using try, except keyword
    try:
        
        #operations to open text file and store in dictionary 'd'
        with open("product_inventory.txt", "r") as file:
            #iterate over each lines of file
            for line in file:
                product, brand, quantity, cp, origin = line.replace("\n", "").split(",")
                #defining type of variable 
                cp = int(cp)
                quantity = int(quantity)

                ''' Updating dictionary with product name as key and store other details values
                    This is an exaple of nested dictionary.'''
                d[product] = {'brand': brand, 'quantity': quantity, 'price': cp, 'origin': origin}

            #returning dictionary
            return d
    except FileNotFoundError:
        #printing suitable message in case of exception is occured
        print("File not Found")
        
        
#This function create a custom date format and return it
def date():
    """
    Generate and return the current date using the datetime module and time in a custom 'YYYY/MM/DD HH:MM:SS' format.

    Parameters: None

    Returns:
    str: A string representing the current date and time in the format 'YYYY/MM/DD HH:MM:SS'.

    Raises:
    None

    Example:
    >>> date()
    '2025/05/10 14:23:45'
    """
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    minute = datetime.now().minute
    second  = datetime.now().second
    date_of_transaction = str(year) + '/' + str(month) + '/' + str(day) + ' ' +str(hour) + ':' + str(minute) + ':' + str(second)
    
    return date_of_transaction
