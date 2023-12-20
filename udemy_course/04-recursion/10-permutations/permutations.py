def permutations(s):
    def permutations_helper(list, temp_list, s):
        if len(temp_list) == len(s):
            list.append(''.join(temp_list))
            return

        for i in range(len(s)):
            if s[i] in temp_list:
                continue
            temp_list.append(s[i])
            permutations_helper(list, temp_list, s)
            temp_list.pop()

    result = []
    permutations_helper(result, [], s)
    return result

