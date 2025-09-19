from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV on startup
orders = pd.read_csv("orders.csv", dtype={"Order_ID": str})

@app.get("/order")
def get_order():
    order_id = request.args.get("order_id", "")
    row = orders.loc[orders["Order_ID"] == order_id]
    if row.empty:
        return jsonify({"found": False, "message": f"Order {order_id} not found"}), 404
    r = row.iloc[0].to_dict()
    return jsonify({
        "found": True,
        "order_id": r["Order_ID"],
        "status": r["Order_Status"],
        "expected_ship_date": r["Expected_Ship_Date"],
        "customer": r.get("Customer_Name"),
        "product": r.get("Product"),
        "qty": r.get("Qty")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
