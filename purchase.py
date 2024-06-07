
class ItemToPurchase: 

    # Constructor
    def __init__(self, name = "none", price = 0.0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    # function used to print the total cost of each item
    def print_item_cost(self):
        total_cost = round(self.price * self.quantity)
        print("{} {} @ ${} = ${}".format(self.name, self.quantity, self.price, total_cost))

def main():

        # user inputs item 1 name, price, and quantity
        print("Item 1")
        item_one_name = input("Enter the item name: \n")
        item_one_price = int(input("Enter the item price: \n"))
        item_one_quantity = int(input("Enter the item quantity: \n"))

        # user inputs item 2 name, price, and quantity
        print("Item 2")
        item_two_name = input("Enter the item name: \n")
        item_two_price = int(input("Enter the item price: \n"))
        item_two_quantity = int(input("Enter the item quantity: \n"))

        # item one and item two object created by passing the name, price, and quantity as the argumentes
        item_one = ItemToPurchase(item_one_name, item_one_price, item_one_quantity)
        item_two = ItemToPurchase(item_two_name, item_two_price, item_two_quantity)

        # calculate total cost of all items 
        total_cost = round((item_one.price * item_one.quantity) + (item_two.price * item_two.quantity))

        # print the total cost of the items
        print("TOTAL COST")
        item_one.print_item_cost()
        item_two.print_item_cost()
        print("Total: ${}".format(total_cost))

if __name__ == "__main__":
     main()    

        