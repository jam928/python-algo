# /*
# Space Complexity: O(1)
# Time Complexity: O(1)
# */

def add(num1, num2):
  return num1 + num2

# /*
# Space Complexity: O(n)
# Time Complexity: O(n)
# */

def create_array(num):
  arr = []

  for i in range(num):
    arr.append(i)

  return arr

# /*
# Space Complexity: O(n^2)
# Time Complexity: O(n^2)
# */

def create_matrix(num):
  matrix = []

  for i in range(num):
    matrix[i] = []

    for j in range(num):
      matrix[i][j] = i + j

  return matrix

# /*
# Space Complexity: O(log n)
# Time Complexity: O(log n)
# */

def find_power(base, exponent):
  if exponent == 0:
    return 1

  if exponent % 2 == 0:
    half_power = find_power(base, exponent // 2)
    result = half_power * half_power
    return result

  half_power = find_power(base, (exponent - 1) // 2)
  result = base * half_power * half_power
  return result

# /*
# Space Complexity: O(1)
# Time Complexity: O(n)
# */

def find_sum(arr):
  sum = 0

  for i in range(len(arr)):
    sum += arr[i]

  return sum
