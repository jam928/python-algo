import calculate_total_sales as c


products = [
  { 'name': 'Apple', 'price': 0.5, 'quantity': 10 },
  { 'name': 'Banana', 'price': 0.3, 'quantity': 20 },
  { 'name': 'Orange', 'price': 0.6, 'quantity': 15 },
]

result = c.calculate_total_sales_with_tax(products, 8)

print(result)