from flask import Flask, render_template,request,redirect
from helper import preprocessing, vectorizer, get_prediction

app = Flask(__name__)

data =dict()
reveiws =[]
positive=0
negative=0


@app.route("/")
def index():
    data['reviews'] = reveiws
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html', data=data)


@app.route("/", methods ={'post'})
def my_post():
    text = request.form['text']
    preproced_text = preprocessing(text)
    vectorized_text = vectorizer(preproced_text)
    prediction = get_prediction(vectorized_text)

    if prediction == 'positive':
        global positive
        positive+=1
    else:
        global negative
        negative+=1

    reveiws.insert(0, text)
    return redirect(request.url)

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()