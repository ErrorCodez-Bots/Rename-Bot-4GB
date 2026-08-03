import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@JishuDeveloper'

if __name__ == "__main__":
    # Render / Koyeb வழங்கும் PORT-ஐ எடுத்து இயங்கும் வகையில் அமைக்கப்பட்டுள்ளது
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
