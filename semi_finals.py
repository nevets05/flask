from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return ('Steven B. Fischer'
            '3rd year, BSIT-A'
            'System Integration and Architecture 1'
            'Semi-final exam')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)