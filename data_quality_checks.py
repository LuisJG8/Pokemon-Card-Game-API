import great_expectations as gx 
import pandas as pd
import sys 
import io 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# pd
df = pd.read_csv('./database/data/pokemon_ptcg_data.csv')
print(df)
poke_or_trainer = df["card_type"]
print(poke_or_trainer)

# gx
context = gx.get_context()

# gx suite 
# gx_suite_name = ("pokemon_pocket_tcg_suite")

# suite = context.suites.get(name=gx_suite_name)


data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})


# type 
p_type_rxpectation = gx.expectations.ExpectColumnValuesToBeOfType(column='type', type_="STRING")

def gx_dq_trainer(trainer_or_pokemon_gx):
    print(trainer_or_pokemon_gx)
    # item/trainer card
    if 'item' or 'tool' or 'supporter' in trainer_or_pokemon_gx.lower():

        p_name_type_expectation = gx.expectations.ExpectColumnValuesToBeOfType(column="name", type_="str")

        t_card_type = gx.expectations.ExpectColumnDistinctValuesToBeInSet(column="card_type", value_set=["Trainer/Item", "Trainer/Supporter", "Trainer/Tool"])

        t_description = gx.expectations.ExpectColumnValuesToNotBeNull(column="card_description")


        trainer_card_string_column = ['name','set','rarity','version','image']
        print('STRING')
        for column in trainer_card_string_column:
            print('name of column:' , column)
            check_for_string = gx.expectations.ExpectColumnValuesToNotBeNull(column=column)
            p_type_rxpectation = gx.expectations.ExpectColumnValuesToBeOfType(column='type', type_="STRING")
            validation_result = batch.validate(expect=check_for_string)
            print(validation_result)
            break

        trainer_card_null_columns = ['hp','type','sub_type','evolves_from','attacks','ex_rule','weaknesses','retreat_cost','card_description', 'pack','ability']
        for column in trainer_card_null_columns:
            print('name of column:' , column)
            check_for_null = gx.expectations.ExpectColumnValuesToBeNull(column=column, mostly=1.00)   
            validation_result = batch.validate(expect=check_for_null)
            print(validation_result)
            break

    elif trainer_or_pokemon_gx.lower() == 'pokémon':
        pass


# trainer_card_character_columns = []
# for column in trainer_card_character_columns:
#     trainer_card_type = gx.expectations.ExpectColumnDistinctValuesToBeInSet(column="card_type", value_set=['Trainer/Supporter', 'Trainer/Item'])
#     trainer_artist = gx.expectations.ExpectColumnValuesToBeOfType(column='trainer', type_="STRING")


for index, row in df.iterrows():
    print()
    print('index', index)
    print('row', row)
    card_type = row["card_type"]

    if card_type.lower() == "pokémon":
        # checks for name column
        print('it is a pokemon')

        
    elif card_type.lower() == "trainer/item" or card_type.lower() == "trainer/supporter":
        print(f'it is a {card_type}')
        gx_dq_trainer(card_type.lower())