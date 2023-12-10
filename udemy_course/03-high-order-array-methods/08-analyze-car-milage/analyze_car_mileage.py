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
