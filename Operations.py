#importing Read module which reads the txt file
from Read import toread  
from DateAndTime import returnDateandTime
from Write import *
from Messages import *

item_dict = toread()
'''================================================This is the section is for option 1 ============================================================='''
#function to display Product Details
def displayMP(item_dict):
    """
    Display the details of all products in a tabular format.

    Summary:
    Prints a formatted table containing each product's ID, name, brand, stock quantity, marked price, and country of origin.

    Parameters:
    item_dict (dict): A dictionary containing product data with item IDs as keys. Each value is a list in the format:
        [product_name (str), brand_name (str), stock (int), price (int or str), country (str)]

    Returns:
    None

    Raises:
    TypeError: If item_dict is not a dictionary or if its values are not lists with the expected structure.

    """
    print("ID \t Product \t\t Brand \t\t Stock \t Price\t Country")
    print("="*80)
    for key, value in item_dict.items(): # loop for printing all the lines
        product_name = value[0] #Getting product name
        brand_name=value[1] #Getting Brand name
        stock=value[2] #Getting Quantity
        cost_price = int(value[3])  # Getting marked price
        country = value[4] #Getting country 
        print(key ,"\t", product_name,"\t\t", brand_name ,"\t", stock,"\t",cost_price,"\t",country) 
    print("="*80)
        
def displaySP(item_dict):
    """
    Display the selling price details of all products in a tabular format.

    Summary:
    Prints a formatted table displaying each product's ID, name, brand, stock, selling price (calculated as double the marked price), and country of origin.

    Parameters:
    item_dict (dict): A dictionary containing product data with item IDs as keys. Each value is a list structured as:
        [product_name (str), brand_name (str), stock (int), price (int or str), country (str)]

    Returns:
    None

    Raises:
    TypeError: If item_dict is not a dictionary or if any value list contains incompatible types (e.g., non-integer price).

    """
    print("ID \t Product \t\t Brand \t\t Stock \t Price\t Country")
    print("="*80)
    for key, value in item_dict.items():# this loop is required to print all lines
        product_name = value[0] #Getting product name
        brand_name=value[1] #Getting Brand name
        stock=value[2] #Getting Quantity
        cost_price = int(value[3])  # Getting marked price
        price = cost_price * 2  # Calculating Selling price
        country = value[4] #Getting country
        print(key ,"\t", product_name,"\t\t", brand_name ,"\t", stock,"\t",price,"\t",country)
    print("="*80)

def DisplayProductDetails():
    """
    Prompt the user to choose between viewing products with marked price or selling price and display accordingly.

    Summary:
    Interactively prompts the user to select between displaying product details with either marked price or selling price.
    Based on the user's input, it calls the appropriate function (`displayMP` or `displaySP`) to print product data.

    Parameters:
    None

    Returns:
    None

    Raises:
    ValueError: If the user enters a non-integer input.
    
    Example:
    >>> DisplayProductDetails()
    Enter 1 for displaying price marked price
    Enter 2 for displaying price in Selling Price
    : 1
    (Displays product details with marked price)
    """
    while True:
        sp_or_mp=int(input("Enter 1 for displaying price marked price\nEnter 2 for displaying price in Selling Price\n : "))
        print("="*80)
        #Condition for displaying products in marked price
        if sp_or_mp == 1:
            displayMP(item_dict)
            break
            
        #Condition for displaying products in selling price
        elif sp_or_mp == 2:
            displaySP(item_dict)
            break
            
        else:
            print("Choose a valid option")


