from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('conversation.json', 'r') as f:
        conversation = json.load(f)
    return render_template('index.html', conversation=conversation)

if __name__ == '__main__':
    app.run()
