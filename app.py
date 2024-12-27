from flask import Flask, jsonify, request
import csv
from warehouse.prioritization import OrderQueue

app=Flask(__name__)
orders=OrderQueue()

# Function to load orders from a CSV file
def load_orders_from_csv(file_path):
    try:
        with open(file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                priority = int(row["priority"])
                details = row["details"]
                orders.add_order(priority, details)
        return {"status": "success", "message": "Orders loaded successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Load orders when the app starts
@app.route("/init_orders", methods=["GET"])
def initialize_orders():
    response=load_orders_from_csv("orders.csv")
    return jsonify(response)

# Endpoint to reload orders from a CSV file
@app.route("/reload_orders", methods=["POST"])
def reload_orders():
    file_path=request.json.get("file_path", "orders.csv")
    response=load_orders_from_csv(file_path)
    return jsonify(response)

# Endpoint to process and return the next order
@app.route("/process_order", methods=["GET"])
def process_order():
    order=orders.process_order()
    if order:
        priority, details = order
        return jsonify({"priority": priority, "details": details})
    else:
        return jsonify({"message": "No more orders to process"})

if __name__=="__main__":
    # Explicitly call initialization before running the app
    load_orders_from_csv("orders.csv")
    app.run(debug=True)
