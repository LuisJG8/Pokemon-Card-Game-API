from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime, time
import sys
import io
import json
import csv
import os
import great_expectations as gx
import great_expectations.expectations as gxe
import pandas as pd
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# setting up the webdriver to connect to chrome browser
brave_path = r'C:\Users\luisg\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe'
# Setup ChromeOptions
options = Options()
options.binary_location = brave_path

driver = webdriver.Chrome(options=options)


columns = ['name','type','hp','card_type','sub_type','evolves_from',
           'attacks','ex_rule','weaknesses','retreat_cost','artist',
           'card_description','id','rarity','pack','set','version','image','ability']


# name,type,hp,card_type,sub_type,attacks,weaknesses,retreat_cost,artist,card_description,set,id,rarity,pack,versions,evolves_from,ex_rule,image,ability


with open('pokemon_ptcg_data.csv', 'w') as myfile:
    reading_csv = csv.writer(myfile)
    reading_csv.writerow(columns)


def clean_data_hyphen(pokemon_data_to_clean):
    print('clean hyphen function', pokemon_data_to_clean)

    hyphen_count = 0
    for hyphen in pokemon_data_to_clean:
        if hyphen == '-':
            hyphen_count += 1
            print('hyphen count is:', hyphen_count)
        

    if hyphen_count == 2:
        for i, j in enumerate(pokemon_data_to_clean):
            if j == '-':
                first_hyphen = pokemon_data_to_clean[i:]
                break

        string_without_first_hyphen = first_hyphen.strip('- ')

        for i, j in enumerate(string_without_first_hyphen):
            if j == '-':
                pokemon_type = string_without_first_hyphen[0:i]
                pokemon_hp = string_without_first_hyphen[i+2:]
                print('pok type', pokemon_type)
                # print(pokemon_hp)
                break

        for i, j in enumerate(pokemon_hp):
            if j == ' ':   
                pokemon_hp_num = pokemon_hp[0:i]
                pokemon_hp_string = pokemon_hp[i+1:]
                print('clean hyphen function', pokemon_hp_num)
                print(pokemon_hp_string)
                break
        
        return pokemon_type, pokemon_hp_num, pokemon_hp_string


    elif hyphen_count == 1:
        
        for i, j in enumerate(pokemon_data_to_clean):
            if j == '-':
                before_hyphen = pokemon_data_to_clean[0:i]
                after_hyphen = pokemon_data_to_clean[i+2:]
                print(before_hyphen)
                print(after_hyphen)
                break
        
        return before_hyphen, after_hyphen

def clean_name_symbols_and_packs(pokemon_n_s_p_to_clean):
    print('this is the param\n', pokemon_n_s_p_to_clean) 

    if 'pack' in pokemon_n_s_p_to_clean:
        counting_spaces = 0
        for thing, thing_two in enumerate(pokemon_n_s_p_to_clean):
            if thing_two == ' ':
                counting_spaces += 1
                if counting_spaces == 3:
                    card_number_and_rarity = pokemon_n_s_p_to_clean[0:thing].strip()
                    pokemon_pack = pokemon_n_s_p_to_clean[thing:].strip()
                    # print(card_number_and_rarity)
                    # print(pokemon_pack)

        for myindex, spaces in enumerate(card_number_and_rarity):
            if spaces == ' ':
                pokemon_number = card_number_and_rarity[0:myindex]
                pokemon_rarity = card_number_and_rarity[myindex:]

        return pokemon_number, pokemon_rarity, pokemon_pack
        
    elif 'pack' not in pokemon_n_s_p_to_clean:
        for x, y in enumerate(pokemon_n_s_p_to_clean):
            if y == ' ':
                pokemon_number = pokemon_n_s_p_to_clean[0:x]
                pokemon_rarity = pokemon_n_s_p_to_clean[x:]
                print(x)
                print(y)
                print('no pack')
                print('pokemon num', pokemon_number)
                print('pokemon rarity', pokemon_rarity)
                break
        return pokemon_number, pokemon_rarity


