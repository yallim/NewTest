from flask import Flask
import logging
from templates.test import show_strings

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

@app.route('/<string_value>')
def show_string(string_value):
    app.logger.info(f"Received string_value: {string_value}")
    print("새로추가할거~를 지움")
    print("new")
    print("새로운커밋")
    print("STASH1")
    print("d아멘드할거..")
    print("d제목만지정..")
    print("고칠거.!..±±!.")
    print("아멘드대상!")
    print("아멘드_최종..")
    print("찐최종")
    return show_strings(string_value)


if __name__ == '__main__':
    app.run(debug=True,port=8080)