#importing other modules
from Messages import *
from Read import toread  
from Operations import DisplayProductDetails,displaySP,purchase,restockProduct

#Defining Main function
def main():
    """
    This is the main function of the stock management system of WeCare

    Summary:
    This function is the entrance of the program.
    It pops the welcome message.
    loading the existing product data, and provision of constant navigation options to the user.
    Based on user input, it enables displaying product details, purchase of goods, restock of goods, or an exit from the program.
    Parameters:
    None

    Returns:
    None

    Raises:
    ValueError: Raised if the user inputs a non-integer when prompted for an option.
    Other unexpected exceptions may occur during function calls, depending on their implementations.

    Example:
    >>> main()
    Welcome to the system!
    ----- Menu -----
    1. Display product details
    2. Purchase product
    3. Restock product
    4. Exit
    Enter any one of the options 1-4: 2
    (Runs purchase logic)
    """
    #Calling the Welcome Message function
    welcomeMessage()
    item_dict = toread()
    while True: #This loop runs the program in loop unless the user wants to terminate
        navFeatures()#calling a navFeatures function which displays the options that can be done by this programme
        try:# This is for handeling unfortunate crashing of the programme
            optionChoice = int(input("Enter any one of the options 1-4: "))
            '''Below is the conditional statements which matches with the user input and does the task on the basis of option chosen'''
            if(optionChoice == 1):
                DisplayProductDetails() # calling Diplay product Details function to display the items 
            elif(optionChoice == 2):
                
                purchase() # calling purchase function which is used while making a sale
            elif(optionChoice == 3):
                print("option2")
                restockProduct()# Add stock to existing products
            elif(optionChoice == 4):
                print("Exitted from the system, Thank you!!")# Pops exit message
                break
            else:
                print("Please enter valid option (1/2/3/4)")
        except:
            print("Error 404, Invalid input")#Invalid option warning

#Calling main function here
main()
