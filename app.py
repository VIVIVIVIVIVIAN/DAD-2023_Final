from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    height = float(request.form['height']) / 100
    weight = float(request.form['weight'])
    bmi = round(weight / (height * height), 2)
    return render_template('calculate.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)