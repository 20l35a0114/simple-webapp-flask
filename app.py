import os
from flask import Flask
app = Flask(__name__)

color = "red"
@app.route("/")
def main():
    print(color)
    return render_templet ('hello.html', color=color)

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/who are you')
def hello2():
    return 'I am uday'    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
