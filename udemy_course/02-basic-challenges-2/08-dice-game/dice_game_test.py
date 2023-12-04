import dice_game as dg


def test_dice_game_simulation():
    num_simulations = 100
    simulation_results = dg.dice_game_simulation(num_simulations)

    assert len(simulation_results) == num_simulations

    for result in simulation_results:
        dice1 = result["dice1"]
        dice2 = result["dice2"]
        total_sum = result["sum"]
        game_result = result["result"]

        assert dice1 >= 1
        assert dice1 <= 6

        assert dice2 >= 1
        assert dice2 <= 6

        assert total_sum >= 2
        assert total_sum <= 12

        if total_sum == 7 or total_sum == 11:
            assert game_result == 'win'
        elif total_sum == 2 or total_sum == 3 or total_sum == 12:
            assert game_result == 'lose'
        else:
            assert game_result == 'roll again'
