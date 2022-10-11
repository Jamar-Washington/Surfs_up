# Import Flask dependency
from flask import Flask

# Create flask app instance
app = Flask(__name__)

# Creater flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True)