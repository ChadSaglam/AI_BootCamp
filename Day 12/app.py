from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('salary.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    experience=float(request.form.get('experience'))
    exam=float(request.form.get('exam'))
    interview=float(request.form.get('interview'))

    guess=model.predict([[experience,exam,interview]])
    return render_template('index.html',guess='Our AI-estimated income: ${}'.format(guess[0][0]))

if __name__=="__main__":
    app.run(debug=True)

