import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd
import numpy as np
import datetime

from makeSeries import *

sessions_df = pd.read_json("data/sessions.jsonl", lines=True)
sessions_df = sessions_df[sessions_df["event_type"] == "RETURN_PRODUCT"]
# ns_df = pd.read_json("data/sessions.jsonl", lines=True)

# dimension tables
deliveries_df = pd.read_json("data/deliveries.jsonl", lines=True)
products_df = pd.read_json("data/products.jsonl", lines=True)
# users_df = pd.read_json("data/users.jsonl", lines=True)
# sessions_df = sessions_df.loc[sessions_df["event_type"] == "RETURN_PRODUCT"]
df = sessions_df.merge(products_df, on="product_id", how="left")

def make_desired_col_df(df):
    weeks = df['timestamp'].dt.isocalendar().week
    years = df['timestamp'].dt.isocalendar().year
    result = pd.concat([df['category_path'], years, weeks, df['weight_kg'], df['price']], axis=1)

    return result

def make_count_prod_by_weeks(df, products_dict):
    dates = df.values.tolist()
    for key in products_dict:
        cups = {
            '2019': np.zeros(54),
            '2020': np.zeros(54),
            '2021': np.zeros(54),
            '2022': np.zeros(54)
        }
        products_dict[key] = cups

    for event in dates:
        products_dict[str(event[0])][str(event[1])][event[2]] += 1
    # print(products_dict)

    tables_for_plt = []
    for product in products_dict:
        all_knowledge_list = []
        all_knowledge_list.extend(products_dict[product]['2019'])
        all_knowledge_list.extend(products_dict[product]['2020'])
        all_knowledge_list.extend(products_dict[product]['2021'])
        all_knowledge_list.extend(products_dict[product]['2022'])

        tables_for_plt.append(all_knowledge_list)
        plt.plot(all_knowledge_list)
        plt.xlabel(product)
        plt.show()
    print(tables_for_plt)

if __name__ == "__main__":
    keys = df['category_path'].tolist()
    # print(len(keys))
    products_dict = dict.fromkeys(keys)
    print(len(products_dict))
    df = make_desired_col_df(df)

    tables_for_plot = make_count_prod_by_weeks(df, products_dict)
    # for elem in tables_for_plot:



    # for date in sessions:
    # print(df['category_path'])