def clean_attack_or_attacks(data_to_clean):
    print(data_to_clean)
    for i, j in enumerate(data_to_clean):
        if j == ' ':
            global first_index
            first_index = i
            print('the first index', first_index)
            start_to_second_space = data_to_clean[0:i].strip()
            print('start to second', start_to_second_space)
            break
    # print()
    # print('last value', data_to_clean[-1])

    if data_to_clean[-1] == 'x' or data_to_clean[-1] == '+':
        # print('last value has x and an int before the x')
        for x, y in reversed(list(enumerate(data_to_clean))):
            if y == ' ':
                second_index = x
                break
        the_name_of_attack = data_to_clean[first_index:second_index].strip()
        attack_multiplier = data_to_clean[second_index:].strip()
        # print('name of attack:', the_name_of_attack, 'attack mult:', attack_multiplier)

    elif data_to_clean[-1].isdigit() == True:
        # print('last value is an int')
        for x, y in reversed(list(enumerate(data_to_clean))):
            if y == ' ':
                second_index = x
                break
        the_name_of_attack = data_to_clean[first_index:second_index].strip()
        attack_multiplier = data_to_clean[second_index:].strip()
        # print('name of attack:', the_name_of_attack, 'attack mult:', attack_multiplier)
    
    else:
        the_name_of_attack = data_to_clean[first_index:].strip()
        attack_multiplier = ''

    return start_to_second_space, the_name_of_attack, attack_multiplier


