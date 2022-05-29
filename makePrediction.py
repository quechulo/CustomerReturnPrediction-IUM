from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

from random import random
import datetime

from makeSeries import *




def makeData():
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
    # print(cups)
    two_weeks_cups = make_three_weeks_cups(cups)
    # print(two_weeks_cups)
    plt.plot(two_weeks_cups)
    plt.show()
    return two_weeks_cups

def makeModel(data, timeline):
    model = ExponentialSmoothing(data[:timeline])
    model_fit = model.fit()
    return model_fit

def makePrediction(model_fit, data, timeline):
    yhat = model_fit.predict(len(data[:timeline]), len(data[:timeline]))
    return yhat

def weeksBefore(date):
    weeks = date.isocalendar()[1]
    years = date.isocalendar()[0]
    if years == 2022:
        weeks = weeks + 53 * 3
    elif years == 2021:
        weeks = weeks + 53 * 2
    elif years == 2020:
        weeks = weeks + 53
    weeks = weeks // 3
    return weeks


def predict(weeks_before):
    timeline = weeks_before
    model = makeModel(data, timeline)
    prediction = makePrediction(model, data, timeline)

    print(data)
    print(data[:timeline])

    print('estimated: ', prediction, '----> real: ', data[timeline])
    return prediction

data = makeData()

if __name__ == '__main__':
    date = datetime.datetime(2020, 6, 15)
    weeks = weeksBefore(date)
    predict(weeks)

    # SARIMA example
    # contrived dataset
    # data = [x + random() for x in range(1, 100)]
    # # fit model
    # model = SARIMAX(two_weeks_cups[:timeline], order=(1, 0, 0), seasonal_order=(0, 0, 0, 0))
    # model_fit = model.fit(disp=False)
    # # make prediction
    # yhat = model_fit.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    # print(yhat)

