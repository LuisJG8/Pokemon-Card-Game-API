import pandas as pd
import numpy as np

ptcg_df = pd.read_csv('./data/pokemon_ptcg_data.csv', encoding='utf-8')


ptcg_df["retreat_cost"] = ptcg_df["retreat_cost"].astype("object") 
ptcg_df["hp"] = ptcg_df["hp"].astype("object")


ptcg_df_lenght = len(ptcg_df)
# print(ptcg_df)

df_length = ptcg_df.head(ptcg_df_lenght)

print(ptcg_df.iloc[[80]]['attacks'].isna())