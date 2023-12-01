def display_likes(names):
    length_of_names = len(names)
    if length_of_names == 0:
        return "no one likes this"
    elif 1 == length_of_names:
        return f"{names[0]} likes this"
    elif 2 == length_of_names:
        return f"{names[0]} and {names[1]} like this"
    elif 3 == length_of_names:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {length_of_names - 2} others like this"