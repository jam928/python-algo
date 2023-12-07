def calculate_total_sales_with_tax(products, tax_rate):
    total_price = sum(product['price'] * product['quantity'] for product in products)
    return total_price + float((tax_rate / 100.0) * total_price)