# this function works for all basic, stage1, stage2 and ex pokemon
def pokemon_card_data():
    pokemon_info = []

    try:
        card_name = driver.find_element(By.CLASS_NAME, value="card-text-name")
        pokemon_info.append(card_name.text)
        # print('card name:', card_name.text)
    except:
        print('no card name')
        pokemon_info.append('')

    try:
        card_type_and_hp = driver.find_element(By.CLASS_NAME, value="card-text-title")
        cleaned_string = clean_data_hyphen(card_type_and_hp.text)
        p_pokemon_type = cleaned_string[0].strip()
        p_pokemon_hp_num = cleaned_string[1]
        # p_pokemon_hp_string = cleaned_string[2]
        pokemon_info.extend([p_pokemon_type, p_pokemon_hp_num])
        # print('card element type:', p_pokemon_type)
        # print('card hp num:', p_pokemon_hp_num)
        # print('card hp string:', p_pokemon_hp_string)
    except:
        print('no type and no hp')
        pokemon_info.append('')


    try:
        card_rarity = driver.find_element(By.CLASS_NAME, value="card-text-type")
        print('card rarity element is ', card_rarity.text)
        cleaned_rarity = clean_data_hyphen(card_rarity.text.replace(' - Evolves from ', ' .    '))
        p_card_type = cleaned_rarity[0].strip()
        p_card_rarity = cleaned_rarity[1]
        print('card type', p_card_type)
        print('p card rarity', p_card_rarity)
        if 'Basic' not in p_card_rarity:
            for x, y in enumerate(reversed(list(p_card_rarity))):
                if y == '.':
                    print(y)
                    card_rarity_done = p_card_rarity[0:x-1]
                    card_type_done = p_card_rarity[x-1:]
                    print('one\n', card_rarity_done)
                    print('two\n', card_type_done)
                    break
            
            print(p_card_type, '   ', card_rarity_done, '   ', card_type_done.strip())
            pokemon_info.extend([p_card_type, card_rarity_done.replace('.', '').strip(), card_type_done.replace('.', '').strip()])

        elif 'Basic' in p_card_rarity:
            print('Basic in card rarity confirmed')
            pokemon_info.extend([p_card_type, p_card_rarity])
            print('card rarity:', p_card_rarity)
            print('card type:', p_card_type)
    except:
        print('no card rarity')
        pokemon_info.append('')

    try:
        evolves_from = driver.find_element(By.CSS_SELECTOR, value="p.card-text-type a")
        print('evolves from data ', evolves_from.text)
        if 'Evolves from' in evolves_from.text:    
            pokemon_info.append(evolves_from.text.replace('Evolves from', ''))
        # print('evolves from:', evolves_from.text)
    except:
        print('pokemon does not have evolves from')    
        pokemon_info.append('')

    # try:
    #     card_attack_energy = driver.find_element(By.CSS_SELECTOR, value="span.ptcg-symbol")
    #     pokemon_info.append(card_attack_energy.text)
    #     # print('card attack energy:', card_attack_energy.text)
    # except:
    #     print('no attack energy')


    try:
        card_attack_energy = driver.find_element(By.CSS_SELECTOR, value="span.ptcg-symbol")
        card_attack_name = driver.find_element(By.CLASS_NAME, value="card-text-attack-info")
        print('this is the card attack name\n', card_attack_name.text)
        attack_name_no_spaces = clean_attack_or_attacks(card_attack_name.text.strip())
        card_attack_name_clean = attack_name_no_spaces[1]
        card_attack_points_clean = attack_name_no_spaces[2]
        # print('this is the attack', card_attack_name_clean)
        # print('this is are the attack points', second_card_attack_points_clean)
    except:
        print('no card attack name')
        # print('card attack points:', card_attack_points_clean)
        pokemon_info.append('')

    else:           
        card_attack_description = driver.find_element(By.CSS_SELECTOR, value=".card-text-section .card-text-attack-effect")
        print('card attack name\n', card_attack_description.text)
        print('no attack description')

        # check if pokemon has a 2nd attack
        try:
            second_attack = driver.find_elements(By.CLASS_NAME, value="card-text-attack-info")
            # for thing in second_attack:
            #     print()
            #     print('printing second attack')
            #     print(thing.text)
            second_card_attack_name = second_attack[1]
            attack_name_no_spaces = clean_attack_or_attacks(second_card_attack_name.text.strip())
            second_attack_types = attack_name_no_spaces[0]
            second_card_attack_name_clean = attack_name_no_spaces[1]
            second_card_attack_points_clean = attack_name_no_spaces[2]
            # pokemon_info.extend([second_attack_types, second_card_attack_name_clean, second_card_attack_points_clean])
            

            card_attack_description_two = driver.find_element(By.CLASS_NAME, value="card-text-attack-effect")
            if card_attack_description_two != card_attack_description:
                pokemon_info.append(card_attack_description_two.text)
            print('second attack description', card_attack_description_two.text)
            if second_attack:
                list_of_attack_s_data = [
                                            {
                                                'name'        : card_attack_name_clean,
                                                'damage'      : card_attack_points_clean,
                                                'energy cost' : card_attack_energy.text,
                                                **({'attack description': card_attack_description.text} if card_attack_description.text else {})
                                        },
                                        {
                                            'name'         : second_card_attack_name_clean,
                                            'energy cost'  : second_attack_types,
                                            'damage'       : second_card_attack_points_clean,
                                            'description'  : card_attack_description_two
                                           }
                                        ]
                # pokemon_info.extend([card_attack_name_clean + ' attack points:' + card_attack_points_clean + ' attack energy:' + card_attack_energy.text 
                #                      + (' attack description: ' + card_attack_description.text if card_attack_description.text else '') + 'second attack name: ' + second_card_attack_name_clean + ' second attack energy' + second_attack_types + ' second attack points' + second_card_attack_points_clean 
                #                      + ' attack description' + card_attack_description_two])
                pokemon_info.append(str(list_of_attack_s_data))
        except:
            print('did not found second attack')
            only_one_attack_list = [{
                                    'name': card_attack_name_clean,
                                    'damage': card_attack_points_clean,
                                    'energy': card_attack_energy.text,
                                    **({'description': card_attack_description.text} if card_attack_description.text else {})
                                }]
            pokemon_info.append(str(only_one_attack_list))
            
    # try:
    #     # check if pokemon has a 2nd attack
    #     second_attack = driver.find_elements(By.CLASS_NAME, value="card-text-attack-info")
    #     # for thing in second_attack:
    #     #     print()
    #     #     print('printing second attack')
    #     #     print(thing.text)
    #     second_card_attack_name = second_attack[1]
    #     attack_name_no_spaces = clean_attack_or_attacks(second_card_attack_name.text.strip())
    #     second_attack_types = attack_name_no_spaces[0]
    #     second_card_attack_name_clean = attack_name_no_spaces[1]
    #     second_card_attack_points_clean = attack_name_no_spaces[2]
    #     pokemon_info.extend([second_attack_types, second_card_attack_name_clean, second_card_attack_points_clean])
    # except:
    #     print('no second attack')

    # else:
    #     card_attack_description_two = driver.find_element(By.CLASS_NAME, value="card-text-attack-effect")
    #     if card_attack_description_two != card_attack_description:
    #         pokemon_info.append(card_attack_description_two.text)
    #         print('second attack description', card_attack_description_two.text)


    try:
        finding_ex_rule = driver.find_elements(By.CSS_SELECTOR, value="div.card-text-section p")
        ex_rule = finding_ex_rule[7].text
        pokemon_info.append('Yes')
        # pokemon_info.append(ex_rule.replace('ex rule:', '').strip())
        # print('the ex rule:', ex_rule.strip())
    except:
        print('no ex description rule')
        pokemon_info.append('No')

    try:
        pokemon_weaknes_and_retreat = driver.find_element(By.CLASS_NAME, value="card-text-wrr")

        # print('the text', pokemon_weaknes_and_retreat.text)
        cleaning_string_weakness_and_retreat = pokemon_weaknes_and_retreat.text.replace('Weakness: ', '').replace('Retreat:', ',')
        for myindex, find_comma in enumerate(cleaning_string_weakness_and_retreat):
            if find_comma == ',':
                weakness = cleaning_string_weakness_and_retreat[0:myindex].strip()
                retreat_cost = cleaning_string_weakness_and_retreat[myindex+1:].strip()
        pokemon_info.extend([weakness, retreat_cost])
        # print('pokemon weakness:', weakness)
        # print('retreat:', retreat_cost)
    except:
        print('no weaknes and retreat')
        pokemon_info.append('')


    try:
        artist = driver.find_element(By.CSS_SELECTOR, value=".card-text-section.card-text-artist a")
        pokemon_info.append(artist.text)
        # print('artist: ', artist.text)
    except:
        print('no artist')
        pokemon_info.append('')

    try:
        driver.find_element(By.CSS_SELECTOR, value=".card-text-section.card-text-flavor")
        pokemon_description = driver.find_element(By.CSS_SELECTOR, value=".card-text-section.card-text-flavor")
        pokemon_info.append(pokemon_description.text)  
        # print('pokemon description: ', pokemon_description.text)  
    except:
        print('no description')
        pokemon_info.append('')


    try:
        pokemon_num_in_pack = driver.find_element(By.CSS_SELECTOR, value=".prints-current-details span + span")
        cleaning_the_data = clean_name_symbols_and_packs(pokemon_num_in_pack.text.replace('·', '').strip())
        print(pokemon_num_in_pack.text)
        if 'pack' in pokemon_num_in_pack.text:
            pokemon_card_number = cleaning_the_data[0][1:].strip()
            pokemon_rarity_with_symbols = cleaning_the_data[1].strip()
            pokemon_pack_name = cleaning_the_data[2]
            print('pokemon card number three:', pokemon_card_number)
            print('pokemon rarity with symbols three: ', pokemon_rarity_with_symbols)
            print('pokemon pack name three:', pokemon_pack_name)
            pokemon_info.extend([pokemon_card_number, pokemon_rarity_with_symbols, pokemon_pack_name]) 
        
        elif 'pack' not in pokemon_num_in_pack.text:
            pokemon_card_number = cleaning_the_data[0][1:].strip()
            pokemon_rarity_with_symbols = cleaning_the_data[1]
            print('pokemon card number:', pokemon_card_number)
            print('pokemon rarity with symbols:', pokemon_rarity_with_symbols)
            pokemon_info.extend([pokemon_card_number, pokemon_rarity_with_symbols.strip(), '']) 

        # print('pokemon_pack_name:', pokemon_pack_name)
    except:
        print('no pokemon card number or rarity or name pack')  
        pokemon_info.append('')


    try:
        pokemon_pack = driver.find_element(By.CSS_SELECTOR, value=".prints-current-details .text-lg")
        pokemon_info.append(pokemon_pack.text) 
        # print('pokemon pack: ', pokemon_pack.text)
    except:
        print('no pokemon pack')
        pokemon_info.append('')


    try:
        pokemon_versions = driver.find_element(By.CLASS_NAME, value="card-prints .card-prints-versions") 
        pokemon_info.append(pokemon_versions.text.replace('VERSIONS\n', '').replace('\n', ' '))
        # print(pokemon_versions.text)
    except:
        print('there are not other versions')   
        pokemon_info.append('')


    try:
        pokemon_image = driver.find_element(By.CSS_SELECTOR, value=".card-image img")  
        # pokemon_info.append(pokemon_image.text)
        actual_image = pokemon_image.get_attribute("src")
        pokemon_info.append(actual_image)
        # print('pokemon card image: ', actual_image)
    except:
        print('no image')
        pokemon_info.append('')


    try:
        pokemon_special_ability = driver.find_element(By.CLASS_NAME, value="card-text-ability-info") 
        cleaned_ability = pokemon_special_ability.text.strip().replace('Ability: ', '')
        print('pokemon ability', cleaned_ability)
        if pokemon_special_ability: 
            pokemon_special_ability_effect = driver.find_element(By.CLASS_NAME, value="card-text-ability-effect") 
            print(pokemon_special_ability_effect.text)
            pokemon_info.append(cleaned_ability + ' ' + pokemon_special_ability_effect.text)
    except:
        print('no special ability')
        pokemon_info.append('')



    print('\npokemon information:')
    for data_point in pokemon_info:
        print(data_point)
    print()   
    
    with open('pokemon_ptcg_data.csv', 'a', encoding='utf-8', newline='') as myfile:
        reading_csv = csv.writer(myfile)
        reading_csv.writerow(pokemon_info)

    print('list with pokemon data:\n', pokemon_info)
    
    return pokemon_info



