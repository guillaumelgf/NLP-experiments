import flask
import joblib
import numpy as np

app = flask.Flask(__name__)
pipeline = joblib.load('models/model.joblib')


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if flask.request.method == 'POST':
        title = flask.request.form['search']
    title = np.array([title])
    return pipeline.predict(title)[0]
