# Order Lookup Agent

A simple Flask API that reads from a CSV file of sample orders and returns order info by ID.
Designed to demonstrate how you can import an API into IBM Watsonx Orchestrate as a custom skill.

## Endpoints

- **GET /order?order_id=1005** → returns JSON with order details.

## Setup

```bash
pip install -r requirements.txt
python app.py
