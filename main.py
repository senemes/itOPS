import numpy as np

inventory_db = {
    'ItemA': {'current_stock': 100, 'monthly_sales': [120, 130, 110, 150, 140]},
    'ItemB': {'current_stock': 200, 'monthly_sales': [80, 70, 90, 60, 100]},
}

reorder_threshold_percentage = 0.25  # 25% of average monthly sales
reorder_quantity_factor = 1.5  # Order 150% of the average monthly sales


def predict_monthly_sales(item_sales_history):
    return np.mean(item_sales_history)


def check_inventory_and_reorder():
    for item, data in inventory_db.items():
        average_sales = predict_monthly_sales(data['monthly_sales'])
        threshold = average_sales * reorder_threshold_percentage

        if data['current_stock'] <= threshold:
            reorder_quantity = average_sales * reorder_quantity_factor
            print(f"Reorder signal for {item}. Suggested order quantity: {reorder_quantity:.2f}")
        else:
            print(f"{item} stock is sufficient.")


check_inventory_and_reorder()
