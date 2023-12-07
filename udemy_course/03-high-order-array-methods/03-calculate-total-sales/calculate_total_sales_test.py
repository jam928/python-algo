import calculate_total_sales as c


def test_calculating_total_sales_amount_with_tax():
    products_1 = [
        {'name': 'Apple', 'price': 0.5, 'quantity': 10},
        {'name': 'Banana', 'price': 0.3, 'quantity': 20},
        {'name': 'Orange', 'price': 0.6, 'quantity': 15}
    ]
    products_2 = [
        {'name': 'Chocolate', 'price': 2.5, 'quantity': 5},
        {'name': 'Chips', 'price': 1.2, 'quantity': 10},
        {'name': 'Soda', 'price': 1.0, 'quantity': 8},
        {'name': 'Candy', 'price': 0.5, 'quantity': 15},
    ]
    assert c.calculate_total_sales_with_tax(products_1, 8) == 21.6
    assert c.calculate_total_sales_with_tax(products_2, 5) == 42
