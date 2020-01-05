from flask import Flask,render_template,request,url_for
import pandas as pd
import numpy as np


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def predict():
    url = "https://raw.githubusercontent.com/prateeksawhney97/Flask-Application-for-Spam-vs-Non-Spam-Classification/master/YoutubeSpamMergedData.csv"
    df= pd.read_csv(url)
    df_data = df[["CONTENT","CLASS"]]
    # Features and Labels
    df_x = df_data['CONTENT']
    df_y = df_data.CLASS
    # Extract Feature With CountVectorizer
    corpus = df_x
    cv = CountVectorizer() 
    X = cv.fit_transform(corpus) 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
    
    from sklearn.naive_bayes import MultinomialNB
    mnb = MultinomialNB()
    mnb.fit(X_train, y_train)
    mnb.score(X_test, y_test)
    if request.method == 'POST':
        comment = request.form['comment']
        data = [comment]
        vect = cv.transform(data).toarray()
        my_prediction = mnb.predict(vect)
    return render_template("results.html", prediction=my_prediction, comment=comment)

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=8080,debug=True)
