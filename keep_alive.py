from flask import Flask
import threading

app = Flask('')

@app.route('/')
def home():
    return "โปรแกรมกำลังทำงานครับ"

def run():
    app.run(host='0.0.0.0', port=8080)

def server_on():
    t = threading.Thread(target=run)
    t.start()