'''==================================================== Option 1 Section Ends Here ================================================================='''
'''================================================This is the section is for option 2 ============================================================='''
'''++++++++Main Purchase Function++++++'''
#Creating function for purchasing
def purchase():
    """
    Handle the process of purchasing products, updating inventory, and generating an invoice.

    Summary:
    This function allows a customer to purchase one or more products. It validates stock, applies a "buy 3 get 1 free" offer,
    updates the inventory, records the purchase, and finally generates and displays an invoice for the transaction.

    Parameters:
    None

    Returns:
    None

    Raises:
    ValueError: If the user inputs a non-integer product ID or quantity.
    KeyError: If the provided product ID does not exist in item_dict.
    Exception: For any unforeseen errors during the purchase process.

    Example:
    >>> purchase()
    Enter Customers name: Alice
    Enter Phone number: 1234567890
    (Displays product list)
    Enter the ID of the product that is being purchased: 101
    Enter the quantity of Face Wash by Clean&Clear: 4
    Hello, Alice As you have bought 4. Our policy of buy 3 get one free gives you 1 for free.
    (Displays updated stock and invoice)
    Thank you for shopping with us!
    """
    
    purchased_items = [] # this is the list for holding the items purchased by customer
    total = 0 # Total bill

    #Take information of the User
    name = input("Enter Customers name: ")
    Phone = input("Enter Phone number: ")

    #Making entering phone number optional
    if Phone == "":
        Phone = "No Phone Number Added"

    #The purchase option will also run in loop
    while True:
        try:
            displaySP(item_dict)
            print("="*50)
            #take product ID of the required product
            productID = int(input("Enter the ID of the product that is being purchased: "))
            
            #Validating the entered product ID
            while productID <=0 or productID >=len(item_dict)+1:
                print("product ID is invalid")
                print("\n")
                productID = int(input("Enter valid ID of the product that is being purchased: "))
                
            #take quantity of the product to be purchased
            productQty = int(input("Enter the quantity of "+ item_dict[productID][0]+" by "+item_dict[productID][1] + ": "))
            while productQty <=0:
                print("You cannot enter negative value or 0")
                productQty = int(input("Enter the quantity of "+ item_dict[productID][0]+" by "+item_dict[productID][1] + ": "))

            #Calculate  free items ( Buy 3 get 1 Free)
            availableQty = int(item_dict[productID][2]) #available Quantity in stock
            freeItem = productQty // 3 # free item obtained after buying item
            totalItemGone = freeItem + productQty #total item that going out

            #Validating available stocks
            while totalItemGone > availableQty:
                print("Not enough Item in stock")
                print("\n")
                productQty = int(input("Enter less quantity of "+ item_dict[productID][0]+", available Quantity is "+item_dict[productID][2] + ": "))
                #Recalculating item that is going out
                freeItem = productQty // 3
                totalItemGone = freeItem + productQty
            print("\n")

            #Message to show when get the offer
            if(productQty >= 3):
                print("Hello,", name, "As you have bought", productQty, ". Our policy of buy 3 get one free gives you", freeItem, "for free.")

            #Now Updating stock
            item_dict[productID][2] = str(int(item_dict[productID][2]) - totalItemGone)
            print("\n")

            #Display Updated Stock
            print("Stock Successfully Updated")
            displaySP(item_dict)

            #For Generating invoice
            # At the end of successful purchase
            subtotal = int(item_dict[productID][3]) * 2 * productQty
            # Appending details in purchased_items list for printing it in invoice
            purchased_items.append([item_dict[productID][0], productQty, freeItem, int(item_dict[productID][3]) * 2, subtotal])
            total += subtotal

            #write in main file
            write_in_main_text_file(item_dict)
            
            #Ask if customer wants to continue 
            print("Do you want to buy Another Item (Y/N)")
            decision = input("Enter Y/N")
            if( decision.lower() == 'n'):
                print("\n" + "="*70)
                print("INVOICE")
                print("="*70)
                print(returnDateandTime())
                print("Item\t\tQty\tFree\tUnit Price\tSubtotal")
                print("-"*70)

                total_price = 0
                for item in purchased_items:
                    name = item[0]
                    qty = item[1]
                    free = item[2]
                    price = item[3]
                    subtotal = item[4]
                    print(name + "\t" + str(qty) + "\t" + str(free) + "\t" + str(price) + "\t\t" + str(subtotal))
                    total_price += subtotal
                print("-"*70)
                print("Total Amount Payable:\t\t\t\t", total_price)
                print("="*70)
                print("Thank you for shopping with us!")

                print("\n" + "="*70)
                createPurchaseInvoice(purchased_items, total,name,Phone)#Create invoice file 
                break

            
        except Exception as e:
            print("Error 404, Invalid input:", e)
'''++++ purchase function ends+++++'''


'''==================================================== Option 2 Section Ends Here ================================================================='''

'''================================================This is the section is for option 3 ============================================================='''

'''++++++++Main Restock Function++++++'''
#defining restock product program

def restockProduct():
    """
    Manages the restocking or adding of products to the inventory.

    This function continuously prompts the user for restocking options, either to restock an existing item
    or to add a new item. It handles errors related to invalid inputs and ensures that the user is guided
    to make valid choices.

    Parameters:
    None

    Returns:
    None: This function doesn't return any value. It only manages the restocking and adding process.

    Raises:
    Exception: If any unexpected error occurs while taking user input or during the restocking process,
    the exception is caught, and an error message is displayed.

    """
    print("Restocking WeCare")
    print("\n")
    while True: #Even this function will run in loop
        try: #exception handeling for handeling unfortunate errors
            restockMessage()#  Display restocking message
            restockOption = int(input("Enter your option 1 or 2 : "))#choose your option from here 
            
            displayMP(item_dict)
            if(restockOption == 1):#choose restocking option 
                restockItem(item_dict)
            elif(restockOption == 2):
                addItem(item_dict)
            else:
                print("Please select the correct option")
            continueRestocking = input(" Do you want to continue restocking another item? (Y/N)")
            if(continueRestocking.lower() == 'n'):
                print(" You have been exited from the Restocking section")
                break
            
        except Exception as e:
            print("Error 404, Invalid input:", e) # Catch and print any input errors

