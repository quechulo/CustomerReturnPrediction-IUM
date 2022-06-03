from flask import Flask, jsonify, request
from makeComplexPrediction import MakeComplexPrediction
from makePrediction import MakePrediction
import pickle
import datetime
import random
from csv import DictWriter


app = Flask(__name__)

sample_request_data = {
        "model": 1,     # "test" / 0 / 1
        "day": 15,
        "month": 5,
        "year": 2022
    }

@app.route('/todo/api/v1.0/predictions', methods=['POST'])
def get_prediction():
    request_data = request.get_json()

    date = datetime.datetime(request_data['year'], request_data['month'], request_data['day'])
    weeks = MakePrediction.weeksBefore(date, 4)

    if request_data['model'] == "test":
        option = random.randint(0, 1)
    else:
        option = request_data['model']

    if option == 0:
        model_name = "make_prediction_model.sav"
        model = pickle.load(open(model_name, 'rb'))
        predicted_number_of_returns, real_value = MakePrediction.predict(weeks, model)
    if option == 1:
        model_name = "make_complex_prediction_model.sav"
        model = pickle.load(open(model_name, 'rb'))
        predicted_number_of_returns, real_value = MakeComplexPrediction.predict(weeks, model)

    result = {
        "day": request_data['day'],
        "month": request_data['month'],
        "year": request_data['year'],
        "predicted returns": int(predicted_number_of_returns),
        "real_value": real_value
    }
    evaluate = result.copy()
    evaluate["model name"] = model_name
    with open('evaluation_data.csv', 'a', newline='') as f_object:

        dictwriter_object = DictWriter(f_object, fieldnames=list(evaluate.keys()))
        dictwriter_object.writerow(evaluate)
        f_object.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
    get_tasks()
