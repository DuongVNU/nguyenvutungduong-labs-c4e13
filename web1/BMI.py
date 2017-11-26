from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "This is website to calculate your BMI!"

@app.route('/bmi/<int:w>/<float:h>')
def BMI(w, h):
    BMI = w / (h**2)
    print (BMI)
    if BMI < 16:
        return "You're severely underweight"
    elif BMI < 18.5:
        return "You're underweight"
    elif BMI < 25:
        return "You're normal"
    elif BMI < 30:
        return "You're overweight"
    else:
        return "You're obese"
if __name__ == '__main__':
  app.run(debug=True)
