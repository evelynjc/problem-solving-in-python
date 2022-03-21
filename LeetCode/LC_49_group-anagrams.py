str_dict = {}

for word in strs:
    ordered_str = "".join(sorted(word))
    if ordered_str in str_dict.keys():
        str_dict[ordered_str].append(word)
    else:
        str_dict[ordered_str] = [word]

anagrams = list(str_dict.values())
return anagrams