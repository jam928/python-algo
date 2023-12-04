# Challenge: Dice Game Simulation

## Instructions

Write a function called `dice_game_simulation` that simulates this dice game. The function should take one argument:

- `num_simulations`: The number of times to simulate the dice game.

The game rules are if a 7 or 11 are rolled, the player wins and they get a result of `win`. If a 2, 3 or 12 are rolled they lose and get a result of `lose`. Anything else and they get a result of `roll again`.

The function should return an array of objects, where each object represents a simulation result. Each object should contain the following properties:

- `dice1`: The value of the first dice (a random number between 1 and 6).
- `dice2`: The value of the second dice (a random number between 1 and 6).
- `sum`: The sum of the two dice values.
- `result`: The result of the roll, which can be "win", "lose", or "roll again".

### Function Signature

```python
def dice_game_simulation(num_simulations):
    """
    Simulates the dice game.
    :param num_simulations: The number of times to simulate the dice game.
    :type num_simulations: int
    :return: An array of simulation result objects.
    :rtype: list
    """
    # Your implementation here to simulate the dice game and return the result array
```

### Example

```python
print(dice_game_simulation(3));
/*
  { dice1: 1, dice2: 5, sum: 6, result: 'roll again' },
  { dice1: 5, dice2: 6, sum: 11, result: 'win' },
  { dice1: 1, dice2: 1, sum: 2, result: 'lose' }
*/
```

### Hints

- You can use the `Math.random()` function to simulate rolling a die. It returns a random number between 0 (inclusive) and 1 (exclusive).

## Solution

<details>
  <summary>Click For Solution</summary>

```python
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
```

### Explanation

- The `dice_game_simulation` function simulates the dice game for the specified number of simulations. dice 1 and dice 2 variables simulate random numbers b/t 1-6
- Depending on the sum, the `result` property is determined according to the game rules.
- The results of each simulation are stored in an array of objects.

</details>

### Test Cases

```python
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
```
