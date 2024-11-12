from collections import defaultdict
from typing import List

from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_food = defaultdict(SortedSet) # cuisine -> (rating, food)
        self.cuisines = {} # food -> cuisine
        self.ratings = {} # food -> rating

        for i in range(len(foods)):
            self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i])) # -rating since we want sorted in desc order
            self.cuisines[foods[i]] = cuisines[i]
            self.ratings[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        # get the cuisine of the current food
        cuisine = self.cuisines[food]

        # get the rating of the current food
        rating = self.ratings[food]

        # remove the current rating and food from the cuisines food map and add the new rating
        self.cuisines_food[cuisine].remove((-rating, food))
        self.cuisines_food[cuisine].add((-newRating, food))

        # update rating map
        self.ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        # [(-rating, food)]
        return self.cuisines_food[cuisine][0][1]

if __name__ == '__main__':
    food_ratings = FoodRatings(foods=["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                               cuisines=["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                               ratings=[9, 12, 8, 15, 14, 7])
    print(food_ratings.highestRated("korean")) # kimchi
    print(food_ratings.highestRated("japanese")) # ramen
    food_ratings.changeRating("sushi", 16)
    print(food_ratings.highestRated("japanese")) # sushi
    food_ratings.changeRating("ramen", 16)
    print(food_ratings.highestRated("japanese")) # ramen