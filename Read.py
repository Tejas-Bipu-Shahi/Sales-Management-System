'''+++++++++++++++++ Reading text file ++++++++++++++++++++'''
def toread():
    """
    Reads product data from a file and returns a dictionary representing the inventory.

    This function reads product details from a text file (`itemData.txt`), processes each line, 
    and stores the data in a dictionary where the keys are item IDs and the values are lists of item details.

    Parameters:
    None

    Returns:
    dict: A dictionary containing item details, where the keys are item IDs (integers) 
          and the values are lists containing the following information:
          - item name (str)
          - item brand (str)
          - item quantity (str)
          - item price (str)
          - item country of origin (str)

    Raises:
    IOError: If there is an issue opening or reading the file.
    FileNotFoundError: If the file `itemData.txt` does not exist.
    """
    item_dict = {}#initializing dictionary named as item_dict

    file = open("itemData.txt", "r")#Opening txt file on read mode

    # Reading all lines from the file and store them in a list details
    details = file.readlines()

    # Initialize item_id and start dictionary keys from 1
    item_id = 1

    # Loop through each line in the file
    for line in details:
        # Remove the newline character and split the line by commas
        line = line.replace("\n", "").split(",")
        # Storing the resulting list in a dictionary with item_id as the key
        item_dict[item_id] = line
        # Increment the item_id key for the next item
        item_id = item_id + 1

    # Close the file after reading is complete
    file.close()
    return item_dict

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
