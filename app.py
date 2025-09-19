from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from pathlib import Path

app = Flask(__name__)
CORS(app)

ORDERS = {}
csv_path = Path(__file__).parent / "orders.csv"
with csv_path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["Order_ID"] = str(row.get("Order_ID", "")).strip()
        ORDERS[row["Order_ID"]] = row

@app.get("/")
def health():
    return {"ok": True}

def try_int(v):
    try: return int(v)
    except: return v

@app.get("/order")
def get_order():
    order_id = request.args.get("order_id", "").strip()
    if not order_id:
        return jsonify({"found": False, "message": "order_id is required"}), 400
    row = ORDERS.get(order_id)
    if not row:
        return jsonify({"found": False, "message": f"Order {order_id} not found"}), 404
    return jsonify({
        "found": True,
        "order_id": row.get("Order_ID"),
        "status": row.get("Order_Status"),
        "expected_ship_date": row.get("Expected_Ship_Date"),
        "customer": row.get("Customer_Name"),
        "product": row.get("Product"),
        "qty": try_int(row.get("Qty"))
    })