def trainer_card_data():
    trainer_info = []

    try:
        card_name = driver.find_element(By.CLASS_NAME, value="card-text-name")
        trainer_info.append(card_name.text)
        # print('card name:', card_name.text)
    except:
        print('no card name')
        trainer_info.append('')

    try:
        card_rarity = driver.find_element(By.CLASS_NAME, value="card-text-type")
        cleaned_rarity = clean_data_hyphen(card_rarity.text)
        p_card_type = cleaned_rarity[0]
        p_card_rarity = cleaned_rarity[1]
        trainer_info.extend([p_card_type, p_card_rarity])
        # print('card rarity:', p_card_rarity)
        # print('card type:', p_card_type)
    except:
        print('no card rarity')
        trainer_info.append('')


    try:                                                                              
        item_effect = driver.find_elements(By.CLASS_NAME, value="card-text-section") 
        second_element = item_effect[1]                                               
        print('item effect:', second_element.text)                                 
        trainer_info.append(second_element.text)                                           
    except:                                                                           
        print('no item effect info')                                                     
        trainer_info.append('')

    try:
        artist = driver.find_element(By.CSS_SELECTOR, value=".card-text-section.card-text-artist a")
        trainer_info.append(artist.text)
        # print('artist: ', artist.text)
    except:
        print('no artist')
        trainer_info.append('')

    try:
        pokemon_pack = driver.find_element(By.CSS_SELECTOR, value=".prints-current-details .text-lg")
        trainer_info.append(pokemon_pack.text) 
        # print('pokemon pack: ', pokemon_pack.text)
    except:
        print('no pokemon pack')
        trainer_info.append('')

    try:
        pokemon_num_in_pack = driver.find_element(By.CSS_SELECTOR, value=".prints-current-details span + span")
        cleaning_the_data = clean_name_symbols_and_packs(pokemon_num_in_pack.text.replace('·', '').strip())
        if 'pack' in cleaning_the_data:   
            pokemon_card_number = cleaning_the_data[0][1:]
            pokemon_rarity_with_symbols = cleaning_the_data[1].strip()
            pokemon_pack_name = cleaning_the_data[2]
            trainer_info.extend([pokemon_card_number, pokemon_rarity_with_symbols, pokemon_pack_name]) 
        elif 'pack' not in cleaning_the_data:
            pokemon_card_number = cleaning_the_data[0]
            pokemon_rarity_with_symbols = cleaning_the_data[1]
        # print('pokemon card number:', pokemon_card_number)
        # print('pokemon rarity with symbols:', pokemon_rarity_with_symbols)
        # print('pokemon_pack_name:', pokemon_pack_name)
        trainer_info.extend([pokemon_card_number, pokemon_rarity_with_symbols, pokemon_pack_name]) 
    except:
        print('no pokemon card number or rarity or name pack')  
        trainer_info.append('')

    try:
        pokemon_versions = driver.find_element(By.CLASS_NAME, value="card-prints .card-prints-versions") 
        trainer_info.append(pokemon_versions.text)
        # print(pokemon_versions.text)
    except:
        print('there are not other versions')   
        trainer_info.append('')

    try:
        pokemon_image = driver.find_element(By.CSS_SELECTOR, value=".card-image img")  
        # pokemon_info.append(pokemon_image.text)
        actual_image = pokemon_image.get_attribute("src")
        trainer_info.append(actual_image)
        # print('pokemon card image: ', actual_image)
    except:
        print('no image')
        trainer_info.append('')

    print('\npokemon information:')
    for data_point in trainer_info:
        print(data_point)
    
    
    return trainer_info


