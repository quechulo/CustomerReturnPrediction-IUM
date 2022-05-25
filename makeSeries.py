import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as ss
import pandas as pd
import numpy as np
import datetime

from statsmodels.tsa.holtwinters import ExponentialSmoothing


# fact table
sessions_df = pd.read_json("data/sessions.jsonl", lines=True)

# dimension tables
# deliveries_df = pd.read_json("data/deliveries.jsonl", lines=True)
# products_df = pd.read_json("data/products.jsonl", lines=True)
# users_df = pd.read_json("data/users.jsonl", lines=True)

# print(sessions_df['event_type'])

sessions_df = sessions_df[sessions_df["event_type"] == "RETURN_PRODUCT"]

def make_two_weeks_cups(cups):
    two_weeks_cups = {
        '2019': np.zeros(27),
        '2020': np.zeros(27),
        '2021': np.zeros(27),
        '2022': np.zeros(27)
    }

    for key in cups:
        j = 0
        for i in range(1, 53, 2):
            two_weeks_cups[key][j] = cups[key][i] + cups[key][i + 1]
            j = j + 1

    # print(two_weeks_cups)
    all_knowledge_list = []
    all_knowledge_list.extend(two_weeks_cups['2019'])
    all_knowledge_list.extend(two_weeks_cups['2020'])
    all_knowledge_list.extend(two_weeks_cups['2021'])
    all_knowledge_list.extend(two_weeks_cups['2022'])

    return all_knowledge_list


def make_three_weeks_cups(cups):
    three_weeks_cups = {
        '2019': np.zeros(18),
        '2020': np.zeros(18),
        '2021': np.zeros(18),
        '2022': np.zeros(18)
    }

    for key in cups:
        j = 0
        for i in range(1, 52, 3):
            three_weeks_cups[key][j] = cups[key][i] + cups[key][i + 1] + cups[key][i + 2]
            j = j + 1

    # print(three_weeks_cups)
    all_knowledge_list = []
    all_knowledge_list.extend(three_weeks_cups['2019'])
    all_knowledge_list.extend(three_weeks_cups['2020'])
    all_knowledge_list.extend(three_weeks_cups['2021'])
    all_knowledge_list.extend(three_weeks_cups['2022'])

    return all_knowledge_list

def get_year_and_weeknum_df(df):
    weeks = df['timestamp'].dt.isocalendar().week
    years = df['timestamp'].dt.isocalendar().year
    result = pd.concat([years, weeks], axis=1)
    return result


if __name__ == "__main__":
    df = get_year_and_weeknum_df(sessions_df)
    # print(df)
    dates = df.values.tolist()
    cups = {
        '2019': np.zeros(54),
        '2020': np.zeros(54),
        '2021': np.zeros(54),
        '2022': np.zeros(54)
    }
    # print(dates)
    for event in dates:
        cups[str(event[0])][event[1]] += 1
    print(cups)
    two_weeks_cups = make_three_weeks_cups(cups)
    print(two_weeks_cups)
    plt.plot(two_weeks_cups)
    plt.show()
    all_knowledge_list = []
    all_knowledge_list.extend(cups['2019'])
    all_knowledge_list.extend(cups['2020'])
    all_knowledge_list.extend(cups['2021'])
    all_knowledge_list.extend(cups['2022'])
    print(all_knowledge_list)
    plt.plot(all_knowledge_list)
    plt.show()

    ###  PREDICT  ###
    timeline = len(all_knowledge_list) - 100
    model2 = ExponentialSmoothing(all_knowledge_list[:timeline])
    model_fit2 = model2.fit()
    yhat = model_fit2.predict(len(all_knowledge_list[:timeline]), len(all_knowledge_list[:timeline]))
    print('estimated: ', yhat, '----> real: ', all_knowledge_list[timeline])
