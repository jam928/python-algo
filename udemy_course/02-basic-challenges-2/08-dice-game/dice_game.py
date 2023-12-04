import random


def dice_game_simulation(num_simulations):
    simulations_result = []

    for i in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum = dice_1 + dice_2

        result = "roll again"

        if sum == 7 or sum == 11:
            result = 'win'
        elif sum == 2 or sum == 3 or sum == 12:
            result = 'lose'

        simulations_result.append({"dice1": dice_1, "dice2": dice_2, "sum": sum, "result": result})

    return simulations_result
