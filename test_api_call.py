# import requests


# POKEMON_TCG_API_KEY = '759fc2be-fb7c-471c-8b4b-858f9f9329cc'

# # API HEADERS
# api_header = {
#     'X-Api-Key': POKEMON_TCG_API_KEY
# }

# parameters = {
#     'name': 'charizard'
# }

# card_r = requests.get('https://api.pokemontcg.io/v2/cards', params=parameters)

# print(card_r.json())



# mystring = 'Pokémon - Stage 2 - Evolves from Cosmoem'
# mystring = 'Stage 1  Exeggcute'

# for x, y in enumerate(reversed(list(mystring))):
#     if y == ' ':
#         print(y)
#         hello = mystring[x:]
#         hi = mystring[0:x]
#         break
# print(hello.strip())
# print(hi)


# def clean_data_hyphen(pokemon_data_to_clean):
#     # print(pokemon_data_to_clean)

#     hyphen_count = 0
#     for hyphen in pokemon_data_to_clean:
#         if hyphen == '-':
#             hyphen_count += 1
#             # print('hyphen count is:', hyphen_count)
        

#     if hyphen_count == 2:
#         for i, j in enumerate(pokemon_data_to_clean):
#             if j == '-':
#                 first_hyphen = pokemon_data_to_clean[i:]
#                 break

#         string_without_first_hyphen = first_hyphen.strip('- ')

#         for i, j in enumerate(string_without_first_hyphen):
#             if j == '-':
#                 pokemon_type = string_without_first_hyphen[0:i]
#                 pokemon_hp = string_without_first_hyphen[i+2:]
#                 # print(pokemon_type)
#                 # print(pokemon_hp)

#         for i, j in enumerate(pokemon_hp):
#             if j == ' ':   
#                 pokemon_hp_num = pokemon_hp[0:i]
#                 pokemon_hp_string = pokemon_hp[i+1:]
#                 # print(pokemon_hp_num)
#                 # print(pokemon_hp_string)
        
#         return pokemon_type, pokemon_hp_num, pokemon_hp_string


#     elif hyphen_count == 1:
#         print('printing')
#         for i, j in enumerate(pokemon_data_to_clean):
#             if j == '-':
#                 before_hyphen = pokemon_data_to_clean[0:i]
#                 after_hyphen = pokemon_data_to_clean[i+2:]
#                 # print(before_hyphen)
#                 # print(after_hyphen)
#                 break
        
#         return before_hyphen, after_hyphen
    
# print(clean_data_hyphen(mystring))

# mystring = '#2  xyz  Lunala pack'
# mystrings = ' #3  x'

# def clean_name_symbols_and_packs(pokemon_n_s_p_to_clean):
#     # print('this is the param\n', pokemon_n_s_p_to_clean) 

#     if 'pack' in pokemon_n_s_p_to_clean:
#         counting_spaces = 0
#         for thing, thing_two in enumerate(pokemon_n_s_p_to_clean):
#             if thing_two == ' ':
#                 counting_spaces += 1
#                 if counting_spaces == 3:
#                     card_number_and_rarity = pokemon_n_s_p_to_clean[0:thing].strip()
#                     pokemon_pack = pokemon_n_s_p_to_clean[thing:].strip()
#                     print(card_number_and_rarity)
#                     print(pokemon_pack)

#         for myindex, spaces in enumerate(card_number_and_rarity):
#             if spaces == ' ':
#                 pokemon_number = card_number_and_rarity[0:myindex]
#                 pokemon_rarity = card_number_and_rarity[myindex:]

#         return pokemon_number, pokemon_rarity, pokemon_pack
        
#     elif 'pack' not in pokemon_n_s_p_to_clean:
#         for x, y in enumerate(pokemon_n_s_p_to_clean):
#             if y == ' ':
#                 pokemon_number = pokemon_n_s_p_to_clean[0:x]
#                 pokemon_rarity = pokemon_n_s_p_to_clean[x:]
#                 print(x)
#                 print(y)
#                 print('no pack')
#                 print('pokemon num', pokemon_number)
#                 print('pokemon rarity', pokemon_rarity)
#                 break
#         return pokemon_number, pokemon_rarity
        
    
# hello = clean_name_symbols_and_packs(mystrings.strip())
# print(hello)


# mys = 'Pokémon - Stage 1 - Evolves from Rowlet'

# def clean_data_hyphen(pokemon_data_to_clean):
#     print('clean hyphne function', pokemon_data_to_clean)

#     hyphen_count = 0
#     for hyphen in pokemon_data_to_clean:
#         if hyphen == '-':
#             hyphen_count += 1
#             print('hyphen count is:', hyphen_count)
        

#     if hyphen_count == 2:
#         for i, j in enumerate(pokemon_data_to_clean):
#             if j == '-':
#                 first_hyphen = pokemon_data_to_clean[i:]
#                 break

#         string_without_first_hyphen = first_hyphen.strip('- ')

#         for i, j in enumerate(string_without_first_hyphen):
#             if j == '-':
#                 pokemon_type = string_without_first_hyphen[0:i]
#                 pokemon_hp = string_without_first_hyphen[i+2:]
#                 print(pokemon_type)
#                 print(pokemon_hp)

#         for i, j in enumerate(pokemon_hp):
#             if j == ' ':   
#                 pokemon_hp_num = pokemon_hp[0:i]
#                 pokemon_hp_string = pokemon_hp[i+1:]
#                 print(pokemon_hp_num)
#                 print(pokemon_hp_string)
        
#         return pokemon_type, pokemon_hp_num, pokemon_hp_string


#     elif hyphen_count == 1:
        
#         for i, j in enumerate(pokemon_data_to_clean):
#             if j == '-':
#                 before_hyphen = pokemon_data_to_clean[0:i]
#                 after_hyphen = pokemon_data_to_clean[i+2:]
#                 # print(before_hyphen)
#                 # print(after_hyphen)
#                 break
        
#         return before_hyphen, after_hyphen


# hello = clean_data_hyphen(mys)
# cleaned_rarity = clean_data_hyphen(hello.replace(' - Evolves from ', ' '))
# print()
# print(hello[0])
# print(hello[1])
# print(hello[2])


mylist = []

card_attack_name_clean = 'Tackle'
card_attack_points_clean = 5
desc = 'It does a big tackle'
card_attack_energy = 'GG'


second_card_attack_name_clean = 'Surf'
second_card_attack_points_clean = 100
card_attack_description_two = 'It does surf'
second_attack_types = 'WW'


list_of_attack_data = [{
                        'name'  : card_attack_name_clean,
                        'damage': card_attack_points_clean,
                        'energy cost': card_attack_energy
                        },
                        # (' attack description: ' + card_attack_description.text if card_attack_description.text else ''),
                        {
                        'name': second_card_attack_name_clean,
                        'energy cost'  : second_attack_types,
                        'damage'       : second_card_attack_points_clean,
                        'description ' : card_attack_description_two
                        }
                        ]
newlist = []

print(list_of_attack_data)
