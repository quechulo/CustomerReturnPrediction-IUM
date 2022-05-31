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
    for event in dates:
        cups[str(event[0])][event[1]] += 1
    weeks_cups = make_four_weeks_cups(cups)
    # plt.plot(two_weeks_cups)
    # plt.show()
    return weeks_cups

def makeModel(data):
    model = ExponentialSmoothing(data)
    model_fit = model.fit()
    return model_fit

def makePrediction(model_fit, data, timeline):
    yhat = model_fit.predict(len(data[:timeline]), len(data[:timeline]))
    return yhat

def weeksBefore(date, numofweeks):
    weeks = date.isocalendar()[1]
    years = date.isocalendar()[0]
    if years == 2022:
        weeks = weeks + 53 * 3
    elif years == 2021:
        weeks = weeks + 53 * 2
    elif years == 2020:
        weeks = weeks + 53
    weeks = weeks // numofweeks
    return weeks


def predict(weeks_before, model):
    timeline = weeks_before
    prediction = makePrediction(model, data, timeline)

    print(data)
    print(data[:timeline])

    print('estimated: ', prediction, '----> real: ', data[timeline])
    return prediction

data = makeData()
model = makeModel(data)

if __name__ == '__main__':
    date = datetime.datetime(2022, 2, 15)
    weeks = weeksBefore(date, 4)
    predict(weeks, model)

    # SARIMA example
    # contrived dataset
    # data = [x + random() for x in range(1, 100)]
    # # fit model
    # model = SARIMAX(two_weeks_cups[:timeline], order=(1, 0, 0), seasonal_order=(0, 0, 0, 0))
    # model_fit = model.fit(disp=False)
    # # make prediction
    # yhat = model_fit.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    # print(yhat)

