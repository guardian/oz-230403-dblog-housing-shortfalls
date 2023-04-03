# %%
import pandas as pd 
import os 
import pathlib
# pd.set_option("display.max_rows", 100)

from sudulunu.helpers import pp, make_num, dumper
# from sudulunu.helpers import rand_delay, unique_in_col, null_in_col
# from sudulunu.helpers import combine_from_folder


#%%

data = pd.read_excel('input/housing report numbers.xlsx', sheet_name='National')

# %%

df = data.copy()
# 'Year', 'New net annual dwelling supply', 
# 'New net  annual household formation', 'Balance'

df['Balance'] = pd.to_numeric(df['Balance'])
df['Balance'] = df['Balance'].cumsum()

df['Balance'] = 0- df['Balance']

df = df[['Year', 'Balance']]

df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df['Year'] = df['Year'].dt.strftime("%Y-%m-%d")

df.rename(columns={"Balance": "Cumulative balance"}, inplace=True)

pp(df)

#%%

# bye = df

# final = bye.to_dict(orient='records') 
# template = [
#     {
#     "title": f"Cumulative housing shortfall over the next ten years",
#     "subtitle": f"Showing the difference between net annual supply and household formation (demand)",
#     "footnote": "",
#     "dateFormat": "%Y-%m-%d",
#     "source": "National Housing Finance and Investment Corporation",
#     "margin-left": "50",
#     "margin-top": "30",
#     "margin-bottom": "20",
#     "margin-right": "10",
#     "minY": -110000,
#     "xAxisDateFormat": "%Y"
# #     "tooltip":"<strong>{{#formatDate}}{{Date}}{{/formatDate}}</strong><br/> In ICU: {{ICU}}<br/>"
#     }
# ]

# from yachtcharter import yachtCharter
# # testo = "-testo"
# testo = ''
# chart_key = f"oz-datablogs-housing-short-fall-cumulative-line{testo}"
# yachtCharter(template=template, 
#             data=final,
#             key = [],
#             chartId=[{"type":"linechart"}],
#             options=[{"colorScheme":"guardian", "lineLabelling":"TRUE"}],
#             chartName=f"{chart_key}{testo}")


#%%


zdf = df.copy()

# zdf['Cumulative balance'] = 0 - zdf['Cumulative balance'] 


pp(zdf)



bye = zdf
bye.fillna('', inplace=True)

final = bye.to_dict(orient='records') 
template = [
	{
    "title": f"Cumulative housing shortfall over the next 10 years",
    "subtitle": f"Showing the difference between net annual supply and household formation (demand)",
	"footnote": "",
    "source": "| Source: National Housing Finance and Investment Corporation",
    "dateFormat": "%Y-%m-%d",
    "xAxisDateFormat": "%Y",
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
chart_key = f"oz-datablogs-housing-short-fall-cumulative-bars{testo}"
yachtCharter(template=template, 
			data=final,
            key = [],
            # trendline = trends,
            # options=[{"colorScheme":"guardian", 'trendColors': '#94b1ca,#a9af2b,#a9af2b,#a9af2b'}],
            options=[{"colorScheme":"guardian"}],
            chartId=[{"type":"stackedbar"}],
			chartName=f"{chart_key}")
# %%
