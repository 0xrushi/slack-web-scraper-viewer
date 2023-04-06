from flask import Flask, render_template
import json
import sys

app = Flask(__name__)

@app.route('/')
def index():
    with open(sys.argv[1], 'r') as f:
        conversation = json.load(f)
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python app.py file.json")
        exit(1)
    app.run()