'''++++ Restock function ends+++++'''
'''++++ Actual Restocking codes functions++++'''
'''For restocking options'''

# THis is for restocking existing items
def restockItem(item_dict):
    """
    Restocks products by updating the stock quantity and optionally changing the price.

    Parameters:
    item_dict (dict): A dictionary representing the items in the inventory. Each key is a product ID,
                      and the value is a list containing item details such as:
                      - item name (str)
                      - item description (str)
                      - stock quantity (str)
                      - price (str)

    Returns:
    None: This function doesn't return any value. It modifies the `item_dict` in place and generates a restock invoice.

    Raises:
    ValueError: If invalid input is entered for product ID, quantity, or price.

    """
    restockedItems = [] # this stores the stocked items in list

    
    while True:
        productID = int(input("Enter the ID of the product you want to restock")) #Take product ID
        #Validating the entered product ID
        while productID <=0 or productID >=len(item_dict)+1:
            print("product ID is invalid")
            print("\n")
            productID = int(input("Enter valid ID of the product that is being purchased: "))
            
        newPrice = item_dict[productID][3]
        oldPrice = item_dict[productID][3]

        print("you are restocking" + item_dict[productID][0])
        print("\n")
        
        restockProductQty = int(input("How many products are you adding?")) # takes the qty to be restocked

        #Updating Stock
        item_dict[productID][2] = str(int(item_dict[productID][2]) + restockProductQty)

        #Ask if the user wants to update price as well
        changePrice = input("Do you want to change the price? Y/N").lower()
        if changePrice == 'y':
            newPrice = input("Enter new price")
            item_dict[productID][3] = newPrice
            

        #Restocked Successfull message
        print("Restock Successfull")

        # At the end of successful restock
        restockedItems.append([item_dict[productID][0], restockProductQty,oldPrice,newPrice])

        write_in_main_text_file(item_dict)
        #Ask the user for restocking another item as well?
        restockAgain=input("\n Do you want to add another product? (Y/N)")

        #checks if the user wants to stop restocking than generates invoice
        if(restockAgain.lower() == 'n'):
            createRestockInvoice(restockedItems)#calling function to restock invoice
            print("\n" + "=" * 70)
            print("RESTOCK INVOICE")
            print("=" * 70)
            print("Item\t\tQty\tOld Price\tNew Price")
            print("-" * 70)

            for item in restockedItems:
                name = item[0]
                qty = item[1]
                old_price = item[2]
                new_price = item[3]
                print(name + "\t" + str(qty) + "\t" + str(old_price) + "\t\t" + str(new_price))

            print("=" * 70)
            print("Thank you for restocking with us!")
            print("=" * 70)
            break

#This is for adding item with details
def addItem(item_dict):
    """
    Adds a new item to the inventory and records it in a file.

    This function allows the user to input details of a new product, such as name, brand, quantity, price, and country.
    The product is then added to the inventory with a new unique ID, and the details are saved both to an in-memory dictionary
    and a file ("itemData.txt"). The function allows multiple items to be added, and generates an invoice when the user finishes adding items.

    Parameters:
    item_dict (dict): A dictionary where the key is the product ID and the value is a list containing product details
    (name, brand, quantity, price, country).

    Returns:
    None: This function doesn't return any value. It modifies the `item_dict` and writes data to a file.

    Raises:
    None: This function doesn't raise any exceptions, but handles user inputs and file operations safely.


    """
    addedItems = [] # Stores the added Items with detail in list 
    while True: # loop starts 
        productID = 1 #intializing product id
        
        '''starts loop and increments the value of product ID to obtain the
            id number one more than the exisitng lines in the text file'''
        while productID in item_dict:
            productID += 1

        # Get item details
        name = input("Enter product name: ")
        brand = input("Enter brand: ")
        quantity = input("Enter quantity: ")
        price = input("Enter price: ")
        country = input("Enter country: ")

        # Create new item list to store the detail of the item to be added to the inventory
        new_item = [name, brand, quantity, price, country]

        # Adding to main dictionary
        item_dict[productID] = new_item

            # Append the line in the file
        with open("itemData.txt", "a") as file:
            for i in range(len(new_item)):
                if i == len(new_item) - 1: # checks that the detail is the last item or not
                    file.write(new_item[i] + "\n")  # Add newline at the end
                else:
                    file.write(new_item[i] + ",")  # Add a comma between items

        print("Item added successfully!")
        # At the end of successful add
        addedItems.append([item_dict[productID][0],item_dict[productID][1],item_dict[productID][2],item_dict[productID][3],item_dict[productID][4]])

        addAgain = input("\n Do you want to add another product? (Y/N)") # to know to add another product or not
        
        if(addAgain.lower() == 'n'): # check if the user wants to stop adding
            createAddInvoice(addedItems) # Creates invoice 
            break               

'''END RESTOCK'''


'''==================================================== Option 3 Section Ends Here ================================================================='''

