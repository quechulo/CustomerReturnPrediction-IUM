from flask import Flask, jsonify, request

app = Flask(__name__)

sample_request_data = {
        'day': 1,
        'month': "January",
        'year': 2022
    }


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def get_tasks():
    request_data = request.get_json()

    # do some kind of prediction
    predicted_number_of_returns = 10
    return f"Predicted number of returns for {request_data['day']} day of {request_data['month']} {request_data['year']} is {predicted_number_of_returns}"

if __name__ == '__main__':
    app.run(debug=True)