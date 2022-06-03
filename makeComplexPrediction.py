from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.statespace.sarimax import SARIMAX

from random import random
import datetime
import pickle
from makeSeriesByWeight import *

sessions_df = pd.read_json("data/sessions.jsonl", lines=True)
sessions_df = sessions_df[sessions_df["event_type"] == "RETURN_PRODUCT"]
# ns_df = pd.read_json("data/sessions.jsonl", lines=True)

# dimension tables
# deliveries_df = pd.read_json("data/deliveries.jsonl", lines=True)
products_df = pd.read_json("data/products.jsonl", lines=True)
# users_df = pd.read_json("data/users.jsonl", lines=True)
# sessions_df = sessions_df.loc[sessions_df["event_type"] == "RETURN_PRODUCT"]
df = sessions_df.merge(products_df, on="product_id", how="left")

class MakeComplexPrediction:
    def makeData(df):
        df = make_desired_col_df(df)

        keys = ['10-30', '3-10', '1-3', '0.5-1', '0.2-0.5', '0-0.2']
        products_dict = dict.fromkeys(keys)

        tables_for_plot = make_count_prod_weight_by_weeks(df, products_dict, keys)
        return tables_for_plot

    def makeModel(data):
        model = ExponentialSmoothing(data)
        model_fit = model.fit()
        return model_fit

    def makePrediction(models, data, timeline):
        predictions = []
        for i in range(0, len(models)):
            yhat = models[i].predict(len(data[i][:timeline]), len(data[i][:timeline]))
            predictions.append(yhat[0])
        return predictions

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


    def predict(weeks_before, models):
        timeline = weeks_before
        predictions = MakeComplexPrediction.makePrediction(models, data, timeline)
        for i in range(0, len(predictions)):
            print(data[i])
            print(data[i][:timeline])

            print('estimated: ', predictions[i], '----> real: ', data[i][timeline])

        # TODO sum of 4 predictions
        prediction = 0
        for val in predictions:
            prediction += int(val)
        return prediction, data[i][timeline]

data = MakeComplexPrediction.makeData(df)

models = []
for category in data:
    model = MakeComplexPrediction.makeModel(category)
    models.append(model)
filename = 'make_complex_prediction_model.sav'
pickle.dump(models, open(filename, 'wb'))

if __name__ == '__main__':
    date = datetime.datetime(2022, 2, 15)
    weeks = MakeComplexPrediction.weeksBefore(date, 4)
    result = MakeComplexPrediction.predict(weeks, models)
    print(result)

    # SARIMA example
    # contrived dataset
    # data = [x + random() for x in range(1, 100)]
    # # fit model
    # model = SARIMAX(two_weeks_cups[:timeline], order=(1, 0, 0), seasonal_order=(0, 0, 0, 0))
    # model_fit = model.fit(disp=False)
    # # make prediction
    # yhat = model_fit.predict(len(two_weeks_cups[:timeline]), len(two_weeks_cups[:timeline]))
    # print(yhat)

