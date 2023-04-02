# %%
import pandas as pd 
import os 
import pathlib
# pd.set_option("display.max_rows", 100)

from sudulunu.helpers import pp, make_num, dumper
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder

# from dotenv import load_dotenv
# load_dotenv()
# appy = os.environ['appy']

# %%



pathos = pathlib.Path(__file__).parent
out_path = f"{pathos}/inter"

in_path = f"{pathos}/input"

fillo = f'{in_path}/'

#%%

data = pd.read_csv(fillo)

# %%

df = data.copy()

pp(df)

#%%