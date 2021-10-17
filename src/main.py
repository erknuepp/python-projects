# Program header goes here
# Author: Stephani
# 
# Description: Order System
import json


def part_exists(requested_part:str, parts:list):
    """
    Checks to see if the requested part
    exists in inventory.

    Keyword arguments:
    requested_part:str -- The requested part.
    parts:list -- The available parts.
    """
    return requested_part.lower() in parts

def is_positive_integer(string:str) -> bool:
    """
    Checks to see if the requested value is a positive integer.
    
    Keyword arguments:
    value:str -- The value to check.
    """
    try:
        value = int(string)
        return value >= 0
    except ValueError:
        return False

def get_part_quantity(part:str, data:dict) -> int:
    """
    Gets the quantity for the specfied part.
    
    Keyword arguments:
    part:str -- The part to get the quantity of.
    data:dict -- The dictionary.
    """
    return int(data.get(part).get("quantity"))

def get_part_value(part:str, data:dict) -> int:
    """
    Gets the value for the specfied part.
    
    Keyword arguments:
    part:str -- The part to get the value of.
    data:dict -- The dictionary.
    """
    return int(data.get(part).get("value"))

def get_input(message:str) -> str:
    """
    Gets an input from the user with an input message.
    
    Keyword arguments:
    message:str -- The input message.
    """
    response = ""
    try:
        response = input(message)
    except:
        pass 
    return response

def print_order(order:dict):
    '''
    Prints the order to the terminal.
    
    Keyword arguments:
    order:dict -- The order to print.
    '''
    print("Your order\n")
    total = 0.0
    part_dict:dict
    for part, part_dict in order.items():
        quantity = int(part_dict.get("quantity"))
        price = float(part_dict.get("price"))
        subtotal = price * quantity
        if quantity > 0:
            print(part, "-", quantity,"@", price,"=", round(subtotal,2),"\n")
            total += subtotal
       ##END IF### 
    ###END FOR###
        
    print("Total: $" + str(round(total,2)) + "\n")
    print("Thank you for using the parts ordering system!\n")
###END print_order###

supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'

# Cheap and easy, but bad practice TODO make a way to create this order dictionary properly to maintain data integrity if supplier changes price
order_data = '{"sprocket": {"price": 3.99, "quantity": 0}, "gizmo": {"price": 7.98, "quantity": 0}, "widget": {"price": 14.32, "quantity": 0}, "dodad": {"price": 0.5, "quantity": 0}}'

###PROGRAM START###
inventory_dict = json.loads(supplier_data)

# The order data MUST be stored in a dictionary. 
order_dict = json.loads(order_data)
print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity\n")
print("Parts for order are:\n")
for part in inventory_dict.get("parts"):
    print(part,"\n")

filling_order = True
while(filling_order):
    suborder_part = ""
    suborder_quantity = 0
    #Prompt the user for input, and indicate they can enter in the word “quit” to quit. 
    # The user should enter in a part and then the quantity on two separate lines (so you’ll need two input statements). 
    
    part_input_str = get_input("Enter a part (quit to Quit):\n")
    if part_input_str.lower() == "quit":
        filling_order = False
        break #To display the full order **TODO**
    while(not part_exists(part_input_str, inventory_dict)): # Check to see if the requested part exists
        print(part_input_str, "does not exist.\n")
        part_input_str = get_input("Enter a part (quit to Quit):")
    
    
    order_quantity_input_str = get_input("Enter a quantity:")

    while(not is_positive_integer(order_quantity_input_str)): # Check that quantity is a positive integer
        print("The quantity must be a positive integer.\n")
        order_quantity_input_str = get_input("Enter a quantity:")

    suborder_quantity = int(order_quantity_input_str)

    # You must also allow the user to order a part more than once 
    #   and validate that both ordersare not exceeding the total amount available! TODO
    inventory_part_quantity = get_part_quantity(part_input_str, inventory_dict)
    
    order_part_quantity = get_part_quantity(part_input_str, order_dict)
    
    # Check if there is enough of the part in stock to complete the part order
    if inventory_part_quantity - order_part_quantity < suborder_quantity:
        print("Your quantity exceeds the inventory quantity of", inventory_part_quantity, part_input_str + "(s).\n")
        continue
        
    # If the order is valid, 
    #   store it and continue. 
    order_dict[part_input_str]["quantity"] = suborder_quantity + order_part_quantity

#END While loop to fill order


# Once the user enters quit, 
#   print out an order summary showing the part, 
#   number ordered, 
#   the price per part 
#   and total per part 
#   with a grand total at the end. 
print_order(order_dict)
###PROGRAM END###
