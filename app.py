from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('housing.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    arr = np.array([[data1, data2, data3, data4, data5]])
    pred = model.predict(arr)
    first_number = pred.item(0) * 10000
    print(first_number)
    return render_template('after.html', data=first_number)


if __name__ == "__main__":
    app.run(debug=True)