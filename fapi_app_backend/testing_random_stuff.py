# import sys 
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# rarity_types = ['◊', '◊◊', '◊◊◊', '◊◊◊◊', '☆', '☆☆', '☆☆', 'Crown Rare']

# patata = '◊◊◊◊'

# if patata in rarity_types:
#     print('yes')
# elif patata not in rarity_types:
#     print('nah')


# mys = 'Genetic Apex #4, Genetic Apex #251, Celestial Guardians #230,'

# split_versions_list = mys.split(',')

# new_versions_list = [thing.strip() for thing in split_versions_list]

# print(new_versions_list)


# pokemon_versions = []
# for index, my_string in enumerate(new_versions_list):
#     print('index', index, 'the len', len(new_versions_list))
#     if my_string.strip() in rarity_types:
#         string_before = new_versions_list[index-1]
#         pokemon_versions.extend([string_before + ' ' + my_string])
#     elif my_string.strip() not in rarity_types and index < len(new_versions_list) - 1 and new_versions_list[index+1] not in rarity_types:
#         pokemon_versions.append(my_string)
#     else:
#         print('idk')
#     print(pokemon_versions)


# print('outside', pokemon_versions)
raw_retreat_cost = None

hey = raw_retreat_cost if raw_retreat_cost is not None else 0

print(hey)