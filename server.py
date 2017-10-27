import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.debug = True
    # Bind to PORT if defined, otherwise default to 8030.
    port = int(os.environ.get('PORT', 8030))
    app.run(host='0.0.0.0', port=port)
