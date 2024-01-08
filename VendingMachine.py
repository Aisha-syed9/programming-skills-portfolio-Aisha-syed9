print('''
███ █┼█ ███ ┼┼ █▄█ ███ █┼┼█ ██▄ ███ █┼┼█ ████ ┼┼ █▄┼▄█ ███ ███ █┼█ ███ █┼┼█ ███
┼█┼ █▄█ █▄┼ ┼┼ ███ █▄┼ ██▄█ █┼█ ┼█┼ ██▄█ █┼▄▄ ┼┼ █┼█┼█ █▄█ █┼┼ █▄█ ┼█┼ ██▄█ █▄┼
┼█┼ █┼█ █▄▄ ┼┼ ┼█┼ █▄▄ █┼██ ███ ▄█▄ █┼██ █▄▄█ ┼┼ █┼┼┼█ █┼█ ███ █┼█ ▄█▄ █┼██ █▄▄''')
class VendingMachine:
    def __init__(self):
        self.vending_machine = {
            'chips': {'Lays': {'price': 3.50, 'quantity': 10}, 'Cheetos': {'price': 4.00, 'quantity': 9},
                      'Potato chips': {'price': 5.50, 'quantity': 15}, 'Oman chips': {'price': 1.50, 'quantity': 20}},
            'snacks': {'Chocolate bar': {'price': 2.50, 'quantity': 12}, 'Granola bar': {'price': 3.00, 'quantity': 10},
                       'Popcorn': {'price': 4.50, 'quantity': 9}, 'Protein bar': {'price': 3.45, 'quantity': 14}},
            'drinks': {'Soda': {'price': 2.00, 'quantity': 18}, 'Water': {'price': 1.50, 'quantity': 20},
                       'Juice': {'price': 3.00, 'quantity': 15}, 'Barbican': {'price': 5.00, 'quantity': 10}}
        }
        self.money_in_machine = 50.0
        self.transaction_history = []

    def display_menu(self):
        print("Welcome to the Vending Machine!")
        print("\nCategories available:")
        for category in self.vending_machine:
            print(f"- {category.capitalize()}")

        selected_category = input("\nPlease select a category (chips/snacks/drinks): ").lower()

        if selected_category in self.vending_machine:
            print(f"\nItems available in {selected_category.capitalize()}:")
            for item, details in self.vending_machine[selected_category].items():
                print(f"- {item}: AED {details['price']:.2f} ({details['quantity']} left)")

            selected_item = input(f"\nPlease select an item from {selected_category.capitalize()}: ")

            if selected_item in self.vending_machine[selected_category]:
                item_details = self.vending_machine[selected_category][selected_item]
                price_of_item = item_details['price']
                quantity_of_item = item_details['quantity']
                print(f"\nYou have selected {selected_item}. The price is AED {price_of_item:.2f}.")
                print(f"Available Quantity: {quantity_of_item}")

                amount_paid = float(input("\nPlease enter the amount of money (AED) you have: "))

                if amount_paid < price_of_item:
                    print("Sorry, the amount is not enough. Transaction canceled. Returning money.")
                else:
                    change = amount_paid - price_of_item
                    print(f"Thank you for your purchase! Your change is AED {change:.2f}.")
                    self.dispense_item(selected_category, selected_item)
                    self.update_transaction_history(selected_item, amount_paid, change)
                    self.money_in_machine += price_of_item
            else:
                print("Invalid item selection. Please try again.")
        else:
            print("Invalid category selection. Please try again.")
            
    def dispense_item(self, category, item_name):
        # Decrease the quantity of the selected item from the vending machine inventory
        self.vending_machine[category][item_name]['quantity'] -= 1
        print(f"\nDispensing {item_name} from the {category} category. Enjoy!")

    def update_transaction_history(self, item, money_inserted, change):
        transaction = {
            'item': item,
            'money_inserted': money_inserted,
            'change': change,
        }
        self.transaction_history.append(transaction)

    def display_transaction_history(self):
        print("\n==== Transaction History ====")
        for transaction in self.transaction_history:
            print(f"Item: {transaction['item']}, Money Inserted: AED {transaction['money_inserted']:.2f}, "
                  f"Change: AED {transaction['change']:.2f}")

    def run_vending_machine(self):
        while True:
            self.display_menu()
            another_transaction = input("Do you want to make another transaction? (yes/no): ").lower()
            if another_transaction != 'yes':
                print("Thank you for using the Vending Machine!")
                self.display_transaction_history()
                break


vending_machine = VendingMachine()
vending_machine.run_vending_machine()
print('''
╭━━┳╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭━╮╱╱╱╱╱╱╭━┳╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭┳╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭╮
╰╮╭┫╰┳━╮╭━┳┫┣╮╭┳┳━┳┳╮┃━╋━┳┳╮╭┳┫━╋╋━┳┳━╮╭━━┳┳╮╭━┳━┳━┳━┳┳╯┣╋━┳┳━╮╭━━┳━╮╭━┫╰╋╋━┳┳━╮
╱┃┃┃┃┃╋╰┫┃┃┃━┫┃┃┃╋┃┃┃┃╭┫╋┃╭╯┃┃┣━┃┃┃┃┃╋┃┃┃┃┃┃┃╰╮┃╭┫┻┫┃┃┃╋┃┃┃┃┃╋┃┃┃┃┃╋╰┫━┫┃┃┃┃┃┃┻┫
╱╰╯╰┻┻━━┻┻━┻┻╯┣╮┣━┻━╯╰╯╰━┻╯╱╰━┻━┻┻┻━╋╮┃╰┻┻╋╮┃╱╰━╯╰━┻┻━┻━┻┻┻━╋╮┃╰┻┻┻━━┻━┻┻┻┻┻━┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯''')