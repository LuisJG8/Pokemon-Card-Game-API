import pandas as pd


pd.reset_option('display.max_colwidth')


data = pd.read_csv("pocket_gym.csv")

hello = data.replace('—', '0')
hello.to_csv(path_or_buf='myfile')
