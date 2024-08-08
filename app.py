from flask import Flask, render_template, url_for
from flask import request as req 
import requests

app = Flask(__name__,static_url_path="/static/css/main.css")
@app.route("/",methods = ["GET","POST"])
def Index():
    return(render_template("index.html"))


@app.route("/get_summary",methods=["GET","POST"]) 
def get_summary():
    if req.method=="POST":

        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        input_text = req.form["input_text"] 
        output = query({
            "inputs": input_text
        })[0]

        return render_template("index.html", result = output["summary_text"]) 
    else:
        return(render_template("index.html"))




if __name__ == '__main__':
    app.debug = True 
    app.run()