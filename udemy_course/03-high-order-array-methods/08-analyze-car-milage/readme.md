# Challenge: Car Mileage Analysis

## Instructions

You are given an array of car objects, each containing information about a car's make, model, year, and mileage. Your goal is to perform some analysis on the car mileage data using high order array methods.

Implement a function called `analyze_car_mileage` which takes in an array of car objects and performs the following tasks:

1. Calculate the average mileage of all cars.
2. Find the car with the highest mileage.
3. Find the car with the lowest mileage.
4. Calculate the total mileage of all cars combined.

The function should return an object containing the calculated values as properties.

Here is an object that you can use to test your function in the run file:

```python
cars = [
  { 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'mileage': 30800 },
  { 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'mileage': 32000 },
  { 'make': 'Chevrolet', 'model': 'Impala', 'year': 2021, 'mileage': 17500 },
  { 'make': 'Audi', 'model': 'R8', 'year': 2020, 'mileage': 13000 },
  { 'make': 'Tesla', 'model': 'Model 3', 'year': 2018, 'mileage': 50000 },
]
```

### Function Signature

```python
from typing import List, Dict, Any

def analyze_car_mileage(cars: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Analyzes car mileage data using high order array methods.
    :param cars: An array of car dictionaries.
    :type cars: list of dict
    :return: An object containing calculated values.
    :rtype: dict
    """
    # Implementation of the function goes here
```

Each car object will have the following properties:

- `make`: The make of the car (string).
- `model`: The model of the car (string).
- `year`: The year the car was manufactured (number).
- `mileage`: The mileage of the car (number).

### Examples

```python
cars = [
    {'make': 'Toyota', 'model': 'Corolla', 'year': 2020, 'mileage': 25000},
    {'make': 'Honda', 'model': 'Civic', 'year': 2019, 'mileage': 30000},
    {'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'mileage': 15000},
  ]
analysis = a.analyze_car_mileage(cars)

print(analysis)
# Output:
# {
#   averageMileage: 23333.33,
#   highestMileageCar: { make: "Honda", model: "Civic", year: 2019, mileage: 30000 },
#   lowestMileageCar: { make: "Ford", model: "Mustang", year: 2021, mileage: 15000 },
#   totalMileage: 70000
# }
```

### Constraints

- The input array `cars` will contain at most 100 car objects.
- Each car object's `mileage` property will be a positive integer.
- Result should be rounded to 2 decimal places.

### Hints

- You can use the `sum` method for most of the calculations.

## Solution

<details>
  <summary>Click to view solution</summary>

```python
from typing import List, Dict, Any


def analyze_car_mileage(cars: List[Dict[str, Any]]) -> Dict[str, Any]:
    # Implementation of the function goes here
    mileage_amt_list = [car["mileage"] for car in cars]
    total_mileage = sum(mileage_amt_list)
    average_mileage = total_mileage / len(cars)
    highest_mileage_car = max((mileage, index) for index, mileage in enumerate(mileage_amt_list))
    lowest_mileage_car = min((mileage, index) for index, mileage in enumerate(mileage_amt_list))

    result = {
        "averageMileage": average_mileage,
        "highestMileageCar": cars[highest_mileage_car[1]],
        "lowestMileageCar": cars[lowest_mileage_car[1]],
        "totalMileage": total_mileage
    }

    return result
```

</details>

### Test Cases

```python
import analyze_car_mileage as a


def test_analyzing_car_mileage_data():
    cars = [
        {'make': 'Toyota', 'model': 'Corolla', 'year': 2020, 'mileage': 25000},
        {'make': 'Honda', 'model': 'Civic', 'year': 2019, 'mileage': 30000},
        {'make': 'Ford', 'model': 'Mustang', 'year': 2021, 'mileage': 15000},
    ]
    analysis = a.analyze_car_mileage(cars)

    assert analysis["averageMileage"] == 23333.333333333332
    assert analysis["highestMileageCar"] == {
        'make': 'Honda',
        'model': 'Civic',
        'year': 2019,
        'mileage': 30000,
    }

    assert analysis["lowestMileageCar"] == {
        'make': 'Ford',
        'model': 'Mustang',
        'year': 2021,
        'mileage': 15000,
    }

    assert analysis["totalMileage"] == 70000
```

Feel free to add more test cases to verify the correctness of your `analyzeCarMileage` function.
