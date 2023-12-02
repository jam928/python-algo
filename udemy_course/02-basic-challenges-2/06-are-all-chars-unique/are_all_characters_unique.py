def are_all_characters_unique(word):
    if len(word) == 0:
        return True

    # use set to keep track of the characters in the word
    character_set = set()

    for c in word:
        if c in character_set:
            return False
        character_set.add(c)

    return True