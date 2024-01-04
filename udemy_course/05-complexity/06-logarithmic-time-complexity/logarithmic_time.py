# /*
# Logarithmic Time (O(log n))
#
# Logarithmic time means that the time required to complete a function is proportional to the logarithm of the input data set.
#
# */
import time

mem_cache = {}
def find_power(base, exponent):
    if exponent == 0:
        return 1

    if (base, exponent) in mem_cache:
        return mem_cache.get((base, exponent))

    if exponent % 2 == 0:
        half_power = find_power(base, exponent // 2)
        result = half_power * half_power
        mem_cache.update({(base, exponent): result})
        return result

    half_power = find_power(base, (exponent - 1) // 2)
    result = base * half_power * half_power
    mem_cache.update({(base, exponent): result})
    return result


start = time.time()
print(find_power(2, 100))
end = time.time()
print(f"Find power 1 took: {end - start} ms")

start = time.time()
mem_cache = {}
print(find_power(2, 1000000))
end = time.time()
print(f"Find power 2 took: {end - start} ms")
