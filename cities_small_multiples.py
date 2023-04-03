# %%
import pandas as pd 
import os 
import pathlib
# pd.set_option("display.max_rows", 100)

from sudulunu.helpers import pp, make_num, dumper
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder


#%%

data = pd.read_excel('input/housing report numbers.xlsx', sheet_name='City', header=[0,1], index_col=[0])

# %%

df = data.copy()
# ('Sydney', 'New net annual dwelling supply'), 
# ('Sydney', 'New net  annual household formation'), 
# ('Sydney', 'Balance'), ('Melbourne', 'Year'), 
# ('Melbourne', 'New net annual dwelling supply'), 
# ('Melbourne', 'New net  annual household formation'), 
# ('Melbourne', 'Balance'), ('Brisbane', 'Year'), 
# ('Brisbane', 'New net annual dwelling supply'), 
# ('Brisbane', 'New net  annual household formation'), 
# ('Brisbane', 'Balance'), ('Perth', 'Year'), ('Perth', 'New net annual dwelling supply'), 
# ('Perth', 'New net  annual household formation'), ('Perth', 'Balance'), ('Adelaide', 'Year'), 
# ('Adelaide', 'New net annual dwelling supply'), ('Adelaide', 'New net  annual household formation'),
# ('Adelaide', 'Balance'), ('Hobart', 'Year'), ('Hobart', 'New net annual dwelling supply'), 
# ('Hobart', 'New net  annual household formation'), ('Hobart', 'Balance'), ('Darwin', 'Year'), 
# ('Darwin', 'New net annual dwelling supply'), ('Darwin', 'New net  annual household formation'), 
# ('Darwin', 'Balance'), ('ACT', 'Year'), ('ACT', 'New net annual dwelling supply'),
# ('ACT', 'New net  annual household formation'), ('ACT', 'Balance')

cols = [x for x in df.columns.tolist() if "Balance" in x[1]]
# cols.insert(0,('Melbourne', 'Year') )

df = df[cols]
df = df.reset_index()

# df.columns = df.iloc[0]

new_cols = [x[0] for x in df.columns.tolist()]
new_cols.pop(0)
new_cols.insert(0, 'Year')

df.columns = new_cols

for col in df.columns.tolist()[1:]:
    df[col] = pd.to_numeric(df[col])
    df[col] = df[col].cumsum()
    df[col] = 0 - df[col]

df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Year'] = df['Year'].dt.strftime("%Y-%m-%d")


piv = pd.melt(df, id_vars = ['Year'], value_vars=df.columns.tolist()[1:]).reset_index()
piv = piv[['Year', 'variable', 'value']]

# pp(df)
pp(piv)




# print(df.columns.tolist())
# %%


bye = piv
bye.fillna('', inplace=True)

final = bye.to_dict(orient='records') 
template = [
	{
    "title": f"Cumulative housing shortfall over the next 10 years, by city",
    "subtitle": f"Showing the difference between net annual supply and household formation (demand)",
    "footnote": "",
    "source": "| Source: National Housing Finance and Investment Corporation",
    "dateFormat": "%Y-%m-%d",
    "xAxisLabel": "",
    "yAxisLabel": "",
    "timeinterval": "",
    "tooltip": "",
    "baseline": "",
    "periodDateFormat": "%Y-%m-%d",
    "margin-left": "",
    "margin-top": "",
    "margin-bottom": "",
    "margin-right": "",
    "xAxisDateFormat": "%Y-%m-%d"
	}
]

# from modules.yachtCharter import yachtCharter
from yachtcharter import yachtCharter
testo = "-testo"
# testo = ''
chart_key = f"oz-datablogs-housing-short-fall-cities-small-multiples{testo}"
yachtCharter(template=template, 
			data=final,
            key = [],
            # key = [],
            # trendline = trends,
            # options=[{"colorScheme":"guardian", 'trendColors': '#94b1ca,#a9af2b,#a9af2b,#a9af2b'}],
            options=[{"scaleBy":"group", 'chartType': "area", "numCols": "2" }],
            chartId=[{"type":"smallmultiples"}],
			chartName=f"{chart_key}")