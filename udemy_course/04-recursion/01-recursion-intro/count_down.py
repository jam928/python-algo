def count_down(num):
    # base case
    if num <= 0:
        print('All done!')
        return

    print(num)
    num = num - 1
    count_down(num)