from locust import HttpUser, task, between
import random

class OrderLookupUser(HttpUser):
    wait_time = between(1, 3)  # seconds between requests

    @task
    def get_order(self):
        # pick a random order_id from your sample CSV
        order_id = random.choice(["1001", "1005", "1012"])
        self.client.get(f"/order?order_id={order_id}")
