import csv
from warehouse.prioritization import OrderQueue

# Initialize the order queue
orders = OrderQueue()

# Function to load orders from a CSV file
def load_orders_from_file(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            priority = int(row["priority"])
            details = row["details"]
            orders.add_order(priority, details)
    print("Orders loaded successfully.")

# Add paths for warehouse simulation
print("Loading Orders...")
load_orders_from_file("orders.csv")

# Process orders
print("Processing Orders:")
while True:
    order = orders.process_order()
    if not order:
        break
    print(order)