time.sleep(5)
driver.get("https://pocket.limitlesstcg.com/cards")
# time.sleep(2)

# clicking on pack of cards
card_pack = driver.find_elements(By.TAG_NAME, value='tr')
third_element = card_pack[5]
third_element.click()


the_card = len(driver.find_elements(By.CSS_SELECTOR, ".card-search-grid a"))
# select one card
# pokemon_card = the_card[66]
# pokemon_card.click()
# trainer_card_data()
# time.sleep(8)


counter = 0
# loop all the cards
for card_index in range(the_card):
    
    time.sleep(5)

    the_card = driver.find_elements(By.CSS_SELECTOR, ".card-search-grid a")

    # limit number of cards that are printed out
    counter += 1
    if counter == 5:
        break
        
    current_card = the_card[card_index]
    current_card.click()

    card_type = driver.find_element(By.CLASS_NAME, value="card-text-type")
    cleaned_rarity = clean_data_hyphen(card_type.text)
    p_card_type = cleaned_rarity[0].strip()


    # main function calls
    if p_card_type == 'Pokémon' or p_card_type == 'Basic' or 'Stage 1' or 'Stage 2':
        pokemon_card_data()
    elif p_card_type == 'Trainer' or p_card_type == 'Item':
        trainer_card_data()

    driver.back()
