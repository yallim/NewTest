from flask import Flask
import logging
from templates.test import show_strings

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/<string_value>')
def show_string(string_value):
    app.logger.info(f"Received string_value: {string_value}")
    print("release만의작업")
    print("열작업중")
    print("열작업중1")
    print("열작업중2")
    print("다른작업중;")
    print("다른작업중2;")
    print("다른작업중2;")
    print("다른작업중2;")
    
    return show_strings(string_value)


if __name__ == '__main__':
    app.run(debug=True,port=8080)