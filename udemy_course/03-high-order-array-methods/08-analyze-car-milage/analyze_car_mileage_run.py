import analyze_car_mileage as a

cars = [
  { 'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'mileage': 30800 },
  { 'make': 'Honda', 'model': 'Civic', 'year': 2019, 'mileage': 32000 },
  { 'make': 'Chevrolet', 'model': 'Impala', 'year': 2021, 'mileage': 17500 },
  { 'make': 'Audi', 'model': 'R8', 'year': 2020, 'mileage': 13000 },
  { 'make': 'Tesla', 'model': 'Model 3', 'year': 2018, 'mileage': 50000 },
]

result = a.analyze_car_mileage(cars)

print(result)