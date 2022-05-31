from makeSeries import *
from makeSeriesByProduct import *

sessions_df = pd.read_json("data/sessions.jsonl", lines=True)
sessions_df = sessions_df[sessions_df["event_type"] == "RETURN_PRODUCT"]
# ns_df = pd.read_json("data/sessions.jsonl", lines=True)

# dimension tables
# deliveries_df = pd.read_json("data/deliveries.jsonl", lines=True)
products_df = pd.read_json("data/products.jsonl", lines=True)
# users_df = pd.read_json("data/users.jsonl", lines=True)
# sessions_df = sessions_df.loc[sessions_df["event_type"] == "RETURN_PRODUCT"]
df = sessions_df.merge(products_df, on="product_id", how="left")

def make_count_prod_weight_by_weeks(df, products_dict):
    dates = df.values.tolist()
    # print([i for i in dates if i[3] <= 10 and i[3] > 3])

    for key in products_dict:
        cups = {
            '2019': np.zeros(54),
            '2020': np.zeros(54),
            '2021': np.zeros(54),
            '2022': np.zeros(54)
        }
        products_dict[key] = cups

    for event in dates:
        if 0 < event[3] <= 0.2:
            products_dict['0-0.2'][str(event[1])][event[2]] += 1
        elif 0.2 < event[3] <= 0.5:
            products_dict['0.2-0.5'][str(event[1])][event[2]] += 1
        elif 0.5 < event[3] <= 1:
            products_dict['0.5-1'][str(event[1])][event[2]] += 1
        elif 1 < event[3] <= 3:
            products_dict['1-3'][str(event[1])][event[2]] += 1
        elif 3 < event[3] <= 10:
            products_dict['3-10'][str(event[1])][event[2]] += 1
        elif 10 < event[3] <= 30:
            products_dict['10-30'][str(event[1])][event[2]] += 1

    tables_for_plt = []

    for key in products_dict:
        ex = make_four_weeks_cups(products_dict[key])
        tables_for_plt.append(ex)
    #     plt.plot(ex)
    #     plt.xlabel(key)
    #     plt.show()
    # print(tables_for_plt)
    return tables_for_plt



if __name__ == "__main__":
    df = make_desired_col_df(df)

    keys = ['10-30', '3-10', '1-3', '0.5-1', '0.2-0.5', '0-0.2']
    products_dict = dict.fromkeys(keys)

    tables_for_plot = make_count_prod_weight_by_weeks(df, products_dict)

