
def split_list(lst, k):
    return [lst[i:i+k] for i in range(0, len(lst), k)]

my_list = [1,2,3,4,5]

print(split_list(my_list, 2))