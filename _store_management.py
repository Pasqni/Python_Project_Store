import json

class Product:
    
    """
    Defines the characteristics of a product
    """
    
    def __init__(self, name, quantity, purchase_price, sale_price):
        self.name = name
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        
    def to_dict(self):
        return self.__dict__
        

class Store:
    
    """
    Defines a Store object and the available actions
    """
    
    def __init__(self):
        self.products = []
        self.sales = []
        self.load_data()
        
    def load_data(self):
        
        """
        Reads data from the JSON file
        """
        
        try:
            with open('store.json', 'r') as json_file:
                data = json.load(json_file)
                self.products = [Product(**product) for product in data.get('products', [])]
                self.sales = [Product(**sales) for sales in data.get('sales', [])]
        except FileNotFoundError:
            pass

    def save_data(self):
        
        """
        Writes data to the JSON file
        """
        
        with open('store.json', 'w') as json_file:
            json.dump({
                'products': [product.to_dict() for product in self.products],
                'sales': [sale.to_dict() for sale in self.sales]
            }, json_file)

    
    def sale(self):
        
        """
        Checks the availability of a product
        Records the product as sold
        Prints a summary of sales and the total
        Adds sales to the JSON file
        """
        
        tmp_sales = []
        while True:
            found = False
            name = input("Product name: ").lower()
            for product in self.products:
                if product.name == name:
                    found = True
                    if found:
                        try:
                            quantity = int(input("Quantity: "))
                            if quantity > 0:
                                if product.quantity >= quantity:
                                    product.quantity -= quantity
                                    p_price = product.purchase_price
                                    s_price = product.sale_price
                                    product_to_sell = Product(name, quantity, p_price, s_price) 
                                    self.sales.append(product_to_sell)
                                    tmp_sales.append(product_to_sell)
                                else:
                                    print("Quantity not available")
                            else:
                                print("Quantity must be greater than 0")
                        except ValueError:
                            print("Invalid quantity entered")
                            break
            if found == False:
                print("Entered product is not available")
            if input("Sell another product ? (yes/NO):").lower() != 'yes':
                break
        Total = sum([sale.sale_price*sale.quantity for sale in tmp_sales])
        if Total > 0:
            print("VENDITA REGISTRATA")
            for sale in tmp_sales:
                print(f'- {sale.name} X {sale.quantity}: €{sale.sale_price:.2f}')
            print(f"Total: €{Total:.2f}")
        Store.save_data(self)
        tmp_sales = []

    def profits(self):
        
        """
        Calculates and display gross and net profits (totals)
        """
        
        gross_profit = sum([v.sale_price*v.quantity for v in self.sales])
        net_profit = gross_profit - sum([v.purchase_price*v.quantity for v in self.sales])
        print(f'Gross profits: {gross_profit:.2f}, Net profits: {net_profit:.2f}')

    def add_to_store(self):
        
        """
        Adds a new product or increases the quantity of an existing one
        Adds the product to the JSON file
        """
        
        name = input("Product name: ").lower()
        if name.isalpha():
            for product in self.products:
                if product.name == name:
                    try:
                        quantity = int(input("Quantity: "))
                        if quantity > 0:
                            product.quantity += quantity
                            break
                        else:
                            print("Quantity must be greater than 0")
                            break
                    except ValueError:
                        print("Invalid quantity entered")
                        break
            else:
                try:
                    quantity = int(input("Quantity: "))
                    purchase_price = float(input("Purchase price: "))
                    sale_price = float(input("Sale price: "))
                    if quantity > 0 and purchase_price > 0 and sale_price > 0: 
                        product_to_add = Product(name, quantity, purchase_price, sale_price)
                        self.products.append(product_to_add)
                    else:
                        print("Quantity and prices must be greater than 0")
                except ValueError:
                    print("Invalid quantity entered")
        else:
            print("Invalid product name. Numbers are not allowed")
        Store.save_data(self)

    def itemize(self):
        
        """
        Lists registered products, their quantities, and their prices
        """
        
        print("PRODUCT QUANTITY PRICE")
        for product in self.products:
            print(f'{product.name} {product.quantity} {product.sale_price:.2f}')

def help_me():
    
    """
    Lists the commands accepted by the program
    """
    
    accepted_commands = ["- add: adds a product to the warehouse",
                         "- list: lists the products in the warehouse",
                         "- sell: records a sale made",
                         "- profits: shows the gross and net profits",
                         "- help: shows the available commands",
                         "- close: exit the program"]

    print("Available commands are:")
    for command in accepted_commands:
        print(command)

        

