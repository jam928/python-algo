def title_case(str):
    words = str.lower().split(' ')

    result = []
    for index, item in enumerate(words):
        result.append(words[index][0].upper() + words[index][1:])

    return ' '.join(result)
