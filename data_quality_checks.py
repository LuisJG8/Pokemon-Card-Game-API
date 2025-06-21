import great_expectations as gx 
import pandas as pd

df = pd.read_csv('data/pokemon_ptcg_data.csv')
print(df)

context = gx.get_context()

data_source = context.data_sources.add_pandas("pandas")
data_asset = data_source.add_dataframe_asset(name="pd dataframe asset")

batch_definition = data_asset.add_batch_definition_whole_dataframe("batch definition")
batch = batch_definition.get_batch(batch_parameters={"dataframe": df})


# checks for name column
p_name_expectation = gx.expectations.ExpectColumnValuesToNotBeNull(column="name")
p_name_type_expectation = gx.expectations.ExpectColumnValuesToBeOfType(column="name", type_="str")

# type 
p_type_rxpectation = gx.

validation_result = batch.validate(expect=p_name_expectation)
print(validation_result)