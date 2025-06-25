from Operations import *
from DateAndTime import *
'''====================================================== For creating invoice ====================================================================='''
#Creating invoice when a purchase is made
def createPurchaseInvoice(purchased_items, total_price,name,Phone):
    """
    Generates and saves a purchase invoice to a file based on the provided purchase details.

    This function creates a new text file for each purchase, including customer information, 
    purchased items, and the total bill amount. The file name is generated using the current 
    date and time.

    Parameters:
    purchased_items (list): A list of purchased items, where each item is represented as a list 
                             containing the following elements:
                             - item name (str)
                             - quantity purchased (int)
                             - free quantity (int)
                             - unit price (float)
                             - subtotal (float)
    total_price (float): The total amount for the purchase (sum of all subtotals).
    name (str): The name of the customer making the purchase.
    Phone (str): The phone number of the customer.

    Returns:
    None: This function does not return a value. It writes the purchase details to a text file.

    Raises:
    IOError: If there is an issue writing to the file.

    """
    filename = "Sale" + returnDateandTime() + ".txt" # this creates a filename which is made diffeerent by calling date and time wala function
    
    f = open(filename,"w")# writing file mode
    # Creating invoice
    f.write("\n" + "="*70 + "\n")
    f.write("               SALE-INVOICE                     \n")
    f.write("="*70 + "\n")
    f.write("\nName: "+ name)
    f.write("\nPhone No. "+  Phone)
    f.write("\n"+returnDateandTime() + "\n")
    f.write("Item\t\tQty\tFree\tUnit Price\tSubtotal\n")
    f.write("-"*70 + "\n")
    # loop starts and ends when all the list of items that has been bought are printed in invoice
    for item in purchased_items:
        f.write(item[0] + "\t" + str(item[1]) + "\t" + str(item[2]) + "\t" + str(item[3]) + "\t\t" + str(item[4]) + "\n")
        
    f.write("-"*70 + "\n")
    f.write("Total Bill Amount :\t\t\t\t" + str(total_price) + "\n")
    f.write("="*70 + "\n")
    f.write("Thanks for shopping\n")
    f.write("="*70 + "\n\n")
    print("="*70)
    print("Sale invoice Reciept created")
    print("="*70)
    
    f.close() #closing file
    
def write_in_main_text_file(item_dict):
    """
    Writes the current item data to a text file.

    This function saves the contents of the `item_dict` dictionary to a text file named 
    `itemData.txt`. Each item is written as a comma-separated line, where each line represents
    the details of a single item.

    Parameters:
    item_dict (dict): A dictionary containing item details, where the keys are item IDs 
                       (integers) and the values are lists containing:
                       - item name (str)
                       - item brand (str)
                       - item quantity (str)
                       - item price (str)
                       - item country of origin (str)

    Returns:
    None: This function does not return any value. It writes the item data to a text file.

    Raises:
    IOError: If there is an issue opening or writing to the file.
    """
    f= open("itemData.txt", "w")
    for key in item_dict:
        item = item_dict[key]
        line = item[0] + "," + item[1] + "," + item[2] + "," + item[3] + "," + item[4] + "\n"
        f.write(line)

    
    
# Creating invoice after restocking exisiting item
def createRestockInvoice(restockedItems):
    """
    Generates and saves a restock invoice to a text file.

    This function creates a unique restock invoice file by including details of the 
    restocked items such as their name, quantity, old price, and new price. The file name 
    is generated using the current date and time.

    Parameters:
    restockedItems (list): A list of restocked items, where each item is represented as a list 
                            containing the following elements:
                            - item name (str)
                            - quantity restocked (int)
                            - old price (float)
                            - new price (float)

    Returns:
    None: This function does not return a value. It writes the restock details to a text file.

    Raises:
    IOError: If there is an issue writing to the file.
    """
    filename = "restock" + returnDateandTime() + ".txt" # creating unique file name

    f = open(filename, "w") # file opening in writing mode to create a file
    f.write("                     RESTOCK-INVOICE                    \n")
    f.write("=" * 70 + "\n")
    f.write(returnDateandTime() + "\n")
    f.write("Item\t\t\tQuantity\tOldPrice\tNewPrice\n")
    f.write("-" * 70 + "\n") 

    # this loop goes for all the list of the item restocked 
    for item in restockedItems:
        #writing in the file
        f.write(item[0] + "\t\t" + str(item[1]) + "\t\t" + str(item[2]) + "\t\t" +str(item[3])+  "\n")
    f.write("-" * 70 + "\n")
    f.write("Restocking Process Completed.\n")
    f.write("=" * 70 + "\n")
    print("="*70)
    print("Restock Invoice Created Successfully.")
    print("="*70)
    f.close()

    # invoice when a new item is added 
def createAddInvoice(addedItems):
    """
    Create an invoice for the items added to the inventory and save it as a text file.

    Summary:
    This function generates a detailed invoice for newly added items, including their names, brands, quantities, prices, and countries.
    The invoice is saved as a text file with a unique name based on the current date and time.

    Parameters:
    addedItems (list): A list of lists, where each sublist represents an item and contains:
        - Item Name (str)
        - Brand (str)
        - Quantity (int)
        - Price (int or float)
        - Country (str)

    Returns:
    None

    Raises:
    IOError: If there is an issue with file handling (e.g., unable to open or write to the file).
    Exception: For any unforeseen errors during invoice creation or file operations..
    """
    filename = "Adding" + returnDateandTime() + ".txt" #This is to make a new unique file name as same file cannot be created 

    f = open(filename, "w") # opening file in write mode 
    f.write("                     ADDED INVOICE                     \n")
    f.write("=" * 70 + "\n")
    f.write(returnDateandTime() + "\n")
    f.write("Item\t\t\tBrand\tQuantity\tPrice\tCountry\n")
    f.write("-" * 70 + "\n") 
    # loop to print every item in the list
    for item in addedItems:
        
        f.write(item[0] + "\t\t" + item[1] + "\t" + str(item[2]) + "\t\t" + str(item[3]) + "\t" + item[4] + "\n")


    f.write("-" * 70 + "\n")
    f.write("Adding Process Completed.\n")
    f.write("=" * 70 + "\n")
    print("="*70)
    print("Added Invoice Created Successfully.")
    print("="*70)
    #closing the file
    f.close()

'''====================================================================Creating Invoice END ========================================================'''
