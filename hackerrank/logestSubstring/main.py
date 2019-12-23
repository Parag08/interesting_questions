input_string_one = "AGGTAB"
input_string_two = "GXTXAYB"



def longest_substring(str_one, str_two):
    if len(str_one) < len(str_two):
        small_str = str_two
        long_str = str_one
    else:
        small_str = str_one
        long_str = str_two
    map_char = {}
    list_index = []
    for i in range(len(small_str)):
        map_char[i] = []
        for j in range(len(long_str)):
            if small_str[i] == long_str[j]:
                map_char[i].append(j)
                list_index.append(j)
    print(list_index)

def longest_substring_opt(str_one, str_two):
    if len(str_one) > len(str_two):
        small_str = str_two
        long_str = str_one
    else:
        small_str = str_one
        long_str = str_two
    longest_subtring
    for i in range(len(small_str)):
        map_char[i] = []
        for j in range(len(long_str)):
            if small_str[i] == long_str[j]:
                map_char[i].append(j)
                list_index.append(j)
    print(list_index)


longest_substring('GXTXAYB','AGGTAB')
