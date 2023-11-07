def title_case(str):
    words = str.lower().split(' ')

    for i in enumerate(words):
        words[i] = words[i][0].upper() + words[i][1:]

    return ' '.join(words)
