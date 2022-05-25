from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

from random import random

from makeSeries import *


if __name__ == '__main__':
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

    timeline = len(two_weeks_cups)-15
    print(two_weeks_cups)
    print(two_weeks_cups[:timeline])
    model = SimpleExpSmoothing(two_weeks_cups[:timeline])
    model_fit = model.fit()

    # make prediction
    yhat = model_fit.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    print('estimated: ', yhat, '----> real: ', two_weeks_cups[timeline])

    ##  Another model
    model2 = ExponentialSmoothing(two_weeks_cups[:timeline])
    model_fit2 = model2.fit()
    yhat = model_fit2.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    print('estimated: ', yhat, '----> real: ', two_weeks_cups[timeline])

    # SARIMA example
    # contrived dataset
    data = [x + random() for x in range(1, 100)]
    # fit model
    model = SARIMAX(two_weeks_cups[:timeline], order=(1, 0, 0), seasonal_order=(0, 0, 0, 0))
    model_fit = model.fit(disp=False)
    # make prediction
    yhat = model_fit.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    print(yhat)

