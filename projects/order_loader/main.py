from pathlib import Path

from loader import load_orders

path = Path("projects/order_loader/data/orders.json")

orders = load_orders(path)

print(orders)