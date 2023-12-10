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
