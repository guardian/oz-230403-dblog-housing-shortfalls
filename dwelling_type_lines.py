# %%
import pandas as pd 
import os 
import pathlib
# pd.set_option("display.max_rows", 100)

from sudulunu.helpers import pp, make_num, dumper
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder


#%%

data = pd.read_excel('input/housing report numbers.xlsx', sheet_name='Dwelling type')

# %%

df = data.copy()
# 'Unnamed: 0', 'Detached', 'Unnamed: 2', 'Unnamed: 3',
# 'Multi-unit', 'Unnamed: 5', 'Unnamed: 6'

# df['Balance'] = pd.to_numeric(df['Balance'])
# df['Balance'] = df['Balance'].cumsum()

# df = df[['Year', 'Balance']]

# df['Year'] = pd.to_datetime(df['Year'], format='%Y')
# df['Year'] = df['Year'].dt.strftime("%Y-%m-%d")

# df.rename(columns={"Balance": "Cumulative balance"}, inplace=True)

df = df[['Unnamed: 0', 'Unnamed: 3', 'Unnamed: 6']]
df = df[1:]

df.rename(columns={'Unnamed: 0': "Year", 'Unnamed: 3': "Detached homes", 'Unnamed: 6': "Apartments"}, inplace=True)


df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Year'] = df['Year'].dt.strftime("%Y-%m-%d")

for col in ["Detached homes", "Apartments"]:
    df[col] = pd.to_numeric(df[col])
    df[col] = df[col].cumsum()
    df[col] = 0 - df[col]

pp(df)
# %%


bye = df

# final = bye.to_dict(orient='records') 
# template = [
#     {
#     "title": f"Most of the shortfall will be in apartments",
#     "subtitle": f"Showing the cumulative difference between net annual supply and household formation (demand) for each dweling type",
#     "footnote": "",
#     "dateFormat": "%Y-%m-%d",
#     "source": "National Housing Finance and Investment Corporation",
#     "margin-left": "50",
#     "margin-top": "30",
#     "margin-bottom": "20",
#     "margin-right": "10",
#     "minY": -22000,
#     "xAxisDateFormat": "%Y"
# #     "tooltip":"<strong>{{#formatDate}}{{Date}}{{/formatDate}}</strong><br/> In ICU: {{ICU}}<br/>"
#     }
# ]

# from yachtcharter import yachtCharter
# # testo = "-testo"
# testo = ''
# chart_key = f"oz-datablogs-housing-short-fall-dwelling-type-cumulative-line{testo}"
# yachtCharter(template=template, 
#             data=final,
#             key = [],
#             chartId=[{"type":"linechart"}],
#             options=[{"colorScheme":"guardian", "lineLabelling":"TRUE"}],
#             chartName=f"{chart_key}{testo}")



# %%

zdf = df.copy()



pp(zdf)



bye = zdf 
bye.fillna('', inplace=True)

final = bye.to_dict(orient='records') 
template = [
	{
    "title": f"Most of the shortfall will be in apartments",
    "subtitle": f"Showing the cumulative difference between net annual supply and household formation (demand) for each dweling type",
	"footnote": "",
    "source": "| Source: National Housing Finance and Investment Corporation",
    "dateFormat": "%Y-%m-%d",
    "xAxisDateFormat": "%b %Y",
	"margin-left": "60",
	"margin-top": "30",
	"margin-bottom": "20",
	"margin-right": "10",
    "minY": '-30',
    "tooltip":"<strong> Shortfall</strong>: {{groupValue}} "
	}
]

from yachtcharter import yachtCharter
testo = "-testo"
# testo = ''
chart_key = f"oz-datablogs-housing-short-fall-dwelling-type-cumulative-bars{testo}"
yachtCharter(template=template, 
			data=final,
            key = [{"key":"Detached homes", "colour":'#005689'}, {"key":"Apartments", "colour":'#cc2b12'}],
            # trendline = trends,
            # options=[{"colorScheme":"guardian", 'trendColors': '#94b1ca,#a9af2b,#a9af2b,#a9af2b'}],
            # options=[{"colorScheme":"guardian"],
            chartId=[{"type":"stackedbar"}],
			chartName=f"{chart_key}")
# %%
