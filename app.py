from flask import Flask, send_from_directory, render_template, request, abort
import sklearn
from waitress import serve
from src.models.card_classifier import card_predict
from src.utils import get_features #validate_input

app = Flask(__name__, static_url_path = "/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index3.html")

@app.route("/get_results", methods = ["POST"])
def get_results():
    """ Predict the approval (or not) of credit card application based on the inputs. """
    data = request.form
    print(data)

    selection = data['selection']
    test_value = get_features(selection)

    prediction = card_predict(test_value)

    if prediction == 1:
        prediction = 'Approved'
    else:
        prediction = 'Denied'

    return render_template("results.html", prediction = prediction)

    # test_value, errors = validate_input(data)

    # if not errors:
    #     prediction = card_predict(test_value)
    #     return render_template("results.html", prediction = prediction)
    # else:
    #     return abort(400, errors)

if __name__ == "__main__":
    serve(app, host = '0.0.0.0', port = 5000)