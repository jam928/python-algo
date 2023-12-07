# Challenge: Calculate Total Sales

## Instructions

Use the given array of product objects below, each with their name, price, and quantity sold. Additionally, you are given a tax rate as a percentage. Write a function called `calculate_total_sales_with_tax` that takes in an array of product objects, along with the tax rate, and returns the total sales amount including tax.

```js
const products = [
  { name: 'Apple', price: 0.5, quantity: 10 },
  { name: 'Banana', price: 0.3, quantity: 20 },
  { name: 'Orange', price: 0.6, quantity: 15 },
];
```

### Function Signature

```python
def calculate_total_sales_with_tax(products: List[Dict[str, float]], tax_rate: float) -> float:
    """
    Calculates and returns the total sales amount including tax from the input array of products and tax rate.
    :param products: The array of product dictionaries.
    :type products: list of dict
    :param tax_rate: The tax rate as a percentage.
    :type tax_rate: float
    :return: The total sales amount including tax.
    :rtype: float
    """
```

### Examples

```python
calculate_total_sales_with_tax(
  [
    { name: 'Apple', price: 0.5, quantity: 10 },
    { name: 'Banana', price: 0.3, quantity: 20 },
    { name: 'Orange', price: 0.6, quantity: 15 },
  ],
  8
) # 21.6 (20 + 8% tax)

calculate_total_sales_with_tax(
  [
    { name: 'Chocolate', price: 2.5, quantity: 5 },
    { name: 'Chips', price: 1.2, quantity: 10 },
    { name: 'Soda', price: 1.0, quantity: 8 },
    { name: 'Candy', price: 0.5, quantity: 15 },
  ],
  5
); # 42 (40 + 5% tax)
```

### Constraints

- The input array will contain at least one product object.
- The price and quantity values will be positive numbers.
- The tax rate will be a positive number less than 100.
- Round to 2 decimal places.

### Hints

- Calculate the total sales amount before applying the tax, and then add the tax amount to it.

## Solutions

<details>
  <summary>Click For Solution</summary>

This solution calculates the total sales amount including tax by iterating through the products, summing up the product of price and quantity for each product, and then adding the tax amount.

```python
def calculate_total_sales_with_tax(products, tax_rate):
    total_price = sum(product['price'] * product['quantity'] for product in products)
    return total_price + float((tax_rate / 100.0) * total_price)
```

## Explanation

- Calculate the total sales by using the `reduce` method to iterate through the products array, summing up the product of price and quantity for each product.
- Calculate the tax amount by multiplying the total sales by the tax rate and dividing by 100.
- Calculate the total sales including tax by adding the total sales and tax amount together.
- Return the total sales including tax.

</details>

### Test Cases

```python
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
```

Feel free to adjust the challenge or the test cases as needed. If you have any further questions or need additional assistance, please let me know!
