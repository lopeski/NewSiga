from flask import Flask, render_template

#init app 
app = Flask(__name__)

#README.md
@app.route('/')
def home():
    return render_template("index.html")

#run server
if __name__ == "__main__":
    app.run(debug=True)