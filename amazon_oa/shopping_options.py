def get_number_of_options(price_of_jeans, price_of_shoes, price_of_skirts, price_of_tops, dollars):
    options = 0

    sum_map = {}

    # store A+B as key and its sum as value
    for price_of_jean in price_of_jeans:
        for price_of_shoe in price_of_shoes:
            ab = price_of_jean + price_of_shoe
            sum_map[ab] = sum_map.get(ab, 0) + 1

    # add up the values from -C+D
    for price_of_skirt in price_of_skirts:
        for price_of_top in price_of_tops:
            cd = dollars - (price_of_skirt+price_of_top)

            lst_set = {key for key in sum_map.keys() if key <= cd}
            for item in lst_set:
                options += sum_map.get(item)

    return options

if __name__ == '__main__':
    price_of_jeans = [2,3]
    price_of_shoes = [4]
    price_of_skirts = [2,3]
    price_of_tops = [1,2]
    dollars = 10
    options = get_number_of_options(price_of_jeans, price_of_shoes, price_of_skirts, price_of_tops, dollars)

    print(f"Options: {options}")