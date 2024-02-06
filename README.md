Warehouse Management Software 

This project consists in realizing a software for the management of a market warehouse. The software has the following features:

- register new products, with name, quantity, sale price and purchase price;
- list all the available products;
- record the sales made;
- show the gross and net profits;
- show a help menu with all the available commands.

The available commands are:

- **add**: adds a product to the warehouse;
- **list**: lists the products in the warehouse;
- **sell**: records a sale made;
- **profits**: shows the gross and net profits;
- **help**: shows the available commands;  
- **close**: quits the program. 

The program creates a file, `store.json`, which keep track of the products in the warehouse and the sales.<br> 

Furthermore, user input validation is performed: it checks that quantity is an integer positive number, prices are float positive numbers and performs a case-insensitive comparison between the names of the products in the warehouse and the ones entered by the user.
