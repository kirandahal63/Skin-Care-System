from operations import display_products
from operations import selling_product
from operations import restocking_products
#This is a main function which deals with user interface
def main():
    """
    Main function to run the system interface which presents a menu for the admin to
    display products, sell items, restock inventory, or exit.It handles user input and
    calls the corresponding functions from the operations module.

    Parameter: None
    
    Returns: None

    Example:
    >>> main()
    ================================================================================
                                    Welcome to WeCare !!!
    ================================================================================ 

     1. Display Products
     2. Sale item
     3. Restock
     4. Exit
     Enter your choice: 4


    ================================================================================
                            Thank you for using our system!!
    ================================================================================
    
    """
    print('='*80)
    print(" \t\t\t\tWelcome to WeCare !!!")
    print('='*80,'\n')
    check_loop = True

    while check_loop == True:
        print(" 1. Display Products")
        print(" 2. Sale item")
        print(" 3. Restock")
        print(" 4. Exit")
        try:
            admin_input = int(input(" Enter your choice: "))
            print("\n")
            if admin_input == 1:
                display_products(2)
            elif admin_input == 2:
                selling_product()
            elif admin_input == 3:
                restocking_products()
            elif admin_input == 4:
                print("=" * 80)
                print(" \t\t\tThank you for using our system!!")
                print("=" * 80)
                check_loop = False
            else:
                print("\nInvalid input!!\n")
        except ValueError:
            print("\nPlease select correct options !!!\n")

#Calling main function
main()
