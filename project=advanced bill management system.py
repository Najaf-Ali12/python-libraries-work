bill_history = {}
def add(c):
    bill_history[c] = []
    while True:
        item = input(f"Enter the name of the item for {c}: ")
        try:
            size = float(input(f"Enter the quantity of {item}: "))
            r_price = float(input(f"Enter the retail price of the each {item}: "))
            t_price = float(input(f"Enter the trade price of the each {item}: "))
            disc = float(input(f"Enter the extra discount amount for the {item}: "))
            tax_p = float(input("Enter the percentage of tax applicable on total gross amount: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        gross_amount = t_price * size
        tax = gross_amount * tax_p / 100
        net_amount = gross_amount - disc + tax
        bill_history[c].append({
            "Item Name": item,
            "Sale Quantity(boxes)": size,
            "Retail Price": r_price,
            "Trade Price": t_price,
            "Gross Amount": gross_amount,
            "extra Discount": disc,
            "Tax Percentage": tax_p,
            "Tax Amount": tax,
            "Net Amount": net_amount,
        }
        )
        choice = input("Do you want to add more items for this customer? (yes/no): ")
        if choice.lower() != 'yes':
            break
def new():
    cust = input("Enter the name of the new customer: ")
    while True:
        if cust in bill_history.keys():
            print("there is already a bill on the name of",cust)
            add(customer)
            break
        item = input(f"Enter the name of the item for {cust}: ")
        try:
            size = float(input(f"Enter the quantity of {item}: "))
            r_price = float(input(f"Enter the retail price of the {item}: "))
            t_price = float(input(f"Enter the trade price of the {item}: "))
            disc = float(input(f"Enter the extra discount amount for the {item}: "))
            tax_p = float(input("Enter the percentage of tax applicable: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        gross_amount = t_price * size
        tax = gross_amount * tax_p / 100
        net_amount = gross_amount - disc + tax
        bill_history[cust]=[]
        bill_history[cust].append({
            "Item Name": item,
            "Sale Quantity(boxes)": size,
            "Retail Price": r_price,
            "Trade Price": t_price,
            "Gross Amount": gross_amount,
            "extra Discount": disc,
            "Tax Percentage": tax_p,
            "Tax Amount": tax,
            "Net Amount": net_amount,
        }
        )
        choice = input("Do you want to add more items for this customer? (yes/no): ")
        if choice.lower() != 'yes':
            break

def view():
    total_boxes = 0
    total_gross_amount = 0
    total_discount = 0
    total_tax = 0
    total_bill = 0
    
    for customer, items in bill_history.items():
        print("\nCUSTOMER NAME:{}\n".format(customer))
        for item in items:
            print("Item Name:", item["Item Name"])
            boxes = item["Sale Quantity(boxes)"]
            gross_amount = item["Gross Amount"]
            discount = item["extra Discount"]
            tax = item["Tax Amount"]
            net = item["Net Amount"]
            print("Sale Quantity(boxes):",boxes)
            print("Retail Price:",item["Retail Price"])
            print("Trade Price:",item["Trade Price"])
            print("Gross Amount:",gross_amount)
            print("extra Discount:",discount)
            print("Tax Percentage:",item["Tax Percentage"])
            print("Tax Amount:",tax)
            print("Net Amount:",net)
            print(" ")
            
            total_boxes += boxes
            total_gross_amount += gross_amount
            total_discount += discount
            total_tax += tax
            total_bill += net

    print(f"Total Boxes: {total_boxes}")
    print(f"Total Gross Amount: {total_gross_amount}")
    print(f"Total Discount: {total_discount}")
    print(f"Total Tax: {total_tax}")
    print(f"Total Bill: {total_bill}\n")

customer = input("Enter the name of the customer:")
while True:
    print("AVAILABLE CHOICES ARE:")
    try:
        ask = int(input('''1: add more items in bill of customer
2: create a new bill for a new customer
3: view bill history
4: exit
Enter 1, 2, 3, or 4: '''))
    except ValueError:
        print("ENTER A NUMBER")
        continue

    if ask == 1:
        add(customer)
    elif ask == 2:
        new()
    elif ask == 3:
        view()
    elif ask == 4:
        break
    else:
        print("INVALID CHOICE")
