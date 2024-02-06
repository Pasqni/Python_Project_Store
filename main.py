from _store_management import *

if __name__ == "__main__":
    
    cmd = None
    
    """
    Creates an instance of the Store object
    """
    
    store = Store()

    while cmd!="close":

        cmd = input("Digit a command: ").lower()

        if cmd=="sell":
            
            """
            Checks the availability of a product and its quantity
            Records a sale
            """
            store.sale()

        elif cmd=="profits":
            
            """
            Shows gross and net profits
            """
            
            store.profits()
            
        elif cmd=="add":
            
            """
            Adds a product
            """
            store.add_to_store()
            
        elif cmd=="list":
            
            """
            Lists registered products
            """

            store.itemize()
            
        elif cmd=="help":
            
            """
            Prints available commands
            """
            help_me()
            
        elif cmd=="close":
            
            """
            Prints greetings and exits the program
            """
            
            print("Bye bye")
            break

        else:
            
            """
            Invalid command entered
            Prints help message
            """

            print("Invalid command")
            help_me()