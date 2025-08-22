from flask import Flask, render_template, request
from predictor import predict_colleges

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    rank = int(request.form['rank'])
    caste_gender = request.form['caste']
    branch = request.form['branch']

    df = predict_colleges(rank, caste_gender, branch)

    return render_template(
        'result.html',
        rank=rank,
        caste=caste_gender,
        branch=branch,
        df=df.to_html(classes='table table-striped', index=False)
    )

if __name__ == '__main__':
    app.run(debug=True)
