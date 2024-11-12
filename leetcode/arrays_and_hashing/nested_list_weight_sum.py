# T: O(N)
# S: O(D) # where d is the space depth using recursion
def nested_list_weight_sum(arr, depth):
    result = 0

    for i in range(len(arr)):
        if type(arr[i]) is list:
            result += nested_list_weight_sum(arr[i], depth + 1)
        else:
            result += arr[i] * depth

    return result

if __name__ == '__main__':
    arr = [[1,1],2,[1,1]]
    print(nested_list_weight_sum(arr, 1)) # 10

    arr = [1,[4,[6]]]
    print(nested_list_weight_sum(arr, 1)) # 27

    arr = [0]
    print(nested_list_weight_sum(arr, 1)) # 0