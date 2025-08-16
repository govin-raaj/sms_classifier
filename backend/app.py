from flask import Flask,request,jsonify
import pickle
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


app = Flask(__name__)

ps=PorterStemmer()
tfidf=pickle.load(open("vectorizer.pkl",'rb'))
model=pickle.load(open("model.pkl",'rb'))



def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)   
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)        
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
           
    return " ".join(y)

@app.route("/")
def hello_world():
    return "Home page for sms spam classifier"


@app.route("/predict",methods=["POST"])
def predict():
    data=request.get_json()
    message = data.get("message", "")

    if message.strip() == "":
        return jsonify({"error": "Empty message received"}), 400
    
    transform_mssg=transform_text(message)
    x=tfidf.transform([transform_mssg])
    prediction=model.predict(x)[0]
    result = "Spam" if prediction == 1 else "Ham"

    return jsonify({
            "original_message": message,
            "processed_message": transform_mssg,
            "prediction": result,
            "prediction_raw": int(prediction)
        })

    
if __name__ == "__main__":
    app.run(debug=True)